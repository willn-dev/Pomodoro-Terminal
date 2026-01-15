import time, os, sys

def start():
    total_seconds = 1500
    while total_seconds > 0: 
        mins = total_seconds // 60
        secs = total_seconds % 60
        timer_display = f"{mins:02d}:{secs:02d}\n"
        time.sleep(1)
        print(timer_display)
        total_seconds -= 1 

if __name__ == ("__main__"):
    start()
        