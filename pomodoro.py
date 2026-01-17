import time, os, sys
from rich.console import Console
from pyfiglet import Figlet


console = Console
b = Figlet(font="big")
def start():
    total_seconds = 1500
    while total_seconds > 0: 
        mins = total_seconds // 60
        secs = total_seconds % 60
        timer_display = f"\r{mins:02d}:{secs:02d}"
        time.sleep(1)
        print (b.renderText(timer_display, end='', flush=True))
        total_seconds -= 1 
        
if __name__ == ("__main__"):
    start()
        