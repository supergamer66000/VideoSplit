import os
import numpy as np
import argparse
import cv2

def makenewPath(foldername):
    if not os.path.exists(foldername):
        os.makedirs(foldername)
    else:
        print("path Already Exists")
        quit()

def main():

    # parse all args
    parser = argparse.ArgumentParser()
    #parser.add_argument('source', type=str, help='rick_roll.mp4')
    parser.add_argument('file', type=str, help='video')
    parser.add_argument('export', type=str, help="export folder name")
    args = parser.parse_args()
    
    # Makes a new path
    makenewPath(args.export)

    # get file path for desired video and where to save frames locally
    cap = cv2.VideoCapture(args.file)
    path_to_save = os.path.abspath(args.export)
    
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

if __name__ == '__main__':
    main()