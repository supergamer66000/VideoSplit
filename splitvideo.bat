@echo off

:: install function
:install
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
)

:: Check if the .venv exists
if exist .venv\ (
    .venv\Scripts\python.exe .\python\splitvideo.py %*
) else (
    call install
    if errorlevel 1 (
        echo ERROR: Ensure you have ran: splitvideo.bat setup
        exit /b 0
    )
)