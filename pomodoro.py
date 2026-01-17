import time, os, sys
from rich.live import Live
from pyfiglet import Figlet


def start():
    total_seconds = 1500

    with Live(refresh_per_second=4) as live:
        while total_seconds > 0: 
            mins = total_seconds // 60
            secs = total_seconds % 60

            time.sleep(1)
            live.update(format_time(mins, secs))

            total_seconds -= 1 


def format_time(mins, secs):

    bigfig = Figlet(font="big")
    timer_display = f"{mins:02d}:{secs:02d}"
    return bigfig.renderText(timer_display)



if __name__ == ("__main__"):
    start()
        