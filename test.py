import os
from pathlib import Path

def getFilePath(self):
        current_file_path = Path(__file__)
        parent_dir = current_file_path.parent
        parent_dir_str = str(parent_dir)
        return str(parent_dir_str)

def createSubDirectory(parentDir, filename):
    try:
        path = os.path.join(parentDir, filename)
        os.makedirs(path)
    except:
        log.error('There was an Error creating sub-directory')
    
createSubDirectory('C:/Assets/Programming/python/VideSplit/a', "file")