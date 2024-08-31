@echo off
setlocal enabledelayedexpansion

set /p process_description="Podaj nazwe procesu: "

set found=0
set counter=1

for /f "tokens=*" %%A in ('powershell -command "Get-Process | Where-Object {$_.Name -like '*%process_description%*'} | ForEach-Object {$_.'Id'}"') do (
    set pid!counter!=%%A
    echo PID procesu o nazwie "%process_description%" to: %%A
    set /a counter+=1
    set found=1
)

if !found! equ 0 (
    echo Nie znaleziono procesu o podanej nazwie.
) else (
    echo Znaleziono !counter!-1 procesow.
)

if !found! equ 1 (
    echo Pierwszy PID procesu to: !pid1!
    echo Drugi PID procesu to: !pid2!
)

endlocal
pause