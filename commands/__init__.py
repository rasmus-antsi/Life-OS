import os
from rich.console import Console
from commands.project import *
from commands.file_organizer import *

console = Console()

COMMAND_FUNCTIONS = {
    # Project Management
    "start-project": start_project,
    "open-project": open_project,
    "delete-project": delete_project,
    "list-projects": list_projects,
    "archive-project": archive_project,
    "zip-project": zip_project,

    # File Management
    "organize-files": organize_files,
    "list-organized": list_organized,
    "reset-organized": reset_organized,

    # General
    "help": lambda: show_help(),
}

def setup_symlink():
    """Set up symlink to run 'life-os' from anywhere"""
    bin_path = os.path.expanduser("/usr/local/bin/life-os")
    script_path = os.path.abspath(__file__)
    if not os.path.exists(bin_path):
        os.symlink(script_path, bin_path)
        console.print("Life OS installed. Run 'life-os [command]'.")

def show_help():
    """Show available commands, grouped into sub-menus with proper indentation."""
    console.print("\n[bold underline]Life OS - Available Commands[/bold underline]\n")

    categories = {
        "Project Management": {
            "start-project <name>": "Create a new project (type will be asked)",
            "open-project <name>": "Open an existing project",
            "delete-project <name>": "Delete an existing project",
            "list-projects": "List all projects",
            "archive-project <name>": "Move a project to the archive",
            "zip-project <name>": "Compress a project into a .zip file",
        },
        "File Management": {
            "organize-files": "Sort and organize files from Downloads",
            "list-organized": "List organized files",
            "reset-organized": "Delete all organized files",
        },
        "General": {
            "help": "Show this help menu",
        }
    }

    def print_category(name, commands, indent=0):
        """Recursive function to print categories and subcategories properly formatted."""
        prefix = "  " * indent  # Indentation for subcategories
        console.print(f"\n{prefix}[bold cyan]{name}[/bold cyan]")
        
        for cmd, desc in commands.items():
            if isinstance(desc, dict):  # If it's a sub-menu, recurse
                print_category(cmd, desc, indent + 1)
            else:
                console.print(f"{prefix}  ➜ [bold white]{cmd.ljust(25)}[/bold white] - {desc}")

    # Print main categories and their subcategories
    for category, commands in categories.items():
        print_category(category, commands)

    console.print("\n")

def run_command(command, *args):
    func = COMMAND_FUNCTIONS.get(command)
    if func:
        func(*args)
    else:
        console.print("Unknown command. Try 'life-os help'.")
