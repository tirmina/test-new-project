import subprocess

def convert_to_audio(video_url, start_time, end_time):
    # Define the FFmpeg command for conversion
    command = f'ffmpeg -i {video_url} -ss {start_time} -to {end_time} output_audio.mp3'  # Modify output format if needed
    
    # Execute the FFmpeg command
    try:
        subprocess.run(command, shell=True, check=True)
        print("Video successfully converted to audio!")
    except subprocess.CalledProcessError as e:
        print(f"Conversion failed: {e}")
        
# Example usage:
video_url = 'YOUR_VIDEO_URL_OR_FILE_PATH'
start_time = '00:00:35'  # Replace with desired start time
end_time = '00:04:54'  # Replace with desired end time

convert_to_audio(video_url, start_time, end_time) 
