import os
from playsound3 import playsound
from pyfiglet import Figlet
from rich.align import Align
from rich.console import Console
from rich.live import Live
from rich.layout import Layout
from rich.text import Text
import time

console = Console()
layout = Layout()
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

isofont = Figlet(font="larry3d")
fontapply = isofont.renderText("pomo-term")
titlebar = Text(fontapply, style="yellow")

#terminal layout.
layout.split_column(
    Layout(name="title", size=10), 
    Layout(name="timer", ratio=1),
    Layout(name="stop", size=5)
)

console.clear()
console.print("\n" * 3)  # top spacing

layout["title"].update(Align.center(titlebar))
layout["stop"].update(Align.center(Text("press ctrl-c to quit", style="dim")))



def main():
    while True:
        start()
        console.clear()
        console.print("\n" * 6)
        playsound(os.path.join(SCRIPT_DIR, "sounds/timerend.mp3"))
        console.print(Align.center(Text("Great job! Work session complete. Press enter to start a break", style="bold cyan")))
        input()

        break_time()
        console.clear()
        console.print("\n" * 6)
        playsound(os.path.join(SCRIPT_DIR, "sounds/timerend.mp3"))
        console.print(Align.center(Text("Break finished. Press enter to go back to work.", style="bold cyan")))
        input()

def start():
    total_seconds = 1500

    with Live(layout, console=console, refresh_per_second=4) as live:
        while total_seconds > 0: 
            mins = total_seconds // 60
            secs = total_seconds % 60

            time.sleep(1)
            layout["timer"].update(Align.center(format_time(mins, secs)))

            total_seconds -= 1 


def break_time():
    total_seconds = 300
    with Live(layout, console=console, refresh_per_second=4) as live:
        while total_seconds > 0: 
            mins = total_seconds // 60
            secs = total_seconds % 60

            time.sleep(1)
            layout["timer"].update(Align.center(format_time(mins, secs)))
            total_seconds -= 1 


def format_time(mins, secs):

    bigfig = Figlet(font="big")
    timer_display = f"{mins:02d}:{secs:02d}"
    ascii_fy = bigfig.renderText(timer_display)
    return Text(ascii_fy, style= "bold cyan")


if __name__ == ("__main__"):
    main()
