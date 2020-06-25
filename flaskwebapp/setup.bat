echo off
set HOST=0.0.0.0
set FLASK_APP=run.py
echo Environment Variable for flask application is %FLASK_APP%
echo App is running on host  %HOST%
flask run --host=%HOST%
echo on