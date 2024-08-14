from parser import ArgumentParser
from videoprocessor import VideoProcessor

if __name__ == '__main__':
    # Starts the parser
    ArgumentParser()
    arg = ArgumentParser().arg

    # checks if both are present
    if arg.file and arg.directory:
        print("You can not have both")
        quit()

    if arg.file:
        VideoProcessor().splitVideo(path=arg.file, export=arg.export)
    elif arg.directory:
        videos = VideoProcessor().getVideos(arg.directory)
        if videos == []:
            print("Your Path is Empty or has no .mp4 files")
            quit()
        VideoProcessor().splitVideoDirectory(path=videos, export=arg.export)
    #print(ArgumentParser().getDirector())