@echo off
echo to stop this process press ctrl + c then y so that it show ^^Cy then press enter
echo.
echo This process runs a python http server for all calculations the other server has todo.
echo.
echo.

GekkeStart.bat>NUL

python GekkeHTTPServer.py