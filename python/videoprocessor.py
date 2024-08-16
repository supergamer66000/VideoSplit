import os
import cv2
import logging as log
from pathlib import Path
from datetime import datetime
from multiprocessing import Pool, cpu_count
from tqdm import tqdm

class VideoProcessor:
    def __init__(self):
        pass

    def get_date_components(file_path):
        """Convertes file_path to a date"""
        path = Path(file_path)
        timestamp = path.stat().st_ctime
        date_time = datetime.fromtimestamp(timestamp)
        return [date_time.year, date_time.month, date_time.day]

    def get_videos(self, path):
        """Retrieve a list of .mp4 video files in the specified directory."""
        try:
            return [file for file in os.listdir(path) if file.endswith(".MP4") or file.endswith('.mp4')]
        except Exception as e:
            log.error(f"Error accessing directory: {e}")
            quit()
    
    def get_videos_length(self, path) -> int:
        return int(len(self.get_videos(path)))

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
            
    def get_file_data(self):
        pass

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

    def process_video(self, video_file_info):
        """Process a single video file."""
        video_dir, video_file, output_dir = video_file_info
        video_output_dir = os.path.join(output_dir, video_file)
        self.create_subdirectory(output_dir, video_file)
        self.split_video(os.path.join(video_dir, video_file), video_output_dir)
        print(f" Processed {video_file}")

    def split_video_directory(self, video_dir, filename=None, output_dir=None, cores=None):
        """Split videos in a directory into frames using multiprocessing."""
        print(f"{self.get_videos_length(video_dir)} videos")
        video_count = self.get_videos_length(video_dir)
        
        if filename is None:
            filename = 'dir'
        if output_dir is None:
            output_dir = os.path.join(self.get_file_path(), filename)
        if cores is None:
            cores=cpu_count()
        
        videos = self.get_videos(video_dir)
        video_files_info = [(video_dir, video_file, output_dir) for video_file in videos]

        # Use multiprocessing to process each video in parallel
        with Pool(processes=cores) as pool:
            list(tqdm(pool.imap(self.process_video, video_files_info), total=video_count, bar_format='{desc:<5.5}{percentage:3.0f}%|{bar:10}{r_bar}'))

        print("done!")

if __name__ == '__main__':
    print('Dont run this')
    quit()