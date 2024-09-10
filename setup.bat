@echo off

if exist .venv\ (
    echo ERROR: setup.bat has already been ran
) else (
    :: To change the python path change "python" to the python path
    python setup.py
)