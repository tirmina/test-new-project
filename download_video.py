import subprocess

def download_video(video_url, quality):
    # Command to download video with yt-dlp
    command = f'yt-dlp -f "bestvideo[height<={quality}]+bestaudio" -o output.mp4 {video_url}'
    
    # Run the command using subprocess
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    # Check if the download was successful
    if result.returncode == 0:
        return "Video downloaded successfully!"
    else:
        return "Video download failed."
