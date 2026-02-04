@echo off
:: Double-click this file to launch the Key Counter Overlay (hidden console)

cd /d "%~dp0"

:: Check for Python
where python >nul 2>nul
if %errorlevel% neq 0 (
    where pythonw >nul 2>nul
    if %errorlevel% neq 0 (
        echo Python not found. Please install from https://www.python.org/downloads/
        pause
        exit /b 1
    )
)

:: Run with pythonw (no console) or start minimized
where pythonw >nul 2>nul
if %errorlevel% equ 0 (
    start "" pythonw key_counter_overlay.py
) else (
    start "" /min python key_counter_overlay.py
)
