@echo off
:: Double-click this file to launch the Key Counter Overlay

cd /d "%~dp0"

:: Check for Python
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python not found. Attempting to install...
    where winget >nul 2>nul
    if %errorlevel% equ 0 (
        winget install Python.Python.3 --accept-source-agreements --accept-package-agreements
    ) else (
        where choco >nul 2>nul
        if %errorlevel% equ 0 (
            choco install python -y
        ) else (
            echo Please install Python from https://www.python.org/downloads/
            pause
            exit /b 1
        )
    )
)

:: Run the counter
python key_counter_overlay.py
if %errorlevel% neq 0 (
    echo.
    echo Error running the counter.
    pause
)
