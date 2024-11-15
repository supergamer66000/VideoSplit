import os
import cv2
import logging as log
from pathlib import Path
from datetime import datetime
from multiprocessing import Pool, cpu_count
import moviepy.video.io.ImageSequenceClip

class VideoProcessor:
    def __init__(self):
        pass

    def get_date_components(self, file_path):
        """Convertes file_path to a date"""
        path = Path(file_path)
        timestamp = path.stat().st_ctime
        date_time = datetime.fromtimestamp(timestamp)
        return [date_time.year, date_time.month, date_time.day]

    def get_objects(self, path, type, date=None):
        """Retrieve a list of .mp4 video files in the specified directory."""
        try:
            files = []
            for file in os.listdir(path):
                if file.endswith(str(type)) or file.endswith(str(type).upper()):
                    path_to_video = os.path.join(path, file)
                    file_dates = self.get_date_components(path_to_video)
                    if date is None:
                        files.append(file)
                    elif file_dates == date:
                        files.append(file)
            #return [file for file in os.listdir(path) if file.endswith(".MP4") or file.endswith('.mp4')]
            return files
        except Exception as e:
            log.error(f"Error accessing directory: {e}")
            quit()
    
    def get_object_length(self, path, type, date):
        return int(len(self.get_objects(path, date, type)))

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
            
    def build_video(self, image_dir, type=None, file_name=None, fps=None):
        """Build a video back into the .mp4 format"""
        if type is None:
            type = ".jpg"
        if file_name is None:
            file_name = "exported.mp4"
        if fps is None:
            fps = 24

        image_names = self.get_objects(image_dir, type)
        images = []
        for i in image_names:
            path = os.path.join(image_dir, i)
            images.append(path)
        
        if image_names == []:
            log.warn("The Directory is empty")
            return
        
        clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(images, fps)
        clip.write_videofile(file_name)
        
    def split_video(self, video_path, output_dir, create_dir=True):
        """Split a video into frames and save them to the specified directory."""
        if output_dir is None:
            output_dir = self.get_file_path() + "\\" + 'dir'
 
        if create_dir:
            self.create_directory(output_dir)

        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            log.error('Failed to open video file.')
            return
        
        length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        for i in range(length):
            ret, frame = cap.read()
            if ret:
                frame_name = f"{i}.jpg"
                cv2.imwrite(os.path.join(output_dir, frame_name), frame)
                log.info(f"Creating: {frame_name}")
        cap.release()
        log.info('Video processing complete.')

    def process_video(self, video_file_info):
        """Process a single video file."""
        video_dir, video_file, output_dir = video_file_info
        video_output_dir = os.path.join(output_dir, video_file)
        self.create_subdirectory(output_dir, video_file)
        self.split_video(os.path.join(video_dir, video_file), video_output_dir)
        print(f"Processed {video_file}")
    
    def process_video_with_cuda(self):
        pass

    def split_video_directory(self, video_dir, date, filename=None, output_dir=None, cores=None):
        """Split videos in a directory into frames using multiprocessing."""
        #print(f"{self.get_object_length(video_dir, date, type)} .mp4 videos")
        
        if filename is None:
            filename = 'exported'
        if output_dir is None:
            output_dir = os.path.join(self.get_file_path(), filename)
        if cores is None:
            cores=cpu_count()
        
        videos = self.get_objects(video_dir, date=date, type=".mp4")
        if videos == []:
            log.warn("The folder is empty")
        
        video_files_info = [(video_dir, video_file, output_dir) for video_file in videos]

        # Use multiprocessing to process each video in parallel
        with Pool(processes=cores) as pool:
            pool.map(self.process_video, video_files_info)

        print("done!")

if __name__ == '__main__':
    print("Why you running this?")