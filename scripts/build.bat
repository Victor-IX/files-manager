for %%I in (.) do set CurrentDir=%%~nxI
if %CurrentDir%==scripts cd ..

if exist __pycache__ rd /S /Q __pycache__
if exist build rd /S /Q build
if exist "dist/release" rd /S /Q "dist/release"

python -OO -m PyInstaller ^
--clean ^
--noupx ^
--onefile ^
--name="Star-Files" ^
--distpath="./dist/release" ^
source\main.py