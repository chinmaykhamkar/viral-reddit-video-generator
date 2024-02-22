import React, { useState } from 'react'
import './VideoSection.css'
import HoverVideoPlayer from 'react-hover-video-player';

import videoSrc from '../../assets/viral.mp4'
import imageSrc from '../../assets/viral_still.jpg'
const VideoSection = () => {

  return (
    <div className='video-section'>
      <div className='video-title'>
        Select <p className='template'>template</p> video
      </div>
      <div className='video'>
        <div className='video-divs'>

          <HoverVideoPlayer
            videoSrc={videoSrc}
            pausedOverlay={
              <img
                src={imageSrc}
                alt=""
                style={{
                  // Make the image expand to cover the video's dimensions
                  width: '100%',
                  height: '100%',
                  objectFit: 'cover',
                }}
              />
            }

          />
        </div>

        <div className='video-divs'>
          <HoverVideoPlayer
            videoSrc={videoSrc}
            pausedOverlay={
              <img
                src={imageSrc}
                alt=""
                style={{
                  // Make the image expand to cover the video's dimensions
                  width: '100%',
                  height: '100%',
                  objectFit: 'cover',
                }}
              />
            }

          />
        </div>

        <div className='video-divs'>
          <HoverVideoPlayer
            videoSrc={videoSrc}
            pausedOverlay={
              <img
                src={imageSrc}
                alt=""
                style={{
                  // Make the image expand to cover the video's dimensions
                  width: '100%',
                  height: '100%',
                  objectFit: 'cover',
                }}
              />
            }

          />
        </div>

        <div className='video-divs'>
          <HoverVideoPlayer
            videoSrc={videoSrc}
            pausedOverlay={
              <img
                src={imageSrc}
                alt=""
                style={{
                  // Make the image expand to cover the video's dimensions
                  width: '100%',
                  height: '100%',
                  objectFit: 'cover',
                }}
              />
            }

          />
        </div>

        <div className='video-divs'>
          <HoverVideoPlayer
            videoSrc={videoSrc}
            pausedOverlay={
              <img
                src={imageSrc}
                alt=""
                style={{
                  // Make the image expand to cover the video's dimensions
                  width: '100%',
                  height: '100%',
                  objectFit: 'cover',
                }}
              />
            }

          />
        </div>
        <div className='video-divs'>
          <HoverVideoPlayer
            videoSrc={videoSrc}
            pausedOverlay={
              <img
                src={imageSrc}
                alt=""
                style={{
                  // Make the image expand to cover the video's dimensions
                  width: '100%',
                  height: '100%',
                  objectFit: 'cover',
                }}
              />
            }

          />
        </div>
        <div className='video-divs'>
          <HoverVideoPlayer
            videoSrc={videoSrc}
            pausedOverlay={
              <img
                src={imageSrc}
                alt=""
                style={{
                  // Make the image expand to cover the video's dimensions
                  width: '100%',
                  height: '100%',
                  objectFit: 'cover',
                }}
              />
            }

          />
        </div>

        <div className='video-divs'>
          <HoverVideoPlayer
            videoSrc={videoSrc}
            pausedOverlay={
              <img
                src={imageSrc}
                alt=""
                style={{
                  // Make the image expand to cover the video's dimensions
                  width: '100%',
                  height: '100%',
                  objectFit: 'cover',
                }}
              />
            }

          />
        </div>
        {/* <HoverVideoPlayer
          videoSrc={videoSrc}
          pausedOverlay={
            <img
              src={imageSrc}
              alt=""
              style={{
                // Make the image expand to cover the video's dimensions
                width: '100%',
                height: '100%',
                objectFit: 'cover',
              }}
            />
          }

        /> */}
      </div>
    </div>
  )
}

export default VideoSection