import sys
from pytube import YouTube


def main(link):
    yt = YouTube(link)
    print(yt.video_id)
    video.download('/Users/lihuigang/youtube')


if __name__ == '__main__':
    main('https://youtu.be/RjL8ftO8Vko')