@echo off
chcp 65001 > nul
echo Starting Stock Breakout Screener...
python "%~dp0start_server.py"
pause
