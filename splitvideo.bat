@echo off

if "%1" == "setup" (
    if "%2" == "" (
        python setup.py
    ) else (
        echo Path has been specified: %2
        call %2 setup.py
        if errorlevel 1 (
            echo ERROR: Please ensure this is a valid path
        )
    )
) else (
    .venv\Scripts\python.exe .\python\splitvideo.py %*
    if errorlevel 1 (
        echo ERROR: Please ensure you have run splitvideo.bat setup
    )
)
