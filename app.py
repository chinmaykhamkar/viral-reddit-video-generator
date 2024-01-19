from flask import Flask, after_this_request, jsonify, render_template, request, send_file
from gtts import gTTS
from moviepy.editor import VideoFileClip,AudioFileClip,ImageSequenceClip, TextClip, concatenate_videoclips, CompositeVideoClip
import os
import cv2
from io import BytesIO
from flask_cors import CORS
import tempfile
import whisper
from tqdm import tqdm

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-video', methods=['POST'])
def generate_video():
        # Get text and video file from request parameters
        text_input = request.form['text']
        video_input = request.files['video']
        
        ## tts
        speech = gTTS(text_input, lang='en')
        speech_input = './file dump/speech.mp3'
        speech.save(speech_input)
        audio_clip = AudioFileClip(speech_input)
        
        ## open ai wishper
        model = whisper.load_model("base")
        transcribe = model.transcribe(speech_input)
        print(transcribe)        
        asp = 16/9   
        text_array = []
        # temp video path
        video_path = './file dump/input_video.mp4'
        video_input.save(video_path)

        # capture video in cap variable (cv2)
        cap = cv2.VideoCapture(video_path)
        ret, frame = cap.read()
        video_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        video_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        video_fps = cap.get(cv2.CAP_PROP_FPS)
        video_width = frame[:, int(int(video_width - 1 / asp * video_height) / 2):video_width - int((video_width - 1 / asp * video_height) / 2)].shape[1]
        video_width = video_width - (video_width * 0.1)
        for j in tqdm(transcribe['segments']):
            lines = []
            text = j['text']
            end = j['end']
            start = j['start']
            textsize = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)[0]
            char_width = int(textsize[0] / len(text))
            total_frames = int((end - start) * video_fps)
            start = start * video_fps
            total_chars = len(text)
            words = text.split(" ")
            i = 0      
             
            while i < len(words):
                words[i] = words[i].strip()
                if words[i] == "":
                    i += 1
                    continue
                length_in_pixels = len(words[i]) * char_width
                remaining_pixels = video_width - length_in_pixels-15
                line = words[i]
                
                while remaining_pixels > 0:
                    i += 1
                    if i >= len(words):
                        break
                    length_in_pixels = len(words[i]) * char_width
                    remaining_pixels -= length_in_pixels
                    if remaining_pixels < 0:
                        continue
                    else:
                        line += " " + words[i]
                
                line_array = [line, int(start) + 15, int(len(line) / total_chars * total_frames) + int(start) + 15]
                start = int(len(line) / total_chars * total_frames) + int(start)
                lines.append(line_array)
                text_array.append(line_array)       
        
        print(text_array)
        
        image_folder = os.path.join(os.path.dirname(video_path), "frames")
        if not os.path.exists(image_folder):
            os.makedirs(image_folder)
        
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        asp = width / height
        N_frames = 0
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame = frame[:, int(int(width - 1 / asp * height) / 2):width - int((width - 1 / asp * height) / 2)]
            
            for i in text_array:
                if N_frames >= i[1] and N_frames <= i[2]:
                    text = i[0]
                    text_size, _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)
                    text_x = int((frame.shape[1] - text_size[0]) / 2)
                    text_y = int((frame.shape[0] + text_size[1]) / 2)
                    cv2.rectangle(frame, (text_x - 10, text_y - 30), (text_x + text_size[0] + 10, text_y + text_size[1] + 10), (0, 0, 0), -1)
                    cv2.putText(frame, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                    break
            cv2.imwrite(os.path.join(image_folder,str(N_frames) + ".jpg"), frame)
            N_frames += 1
        cap.release()
        
        images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
        images.sort(key=lambda x: int(x.split(".")[0]))
        
        frames = cv2.imread(os.path.join(image_folder, images[0]))
        height, width, layers = frames.shape
        clip = ImageSequenceClip([os.path.join(image_folder, image) for image in images], fps=video_fps)
        # clip.set_audio(audio_clip)
        
                
        # Load the video clip
        # video_clip = VideoFileClip(video_path)
        
        speech_duration = audio_clip.duration
        video_duration = clip.duration
        
        # calculate how many times to repeat the video
        repeat_count = int(speech_duration / video_duration) + 1
        repeated_clips = [clip] * repeat_count
        final_clip = concatenate_videoclips(repeated_clips, method="compose")
        
        # trim video if speech duration is less than video duration
        final_clip = final_clip.subclip(0, speech_duration)
        
        # add speech to video 
        final_clip = final_clip.set_audio(audio_clip)

        # define output video path
        output_path = './final videos/output_video.mp4'
        final_clip.write_videofile(output_path)
        # final_clip.write_videofile(output_path)
        # res.write_videofile(output_path)

        # Cleanup: delete the temporary video file
        final_clip.close()
        # os.remove(speech_input)
        # os.remove(video_path)

        return send_file(output_path, as_attachment=True, download_name='output_video.mp4')
        



if __name__ == '__main__':
    app.run(debug=True)
