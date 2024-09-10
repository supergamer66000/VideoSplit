@echo off

:: Check if the .venv exists
if exist .venv\ (
    .venv\Scripts\python.exe .\python\splitvideo.py %*
) else (
    echo ERROR: Ensure you have ran setup.bat
)