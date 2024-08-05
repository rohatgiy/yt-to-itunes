from __future__ import unicode_literals
import os.path
import yt_dlp
import argparse

HOMEDIR = os.path.expanduser('~')

def main(ytdl_opts, url):
    with yt_dlp.YoutubeDL(ytdl_opts) as ytdl:
        ytdl.download([url])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download audio from YouTube.')
    parser.add_argument('url', type=str, help='YouTube or YouTube playlist URL')
    parser.add_argument('--format', type=str, default='bestaudio/best', help='Format of the audio')
    parser.add_argument('--codec', type=str, default='mp3', help='Preferred codec')
    parser.add_argument('--quality', type=str, default='192', help='Preferred quality')
    parser.add_argument('--ffmpeg-location', type=str, default='/usr/local/bin/ffmpeg', help='Location of ffmpeg')
    parser.add_argument('--output', type=str, default= HOMEDIR + '/Music/Music/Media.localized/Automatically Add to Music.localized/%(title)s.%(ext)s', help='Output directory template')
    parser.add_argument('--ignore-errors', default=True, action='store_true', help='Ignore errors during download')

    args = parser.parse_args()

    ytdl_opts = {
        'format': args.format,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': args.codec,
            'preferredquality': args.quality,
        }],
        'ffmpeg_location': args.ffmpeg_location,
        'outtmpl': args.output,
        'ignoreerrors': args.ignore_errors
    }

    main(ytdl_opts, args.url)