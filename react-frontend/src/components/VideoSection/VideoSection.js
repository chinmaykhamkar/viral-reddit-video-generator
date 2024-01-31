import React from 'react'
import './VideoSection.css'
import videoSrc from '../../assets/viral.mp4'
const VideoSection = () => {
  return (
    <div className='video-section'>
      <div className='video-title'>
        Select <p className='template'>template</p> video
      </div>
      <div className='video'>
        <video src={videoSrc} width={300} type="video/mp4" controls></video>
      </div>
    </div>
  )
}

export default VideoSection