import logging as log
from parser import ArgumentParser
from videoprocessor import VideoProcessor

def main():
    # Initialize the argument parser and parse arguments
    parser = ArgumentParser()
    args = parser.arg

    # Check if both file and directory arguments are provided
    if args.file and args.directory:
        log.info("You cannot specify both a file and a directory.")
        return

    video_processor = VideoProcessor()

    # Process a single file
    if args.file:
        video_processor.split_video(video_path=args.file, output_dir=args.folder)
    
    # Process a directory of videos
    elif args.directory:
        videos = video_processor.get_videos(args.directory)
        
        # Check if the directory is empty or contains no .mp4 files
        if not videos:
            log.warning('The directory is empty or does not contain any .mp4 files.')
            return
        
        video_processor.split_video_directory(video_dir=args.directory, output_dir=args.export, filename=args.folder, cores=args.core_count)

if __name__ == '__main__':
    main()
