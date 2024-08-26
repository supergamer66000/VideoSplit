import argparse
import sys
import logging as log

class ArgumentParser:
    def __init__(self):
        self.title = " __      ___     _            _____       _ _ _   \n \\ \\    / (_)   | |          / ____|     | (_) |  \n  \\ \\  / / _  __| | ___  ___| (___  _ __ | |_| |_ \n   \\ \\/ / | |/ _` |/ _ \\/ _ \\___ \\| '_ \\| | | __|\n    \\  /  | | (_| |  __/ (_) |___) | |_) | | | |_ \n     \\/   |_|\\__,_|\\___|\\___/_____/| .__/|_|_|\\__|\n                                   | |            \n                                   |_|            "
        self.parser = argparse.ArgumentParser(description="This is a simple program were it will split a video file or directory to a list of frames", epilog=f"For more information see my github :) \nhttps://github.com/supergamer66000/VideoSplit")

        if self.getNoArgs():
            print(self.title)
            self.parse()
            
            # Parsers the args
            self.arg = self.parser.parse_args()
        else:
            log.warning("Please use --direcotor or --file for use. --help for help")
            quit()
        
        #if self.arg.help:
        #    print(self.title)
        
    def parse(self):
        # parse all args
        options = self.parser.add_argument_group('Options')
        options.add_argument('--file', type=str, help='selected the file')
        options.add_argument('--dir', '--directory', type=str, help='selected the file director')
        options.add_argument('--build', type=str, help="Builds the video to a .mp4 format")
        options.add_argument('--type', type=str, help="Allows you define what file type. e.g .mp4")
        options.add_argument('--fps', type=int, help="Specifies fps for --build")
        options.add_argument('--rename', type=str, help="export folder name")
        options.add_argument('--export', type=str, help="folder Export Path")
        options.add_argument('--core-count', type=int, help="Specify how many core the programe uses")
        options.add_argument('--date', type=str, help='Allow you to only do file that were created on a spicific date: Year/Month/Day, --time 2024/8/13')
        options.add_argument('--funny', action='store_true', help="funny")
        #options.add_argument('--debug', action='action_True', help="Debug")
    
    
    
    def getNoArgs(self):
        if len(sys.argv) > 1:
            return True
        return False

if __name__ == '__main__':
    print("Why you running this?")