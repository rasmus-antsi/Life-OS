#!/usr/bin/env python3
from rich.console import Console
from rich.panel import Panel
import sys
from commands import run_command, setup_symlink, show_help

console = Console(color_system=None)  # Minimalist output

HEADER = """
██      ██ ███████ ███████      ██████  ███████ 
██      ██ ██      ██          ██    ██ ██      
██      ██ █████   █████       ██    ██ ███████ 
██      ██ ██      ██          ██    ██      ██ 
███████ ██ ██      ███████      ██████  ███████ 
"""

SEPARATOR = "----------------------------------"

if __name__ == "__main__":
    setup_symlink()
    if len(sys.argv) < 2:
        console.print(Panel(HEADER, title="Life OS", expand=False))
        show_help()
    else:
        run_command(sys.argv[1], *sys.argv[2:])