import platform
import subprocess
import sys

class Setup:
    def __init__(self):
        if self.check_python_version():
            self.setup()
            
    def check_python_version(self):
        """Checks python version"""
        version = [int(i) for i in platform.python_version().split('.')]
        if version[1] >= 11:
            return True
        print("Your python version is not above 3.11")
        return False
        
    def setup(self):
        """Setup function"""
        # Creates the venv
        self.create_venv()
        
        # Installes all the packages
        self.install_package("opencv-python")
        self.install_package("moviepy")
        
        # Runs the help Command
        self.print_title()
        
        print("For help on using split video please type splitvideo.bat --help")
        
    def create_venv(self):
        subprocess.check_call([sys.executable, "-m", "venv", ".venv"])
    
    def install_package(self, package_name):
        subprocess.check_call([".venv/Scripts/python.exe", "-m", "pip", "install", package_name])
    
    def print_title(self):
        title = " __      ___     _            _____       _ _ _   \n \\ \\    / (_)   | |          / ____|     | (_) |  \n  \\ \\  / / _  __| | ___  ___| (___  _ __ | |_| |_ \n   \\ \\/ / | |/ _` |/ _ \\/ _ \\___ \\| '_ \\| | | __|\n    \\  /  | | (_| |  __/ (_) |___) | |_) | | | |_ \n     \\/   |_|\\__,_|\\___|\\___/_____/| .__/|_|_|\\__|\n                                   | |            \n                                   |_|            "
        print(title)
        
if __name__ == "__main__":
    try:
        Setup()
    except subprocess.CalledProcessError as e:
        print(f"There was an error perhaps its already been setup?")