import pytube as pt
from pytube import YouTube
import sys
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("view: ", yt.views)

yd = yt.streams.get_lowest_resolution()

path = '/home/solo/Desktop'
yd.download(path)
print("Video downloaded to:", path)

