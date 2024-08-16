import argparse
import sys
import logging as log
import os


class ArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="This is a simple program were it will split a video file or directory to a list of frames", epilog=f"\nFor more information see my github :) \nhttps://github.com/supergamer66000/VideoSplit")

        if self.getNoArgs():
            self.parse()
        else:
            log.warning("Please use --direcotor or --file for use. --help for help")
            quit()
        
    def parse(self):
        # parse all args
        #parser.add_argument('source', type=str, help='rick_roll.mp4')
        options = self.parser.add_argument_group('Options')
        options.add_argument('--file', type=str, help='selected the file')
        options.add_argument('--dir', '--directory', type=str, help='selected the file director')
        options.add_argument('--folder', type=str, help="export folder name")
        options.add_argument('--export', type=str, help="folder Export Path")
        options.add_argument('--core-count', type=int, help="Specify how many core the programe uses")
        options.add_argument('--date', type=str, help='Allow you to only do file that were created on a spicific date: [Year, Month, Day], --time 2024/8/13')
        options.add_argument('--funny', action='store_true', help="funny")
        #options.add_argument('--debug', action='action_True', help="Debug")
        
        # Parsers the args
        self.arg = self.parser.parse_args()
    
    def getNoArgs(self):
        if len(sys.argv) > 1:
            return True
        return False