import time, os, sys

def start():
    mins = total_seconds // 60
    secs = total_seconds % 60
    total_seconds = 1500
    timer_display = f"{mins:02d}:{secs:02d}"

    while total_seconds > 0: 
        time.sleep(1)
        timer_display -= 1 
