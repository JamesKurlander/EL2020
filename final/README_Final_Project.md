Here is the finalized version of my RoboBuddy final project.

DESCRIPTION: The code contained in this project was used to create a small desktop robot guardian that could fit inside of a metal can. It's capable of detecting motion, capturing an image of your desk space (and any possible intruders), playing a funny bit of audio to alert the intruder, emailing the user an image of the intruder along with a link to a livestream from the robot. From this livestream, there are a variety of buttons that the user can select to play funny audio clips from the robot to tease the intruder.

BREAKDOWN: This project consisted of multiple components/files which are listed below along with a brief description of the purpose they served:

  1. robo_buddy.py - used to run the detection, image capture, and emailing program.
  2. server.py - used to host a Flask server for the user to view live footage from the robot.
  3. stream.py - used to stream live video from the robot to the webpage.
  4. templates/index.html - used to design the webpage.
  5. templates/style.css - used to style the webpage.
  6. audio_files/ - used to hold a variety of funny .wav audio clips.

WALKTHROUGH: Below is a more in depth walkthrough on how to complete this project.

1. Writing the robo_buddy.py file:
  This file makes use of some GPIO and the standard Raspberry Pi camera module V2 through the use of the R PI.GPIO and picamera Python libraries. The program is comprised of the following functions:

  - detect() - runs idefinitely, checking the PIR sensor for any movement, as well as the touch sensor to see if the owner has disarmed the system. If an intruder is detected, the program plays an audio file to alert them that they've been caught and call the capture() function. If the owner disarms the system, the program immediately ends.
  - capture() - takes a snapshot of the intruder and sends it to the alert function.
  - alert() - composes an email to send to the owner containing an image of the intruder along with a link to a livestream from the robot's camera.
  
2. Getting audio to work:
  In audio to get audio working on the Pi, I used the alsamixer program (which was native to my Pi). The USB speaker had to be selected as the default audio device in the .conf file for ALSA, but once that was done, it was pretty much plug and play.

3. Setting up the webserver:
  Next came setting up the Flask server. This was heavily based off of the code we had written for our midterm project. The only difference was that the webpage is now being used to simply host a live video feed and an array of buttons to play sounds from the robot. The video feed works by sending a constant stream of images to the stream (@app.route'/video_feed'). The camera object is created by/imported from the stream.py file. This file contains functions to initialize the camera and actualyl snap an image. This calls "gen(camera)" which essentially just takes an image and sends it back. This process is called Motion JPEG. It's not the best quality, but it's low latency and is similar to what's used in CCTV security cameras.
