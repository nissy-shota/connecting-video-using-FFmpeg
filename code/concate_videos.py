import subprocess
import glob
from moviepy.editor import *


def main():

    print('hello beautiful world')
    src_movies_path = '/home/shota/Projects/connecting-video-using-FFmpeg/movies/*mp4'
    movies_list_file = 'fileList.txt'

    files = glob.glob(src_movies_path)

    for file in files:
        cmd = f'ffmpeg -i {file} -vcodec h264 -acodec mp3 -b:v 5000k -r 25 -pix_fmt yuv420p mod{file}'
        subprocess.run(cmd, shell=True)
    print('converted')

    videos = []
    for file in files:
        video = VideoFileClip(file)
        videos.append(video)

    final_clip = concatenate_videoclips(videos)
    final_clip.write_videofile('merge.mp4', fps=25)


if __name__ == '__main__':

    main()