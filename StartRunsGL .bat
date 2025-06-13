@ECHO OFF

START C:\LDPlayer\LDPlayer9\dnplayer.exe index=0

cd "C\....\AnotherEdenScripts"

start.py

timeout /t 30
shutdown /s /t 120
