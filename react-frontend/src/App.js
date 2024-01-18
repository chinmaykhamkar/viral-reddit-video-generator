import React, { useState } from 'react';
import axios from 'axios';

const App = () => {
  const [text, setText] = useState('');
  const [video, setVideo] = useState(null);
  const [resultVideo, setResultVideo] = useState(null);
  const [loading, setLoading] = useState(false);  
  const handleTextChange = (e) => {
    setText(e.target.value);
  };

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    const reader = new FileReader();
     reader.onload = (e) => {
       setText(e.target.result);
     }
     reader.readAsText(file);
  };

  const handleVideoChange = (e) => {
    setVideo(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log("clicked")
    // FormData to send text and video file to the backend
    setLoading(true);
    const formData = new FormData();
    formData.append('text', text);
    formData.append('video', video);

    try {
      // Send data to Flask backend
      const response = await axios.post('http://127.0.0.1:5000/generate-video', formData, {
        responseType: 'blob',
      });
      const videoBlob = new Blob([response.data], { type: 'video/mp4' });
      // Set the result video for display
      setResultVideo(URL.createObjectURL(videoBlob));
    } catch (error) {
      console.error('Error submitting the form:', error);
    } finally {
      setLoading(false);  
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Text:
          <input type="text" value={text} onChange={handleTextChange} />
        </label>
        <br />
        <label>
          or Upload Text File:
          <input type="file" accept=".txt" onChange={handleFileChange} />
        </label>
        <br />
        <label>
          Video:
          <input type="file" accept="video/mp4" onChange={handleVideoChange} />
        </label>
        <br />
        <button type="submit">Submit</button>
      </form>
      {loading && <p>Loading...</p>}
      {resultVideo && (
        <div>
          <h2>Result Video:</h2>
          <video src={resultVideo} width={400} type="video/mp4" controls>
            Your browser does not support the video tag.
          </video>
          {/* <video width="400" controls>
            <source src={resultVideo} type="video/mp4" />
            Your browser does not support the video tag.
          </video> */}
        </div>
      )}
    </div>
  );
};

export default App;
