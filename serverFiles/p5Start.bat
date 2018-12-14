@echo off
echo to stop this process press ctrl + c then y so that it show ^^Cy then press enter
echo.
echo This process runs an http server for the p5 ui in the browser.
echo.
echo.

cd p5Files/

python -m http.server

