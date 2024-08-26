@echo off

if "%1" == "setup" (
    if "%2"=="" (
        python setup.py
    ) else (
        %2 setup.py
    )
    goto :eof
)

%@try%
.venv\Scripts\python.exe .\python\splitvideo.py %*
%@EndTry%
:@Catch
echo ERROR: Please ensure you have ran splitvideo.bat setup
:@EndCatch