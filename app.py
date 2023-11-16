from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    video_url = request.form['video_url']
    action = request.form['action']
    
    if action == 'Download Video':
        quality = request.form['quality']
        command = f'yt-dlp -f "bestvideo[height<={quality}]+bestaudio/best[height<={quality}]" -o output.mp4 {video_url}'
        subprocess.run(command, shell=True)
        return "Video downloaded successfully! <a href='/'>Back</a>"
    
    elif action == 'Convert to Audio':
        start_time = request.form['start_time']
        end_time = request.form['end_time']
        command = f'ffmpeg -i {video_url} -ss {start_time} -to {end_time} output_audio.mp3'
        subprocess.run(command, shell=True)
        return "Conversion successful! <a href='/'>Back</a>"
    
    # Include handling for other functionalities like thumbnail download

if __name__ == '__main__':
    app.run(debug=True)
