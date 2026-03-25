@echo off
setlocal enabledelayedexpansion

title CipherCore Suite Build System

cd /d %~dp0

set APP_NAME=CipherCore Suite
set APP_EXE=CipherCoreSuite
set APP_VERSION=1.0.0.0
set APP_AUTHOR=Thorsten Bylicki
set APP_COMPANY=Thorsten Bylicki
set APP_COPYRIGHT=Copyright (c) Thorsten Bylicki. All rights reserved.
set APP_ICON=assets\ciphercore.ico
set VERSION_FILE=version_info.txt
set MAIN_FILE=run.py

echo.
echo ==========================================
echo   %APP_NAME% Build System
echo   Version: %APP_VERSION%
echo   Author: %APP_AUTHOR%
echo ==========================================
echo.

where python >nul 2>nul
if errorlevel 1 (
    echo [FEHLER] Python wurde nicht gefunden.
    echo Bitte stelle sicher, dass Python installiert und im PATH verfuegbar ist.
    echo.
    pause
    exit /b 1
)

if not exist requirements.txt (
    echo [FEHLER] Die Datei requirements.txt wurde nicht gefunden.
    echo.
    pause
    exit /b 1
)

if not exist "%VERSION_FILE%" (
    echo [FEHLER] Die Datei %VERSION_FILE% wurde nicht gefunden.
    echo.
    pause
    exit /b 1
)

if not exist "%MAIN_FILE%" (
    echo [FEHLER] Die Datei %MAIN_FILE% wurde nicht gefunden.
    echo.
    pause
    exit /b 1
)

if not exist "%APP_ICON%" (
    echo [WARNUNG] Das Icon %APP_ICON% wurde nicht gefunden.
    echo Der Build wird ohne eigenes Icon fortgesetzt.
    set USE_ICON=
) else (
    set USE_ICON=--icon "%APP_ICON%"
)

echo [INFO] Alte Build-Dateien werden entfernt...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist "%APP_EXE%.spec" del /f /q "%APP_EXE%.spec"

echo.
echo [INFO] Python Version:
python --version

echo.
echo [INFO] Abhaengigkeiten werden installiert bzw. aktualisiert...
python -m pip install --upgrade pip
if errorlevel 1 (
    echo [FEHLER] Pip konnte nicht aktualisiert werden.
    echo.
    pause
    exit /b 1
)

python -m pip install -r requirements.txt
if errorlevel 1 (
    echo [FEHLER] Die requirements konnten nicht installiert werden.
    echo.
    pause
    exit /b 1
)

python -m pip install pyinstaller
if errorlevel 1 (
    echo [FEHLER] PyInstaller konnte nicht installiert werden.
    echo.
    pause
    exit /b 1
)

echo.
echo [INFO] Build wird gestartet...
echo.

python -m PyInstaller ^
  --noconfirm ^
  --clean ^
  --windowed ^
  --onefile ^
  --name "%APP_EXE%" ^
  %USE_ICON% ^
  --version-file "%VERSION_FILE%" ^
  --exclude-module torch ^
  --exclude-module functorch ^
  --exclude-module tensorflow ^
  --exclude-module matplotlib ^
  --exclude-module pandas ^
  --exclude-module pyarrow ^
  --exclude-module sqlalchemy ^
  "%MAIN_FILE%"

if errorlevel 1 (
    echo.
    echo [FEHLER] Der Build ist fehlgeschlagen.
    echo Bitte pruefe die Ausgabe auf konkrete Fehlermeldungen.
    echo.
    pause
    exit /b 1
)

echo.
echo ==========================================
echo   BUILD ERFOLGREICH ABGESCHLOSSEN
echo ==========================================
echo.
echo Die EXE sollte sich nun hier befinden:
echo dist\%APP_EXE%.exe
echo.
echo Eingebettete Metadaten:
echo • Produktname
echo • Dateibeschreibung
echo • Copyright
echo • Version
echo • Deutsch und Englisch aus version_info.txt
echo.

pause
exit /b 0
