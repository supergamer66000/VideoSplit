import os
from os import listdir
import numpy as np
import cv2
from multiprocessing import Pool, cpu_count

class VideoProcessor:
    
    def __init__(self):
        pass

    def getVideos(self, path):
        try:
            arr = os.listdir(path)
            parsedVideos = [i for i in arr if i.endswith(".mp4")]
            return parsedVideos
        except:
            print("That is not a valid path")

    def createFileDirector(name):
        if not os.path.exists(name):
            os.makedirs(name)
        else:
            print("path Already Exists")
            quit()

    def splitVideoDirectory(self, path, export):
        print(self.getVideos(path))
        for files in self.getVideos(path):
            self.createFileDirector(str(files))
            self.splitVideo(files, export)

    #def splitVideoDirectory(self, video_files, export="frames"):
    #    # Create a multiprocessing Pool
    #    num_workers = min(len(video_files), cpu_count())  # Use the number of available CPUs or the number of videos, whichever is smaller
    #    with Pool(num_workers) as pool:
    #        # Pool.starmap allows us to pass multiple arguments to the worker function
    #        pool.starmap(self.splitVideo, [(video_file, export) for video_file in video_files])
    
    def splitVideo(self, path, export):
        self.createFileDirector(export)
        
        cap = cv2.VideoCapture(path)
        path_to_save = os.path.abspath("frames")
        
        current_frame = 1

        if (cap.isOpened() == False):
            print('Cap is not open')

        # cap opened successfully
        while(cap.isOpened()):

            # capture each frame
            ret, frame = cap.read()
            if(ret == True):

                # Save frame as a jpg file
                name = 'frame' + str(current_frame) + '.jpg'
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