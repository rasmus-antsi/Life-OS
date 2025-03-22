import os
import shutil
from rich.console import Console

console = Console()

HOME_DIR = os.path.expanduser("~")
DOWNLOADS_DIR = os.path.join(HOME_DIR, "Downloads")
SORTED_DIR = os.path.join(HOME_DIR, "life-os/organized")

FILE_CATEGORIES = {
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".tiff", ".bmp"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Music": [".mp3", ".wav", ".flac", ".aac"],
    "Archives": [".zip", ".tar", ".gz", ".rar"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java"],
    "3D Files": [".stl", ".obj", ".fbx", ".blend", ".gltf", ".glb"],
    "Others": []
}

# ──────────────────────────── File Organizer ──────────────────────────── #
def organize_files():
    """Sort files from Downloads into categorized folders in life-os."""
    if not os.path.exists(DOWNLOADS_DIR):
        console.print("Downloads folder not found!")
        return
    
    console.print("Organizing files...")

    for file in os.listdir(DOWNLOADS_DIR):
        file_path = os.path.join(DOWNLOADS_DIR, file)
        if os.path.isfile(file_path):
            move_file(file_path)

    console.print("Files organized successfully!")

def move_file(file_path):
    """Move a file to its appropriate category folder."""
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()
    
    category = next((cat for cat, exts in FILE_CATEGORIES.items() if ext in exts), "Others")
    target_folder = os.path.join(SORTED_DIR, category)
    
    os.makedirs(target_folder, exist_ok=True)
    shutil.move(file_path, target_folder)
    console.print(f"Moved: {os.path.basename(file_path)} → {category}")

def reset_organized():
    """Delete all organized files."""
    if os.path.exists(SORTED_DIR):
        shutil.rmtree(SORTED_DIR)
        console.print("All organized files deleted!")
    else:
        console.print("No organized files to delete.")

def list_organized():
    """List organized files."""
    if not os.path.exists(SORTED_DIR):
        console.print("No organized files found.")
        return
    
    console.print("\nOrganized Files:\n")
    for category in os.listdir(SORTED_DIR):
        category_path = os.path.join(SORTED_DIR, category)
        if os.path.isdir(category_path):
            console.print(f"{category}")
            for file in os.listdir(category_path):
                console.print(f"  ➜ {file}")
