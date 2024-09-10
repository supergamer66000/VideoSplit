import logging as log
from videoprocessor import VideoProcessor
import click

def fun(funny):
        import webbrowser
        import time
        import socket
        import sys
        def check_internet_connection():
            remote_server = "www.google.com"
            port = 80
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            try:
                sock.connect((remote_server, port))
                return True
            except socket.error:
                return False
            finally:
                sock.close()
        ascii = "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢶⣾⣷⣾⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠁⠁⠈⠁⠀⠀⠀⠀⠀⢹⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⢸⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⢹⣿⣿⡆⠀⠈⠥⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⢽⠗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣶⣶⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢿⡌⠀⠀⠰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡆⠀⣿⣾⣶⣆⠀⠀⢨⡄⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⣿⡈⠛⢿⣿⣿⡄⠀⢸⢊⣀⠈⣿⣿⣶⣶⣤⣄⣀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠈⠀⠉⠁⠀⠀⠄⠀⠀⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀\n⠀⠀⠀⠀⠀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡄⠲⠤⢤⣤⡄⠀⠀⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧\n⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣉⣀⣐⠒⠒⠠⠰⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠤⠤⠉⣉⣉⢸⣓⡲⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠒⠒⠒⠠⠤⢼⣭⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣉⣙⠛⠒⢸⠶⣦⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿\n⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⠤⠬⢍⣉⣹⣛⣓⣲⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡒⠲⠶⠶⡿⣽⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣍⣙⣛⣏⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏\n⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠦⠤⣬⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀\n⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣙⣟⣿⣷⣷⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆\n⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠙⠃\n⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⠀⠀⠀\n⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀\n⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠛⠛⠁⡇⠟⢿⣿⣿⣿⣿⣿⣿⣿⣧⡀\n GET RICKROLLED NOOB"
        if check_internet_connection():
            webbrowser.open_new('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
            time.sleep(0.2)
            print(ascii)
        else:
            print(ascii)

class Parser:
    def __init__(self) -> None:
        pass
    
    @click.group()
    def cli():
        pass
    
    @cli.command()
    @click.argument('PATH')
    @click.option('--export')
    def file(path, export) -> None:
        VideoProcessor().split_video(path, export)
    
    @cli.command()
    @click.argument('PATH')
    @click.option('--export')
    @click.option('--date')
    @click.option('--core-count/-c')
    def dir(path, export, date, core_count):
        if not core_count:
            core_count = None
        VideoProcessor().split_video_directory(video_dir=path, date=date, output_dir=export, cores=core_count)
    
    @cli.command()
    @click.argument('DIRECTORY')
    #@click.option('--export')
    @click.option('--fps')
    @click.option('--type')
    def build(directory, fps, type):
        if not type:
            type = None
        if not fps:
            fps = None
        VideoProcessor().build_video(image_dir=directory, type=type, fps=fps)
        

if __name__ == '__main__':
    title = """ __      ___     _            _____       _ _ _   \n \\ \\    / (_)   | |          / ____|     | (_) |  \n  \\ \\  / / _  __| | ___  ___| (___  _ __ | |_| |_ \n   \\ \\/ / | |/ _` |/ _ \\/ _ \\___ \\| '_ \\| | | __|\n    \\  /  | | (_| |  __/ (_) |___) | |_) | | | |_ \n     \\/   |_|\\__,_|\\___|\\___/_____/| .__/|_|_|\\__|\n                                   | |            \n                                   |_|            """
    print(title)
    app = Parser()
    Parser().cli()