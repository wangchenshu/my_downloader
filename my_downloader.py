from __future__ import unicode_literals
import youtube_dl
import os
import sys

if len(sys.argv) < 2:
    print 'usage: python %s <youtube_url>' % (sys.argv[0])
    sys.exit()

download_url = sys.argv[1]
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([download_url])
