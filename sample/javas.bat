@echo off  

set curp=%~dp0

set appf=%curp%app.info
set /p getTitle=<%appf%
title=%getTitle% 

set ctype= %1
if "%ctype%"==" " set ctype=start

set command=%curp%javasw.py %curp% %ctype%
python %command%

@pause