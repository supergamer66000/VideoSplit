import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--export', type=str)
args = parser.parse_args()

def createFileDirector(name):
    if not os.path.exists(name):
        os.makedirs(name)
    else:
        print("path Already Exists")
        quit()
    
createFileDirector(args.export)