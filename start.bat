@echo off
set dir_path=%cd%\magic
echo %dir_path%
python tinypng.py -d %dir_path%
pause & exit