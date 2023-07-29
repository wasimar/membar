"""
This code will print a progress bar to the console that shows the current memory usage and the peak memory usage. The progress bar will update every time the `update()` method is called.
"""
from os import getpid
from psutil import Process, virtual_memory

# ANSI escape codes for colors
OKGREEN = '\033[92m'
WARNING = '\033[93m'
DANGER = '\033[91m'
ENDC = '\033[0m'

def bar_string(current: int, total: int, indicator: str = '■', length: int = 30) -> str:
    """
    Return a string representing the indicator bar.
    current: current memory usage
    total: total available memory
    indicator: indicator character
    length: length of the indicator bar
    """
    progress = current / total
    n = int(progress * length)
    if progress < .5:
        Col = OKGREEN
    elif progress < .8:
        Col = WARNING
    else:
        Col = DANGER
    return f"{Col}{indicator * n}{' ' * (length - n)} {progress * 100:.2f}% | {current}/{total}GB{ENDC}"


class MemBar:
    def __init__(self, total: int, total_ram: float = (virtual_memory().total / 10**9).__round__(3)) -> None:
        """
        total (int): The total number of iterations.
        total_ram (float, optional): The total RAM in GB (default: total RAM of the system).
        """
        self.total = total
        self.current = 0
        self.progress = Process(getpid())
        self.peak_ram = 0
        self.total_ram = total_ram
        self.init_ram = (self.progress.memory_info().rss / 10**9).__round__(3)

    def update(self) -> None:
        """
        Update the memory monitor bar.
        """
        self.current += 1
        rss = (self.progress.memory_info().rss / 10**9).__round__(3)
        self.peak_ram = max(self.peak_ram, rss)
        print('\033[K' + f"[Peak] {bar_string(self.peak_ram, self.total_ram)} [Current] {bar_string(rss, self.total_ram)}", end='\r', flush=True)        
        if self.current == self.total:
            print()