#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stock Breakout Screener — Local HTTP Server
Run this file to open the dashboard with auto-loading from data/
"""
import http.server, socketserver, os, sys, webbrowser, threading, time

PORT = 8765

# Change to the directory of this script (handles Hebrew/Unicode paths)
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # Silence request logs

def open_browser():
    time.sleep(0.8)
    webbrowser.open(f'http://127.0.0.1:{PORT}/')

threading.Thread(target=open_browser, daemon=True).start()

print("=" * 50)
print("  Stock Breakout Screener")
print(f"  http://127.0.0.1:{PORT}/")
print("  Press Ctrl+C to stop.")
print("=" * 50)

try:
    with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")
except OSError:
    # Port already in use — just open the browser
    print(f"Port {PORT} already in use. Opening browser...")
    webbrowser.open(f'http://127.0.0.1:{PORT}/')
