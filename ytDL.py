from pytube import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip
import sys
import os
videoURL = ""
if (len(sys.argv) > 1):
    videoURL = sys.argv[1]
if ("youtube.com" not in videoURL):
    videoURL = input("Enter YouTube URL: ")
yt = YouTube(videoURL,use_oauth=True,allow_oauth_cache=True)
filename = yt.title.replace(" ","_")
print("Downloading YouTube File: " + yt.title)
# Use a different filename for files because moviepy breaks when writing into the same filename
yt.streams.order_by("resolution").desc().first().download(filename=filename + "v.mp4")
yt.streams.filter(only_audio=True).first().download(filename=filename + "a.mp3")

video = VideoFileClip(filename + "v.mp4")
audio = AudioFileClip(filename + "a.mp3")

output = video.set_audio(audio)
output.write_videofile(filename + ".mp4")
os.remove(filename + "v.mp4")
os.remove(filename + "a.mp3")
