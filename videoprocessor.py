import os
from os import listdir
import numpy as np
import cv2
from multiprocessing import Pool, cpu_count
import logging as log
from pathlib import Path

# TODO: get subdirectories working

class VideoProcessor:
    def __init__(self):
        pass

    def getVideos(self, path):
        try:
            arr = os.listdir(path)
            parsedVideos = [i for i in arr if i.endswith(".mp4")]
            return parsedVideos
        except:
            log.error('Please check Spelling or if its a valid path')
            quit()

    def getFilePath(self):
        current_file_path = Path(__file__)
        parent_dir = current_file_path.parent
        parent_dir_str = str(parent_dir)
        return str(parent_dir_str)

    def createSubDirectory(self, parentDir, filename):        
        try:
            path = os.path.join(parentDir, filename)
            os.makedirs(path)
        except:
            log.error('There was an Error creating sub-directory')

    def createFileDirector(self, filename):
        try:
            os.makedirs(str(filename))
        except:
            log.error("there was an error. Perhaps the folder already exists")
            quit()

    def splitVideoDirectory(self, pathtoVideo, pathtoDir, filename):
        if pathtoDir == None:
            pathtoDir = self.getFilePath() + '/' + str(filename)
        
        for files in self.getVideos(pathtoVideo):
            #self.createSubDirectory(pathtoDir, files)
            self.splitVideo(str(pathtoVideo + '\\' + files), filename)

    #def splitVideoDirectory(self, video_files, export="frames"):
    #    # Create a multiprocessing Pool
    #    num_workers = min(len(video_files), cpu_count())  # Use the number of available CPUs or the number of videos, whichever is smaller
    #    with Pool(num_workers) as pool:
    #        # Pool.starmap allows us to pass multiple arguments to the worker function
    #        pool.starmap(self.splitVideo, [(video_file, export) for video_file in video_files])
    
    def splitVideo(self, path, filename):
        # if not called it will defualt to dir
        if not filename:
            filename = 'dir'
        # Creates the File Directory
        self.createFileDirector(filename)
        
        cap = cv2.VideoCapture(path)
        path_to_save = os.path.abspath(filename)
        
        current_frame = 1

        if (cap.isOpened() == False):
            print('Cap is not open')

        # cap opened successfully
        while(cap.isOpened()):

            # capture each frame
            ret, frame = cap.read()
            if(ret == True):

                # Save frame as a jpg file
                name = str(current_frame) + '.jpg'
                print(f'Creating: {name}')
                cv2.imwrite(os.path.join(path_to_save, name), frame)

                # keep track of how many images you end up with
                current_frame += 1
            
            else:
                break

            if current_frame == 50+1:
                break

        # release capture 
        cap.release()
        print('done')
        
if __name__ == '__main__':
    app = VideoProcessor()
    Videos = app.getVideos('C:/Assets/Programming/python/VideSplit/videos')
    print(Videos)