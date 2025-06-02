@echo off
title AstraBot - Downloader
color 0a
cls

:: Check for python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python not found! Please install it:
    echo https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe
    echo And set "Add Python to PATH" to true!
    pause
    exit
)

:: Install packages
echo [~] Installing packages
pip install --upgrade pyautogui keyboard pillow pystray mysql-connector-python

:: Starte das Skript
echo [~] Starting AstraBot...
python "%~dp0astra.py"
echo [~] If it doesnt start automatically please start the .py yourself!
pause
