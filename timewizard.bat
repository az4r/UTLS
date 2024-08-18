@echo off

if not "%1" == "min" start /MIN cmd /c %0 min & exit/b >nul 2>&1

:a
date 24-12-2023
time 06:30:00
ping 1.1.1.1 -n 2 -w 400 >nul
goto a