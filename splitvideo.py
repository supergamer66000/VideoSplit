from parser import ArgumentParser
from videoprocessor import VideoProcessor
import logging as log

if __name__ == '__main__':
    # Starts the parser
    ArgumentParser()
    arg = ArgumentParser().arg

    # checks if both are present
    if arg.file and arg.directory:
        print("You can not have both")
        quit()

    # Checks if one of the arguments are called
    if arg.file:
        VideoProcessor().splitVideo(path=arg.file, export=arg.folder)
    elif arg.directory:
        videos = VideoProcessor().getVideos(arg.directory)
        
        # Checks if the folder is empty
        if videos == []:
            log.warning('This Folder is Empty or does not contain .mp4 file format')
            quit()
        
        VideoProcessor().splitVideoDirectory(pathtoVideo=arg.directory, pathtoDir=arg.export, filename=arg.folder)