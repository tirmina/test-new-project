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
        command = f'ffmpeg -i "{video_url}" -ss {start_time} -to {end_time} output_audio.mp3'
        subprocess.run(command, shell=True)
        return "Conversion successful! <a href='/'>Back</a>"

import os
import requests

@app.route('/download_thumbnail', methods=['POST'])
def download_thumbnail():
    video_url = request.form['video_url']
    thumbnail_url = f'http://img.youtube.com/vi/{video_url.split("v=")[1]}/0.jpg'
    thumbnail = requests.get(thumbnail_url)

    if thumbnail.status_code == 200:
        with open('thumbnail.jpg', 'wb') as file:
            file.write(thumbnail.content)
        return "Thumbnail downloaded successfully! <a href='/'>Back</a>"
    else:
        return "Thumbnail download failed. <a href='/'>Back</a>"

    
    # Include handling for other functionalities like thumbnail download


import os

# Access the API key from the environment variable
api_key = os.environ.get('YOUTUBE_API_KEY')

# Use the API key in your function
def your_function():
    # Your code using the API key here
    pass

