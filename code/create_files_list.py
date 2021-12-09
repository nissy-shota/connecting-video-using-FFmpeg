import glob


def main():
    print('hello beautiful world')
    src_movies_path = '/home/shota/Projects/connecting-video-using-FFmpeg/movies/*mp4'
    movies_list_file = 'fileList.txt'

    files = glob.glob(src_movies_path)

    with open(movies_list_file, mode='w') as f:
        for file in files:
            f.write(f'file \'{file}\' \n')


if __name__ == '__main__':
    main()