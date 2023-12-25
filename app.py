from flask import Flask, render_template, request, send_file
from gtts import gTTS
from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
from io import BytesIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-video', methods=['POST'])
def generate_video():
        # Get text and video file from request parameters
        text = request.get_json()
        print(text)
        # video_file = request.args.get('video', '')

        # # Convert text to speech
        # print(text, video_file)
        # speech = gTTS(text, lang='en')

        # # Save speech to a temporary file
        # temp_speech_file = "./temp_speech.mp3"
        # speech.save(temp_speech_file)

        # # Load video clip
        # video_clip = VideoFileClip(video_file)

        # # Calculate speech duration and video duration
        # speech_duration = speech.duration
        # video_duration = video_clip.duration

        # # Calculate how many times to repeat the video
        # repeat_count = int(speech_duration / video_duration) + 1

        # # Repeat the video clips and concatenate
        # repeated_clips = [video_clip] * repeat_count
        # final_clip = concatenate_videoclips(repeated_clips, method="compose")

        # # Trim the final clip if speech duration is less than video duration
        # if speech_duration < video_duration:
        #     final_clip = final_clip.subclip(0, speech_duration)

        # # Add speech to video
        # final_clip = final_clip.set_audio(temp_speech_file)
        # print("### here ####")
        # # Save the final video to a BytesIO object
        # video_buffer = BytesIO()
        # final_clip.write_videofile(video_buffer, codec='libx264', audio_codec='aac')

        # # Seek to the beginning of the buffer
        # video_buffer.seek(0)

        # # Cleanup temporary files
        # os.remove(temp_speech_file)
        # print("@@@@ here @@@@")
        # # Return the video file as a response
        # return send_file(video_buffer, mimetype='video/mp4', as_attachment=True, download_name='generated_video.mp4')
        return "text"

if __name__ == '__main__':
    app.run(debug=True)
