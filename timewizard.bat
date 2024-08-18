@if (@CodeSection == @Batch) @then
@echo off
setlocal

if not "%1" == "min" start /MIN cmd /c %0 min & exit/b >nul 2>&1

date 24-12-2023

:a
time 06:60:00
cscript /nologo /e:JScript "%~f0" 250
goto a

@end
WSH.Sleep(WSH.Arguments(0));