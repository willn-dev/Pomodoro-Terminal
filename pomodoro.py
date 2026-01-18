import time
from pyfiglet import Figlet
from rich.align import Align
from rich.console import Console
from rich.live import Live
from rich.layout import Layout
from rich.text import Text

console = Console()
layout = Layout()


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

def start():
    total_seconds = 1500

    with Live(layout, console=console, refresh_per_second=4) as live:
        while total_seconds > 0: 
            mins = total_seconds // 60
            secs = total_seconds % 60

            time.sleep(1)
            layout["timer"].update(Align.center(format_time(mins, secs)))

            total_seconds -= 1 
        if total_seconds = 0:


def format_time(mins, secs):

    bigfig = Figlet(font="big")
    timer_display = f"{mins:02d}:{secs:02d}"
    ascii_fy = bigfig.renderText(timer_display)
    return Text(ascii_fy, style= "bold cyan")


if __name__ == ("__main__"):
    start()
