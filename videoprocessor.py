import os
import cv2
import logging as log
from pathlib import Path
from multiprocessing import Pool, cpu_count

class VideoProcessor:
    def __init__(self):
        """Initialize the VideoProcessor."""
        pass

    def get_videos(self, path):
        """Retrieve a list of .mp4 video files in the specified directory."""
        try:
            return [file for file in os.listdir(path) if file.endswith(".mp4")]
        except Exception as e:
            log.error(f"Error accessing directory: {e}")
            quit()

    @staticmethod
    def get_file_path():
        """Get the path to the current file's directory."""
        return str(Path(__file__).parent)

    @staticmethod
    def create_subdirectory(parent_dir, filename):
        """Create a subdirectory under the specified parent directory."""
        try:
            path = os.path.join(parent_dir, filename)
            os.makedirs(path, exist_ok=True)
        except Exception as e:
            log.error(f"Error creating sub-directory: {e}")
            quit()

    @staticmethod
    def create_directory(path):
        """Create a directory."""
        try:
            os.makedirs(path, exist_ok=True)
        except Exception as e:
            log.error(f"Error creating directory: {e}")
            quit()

    def split_video_directory(self, video_dir, filename, output_dir=None):
        """Set the filename to the defualt"""
        if filename == None:
            filename = 'dir'
        
        """Split videos in a directory into frames and save them to a subdirectory."""
        if output_dir is None:
            output_dir = os.path.join(self.get_file_path(), filename)
        
        videos = self.get_videos(video_dir)
        for video_file in videos:
            video_output_dir = os.path.join(output_dir, video_file)
            self.create_subdirectory(output_dir, video_file)
            self.split_video(os.path.join(video_dir, video_file), video_output_dir)

    def split_video(self, video_path, output_dir, create_dir=True):
        """Split a video into frames and save them to the specified directory."""
        if output_dir is None:
            output_dir = self.get_file_path() + "\\" + "dir"
        
        if create_dir:
            self.create_directory(output_dir)

        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            log.error('Failed to open video file.')
            return
        
        current_frame = 1
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                frame_name = f"{current_frame}.jpg"
                cv2.imwrite(os.path.join(output_dir, frame_name), frame)
                log.info(f"Creating: {frame_name}")
                current_frame += 1
            else:
                break

        cap.release()
        log.info('Video processing complete.')

if __name__ == '__main__':
    app = VideoProcessor()
    video_directory = 'C:/Assets/Programming/python/VideSplit/videos'
    videos = app.get_videos(video_directory)
    print(videos)
