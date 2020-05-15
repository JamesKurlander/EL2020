from flask import Flask, render_template, Response
from stream import Camera
from subprocess import call

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/button1")
def button1_click():
	call(["aplay", "/home/james/EL2020/final/audio_files/gahdeem.wav"])

@app.route("/button2")
def button2_click():
	call(["aplay", "/home/james/EL2020/final/audio_files/actions_have_consequences.wav"])

@app.route("/button3")
def button3_click():
	call(["aplay", "/home/james/EL2020/final/audio_files/its_time_to_stop.wav"])

@app.route("/button4")
def button4_click():
	call(["aplay", "/home/james/EL2020/final/audio_files/elevator_music.wav"])

@app.route("/button5")
def button5_click():
	call(["aplay", "/home/james/EL2020/final/audio_files/homer_simpson_lesson.wav"])

@app.route("/button6")
def button6_click():
	call(["aplay", "/home/james/EL2020/final/audio_files/it_was_at_this_moment.wav"])

@app.route("/button7")
def button7_click():
	call(["aplay", "/home/james/EL2020/final/audio_files/ready_to_rumble.wav"])

if __name__ == '__main__':
    app.run(host='192.168.1.204', port=2020, debug=True, threaded=True)
