@echo on

chdir /D "C:\Windows"
start "" notepad.exe
chdir /D "C:\runasdate-x64"

setlocal enabledelayedexpansion
set process_description=notepad
set found=0
set counter=1
for /f "tokens=*" %%A in ('powershell -command "Get-Process | Where-Object {$_.Name -like '*%process_description%*'} | ForEach-Object {$_.'Id'}"') do (
    set pid!counter!=%%A
    echo PID procesu o nazwie "%process_description%" to: %%A
    RunAsDate.exe 24\12\2023 06:15:00 Attach:%%A
    set /a counter+=1
    set found=1
)
if !found! equ 0 (
    echo Nie znaleziono procesu o podanej nazwie.
) else (
    set /a counter-=1
    echo Znaleziono !counter!.
)
endlocal

setlocal enabledelayedexpansion
set process_description=svchost
set found=0
set counter=1
for /f "tokens=*" %%A in ('powershell -command "Get-Process | Where-Object {$_.Name -like '*%process_description%*'} | ForEach-Object {$_.'Id'}"') do (
    set pid!counter!=%%A
    echo PID procesu o nazwie "%process_description%" to: %%A
    RunAsDate.exe 24\12\2023 06:15:00 Attach:%%A
    set /a counter+=1
    set found=1
)
if !found! equ 0 (
    echo Nie znaleziono procesu o podanej nazwie.
) else (
    set /a counter-=1
    echo Znaleziono !counter!.
)
endlocal

pause