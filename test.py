import os
import cv2
import concurrent.futures
from tqdm import tqdm

def split_video(video_path, output_dir, create_dir=True, max_workers=4):
    """Split a video into frames and save them to the specified directory using a ThreadPool."""
    if output_dir is None:
        output_dir = get_file_path() + "\\" + "dir"
    
    if create_dir:
        self.create_directory(output_dir)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print('Failed to open video file.')
        return
    
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    def process_frame(frame_id, frame):
        """Process and save a single frame."""
        frame_name = f"{frame_id}.jpg"
        cv2.imwrite(os.path.join(output_dir, frame_name), frame)
        return frame_id

    frame_futures = []
    current_frame = 1

    # Create a ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor, tqdm(total=total_frames, desc="Splitting video into frames", unit="frame") as pbar:
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                # Submit frame processing to the thread pool
                future = executor.submit(process_frame, current_frame, frame)
                frame_futures.append(future)
                current_frame += 1
                pbar.update(1)
            else:
                break

    # Wait for all frames to be processed
    concurrent.futures.wait(frame_futures)

    cap.release()
    print('Video processing complete.')

split_video()