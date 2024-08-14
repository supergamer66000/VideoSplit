import argparse
import sys

class ArgumentParser:
    
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        
        if self.getNoArgs():
            self.parse()
        else:
            print("please use --direcotor or --file for use. --help for help")
            quit()
        
    def parse(self):
        # parse all args
        #parser.add_argument('source', type=str, help='rick_roll.mp4')
        options = self.parser.add_argument_group('Options')
        options.add_argument('--file', type=str, help='selected the file')
        options.add_argument('--directory', type=str, help='selected the file director')
        options.add_argument('--folder', type=str, help="export folder name")
        options.add_argument('--export', type=str, help="folder Export Path")
        
        # Parsers the args
        self.arg = self.parser.parse_args()
    
    def getFile(self):
        return self.arg.file
    
    def getDirector(self):
        return self.arg
    
    def getExport(self):
        return self.arg.export
    
    def getNoArgs(self):
        if len(sys.argv) > 1:
            return True
        return False