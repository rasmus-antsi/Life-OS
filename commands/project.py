import os
import shutil
from rich.console import Console

from settings import *

console = Console()

# ──────────────────────────── Project Management ──────────────────────────── #
def get_templates():
    """Return default templates with folders and files."""
    return {
        "hardware": {"folders": ["3D Files", "KiCAD Files", "Code"], "files": ["README.md"]},
        "3D Design": {"folders": ["Final Version", "Test Files"], "files": ["README.md"]},
        "software": {"folders": ["src", "tests"], "files": ["README.md", "src/main.py"]},
        "custom": {"folders": [], "files": ["README.md"]}
    }

def start_project(name):
    """Create a new project."""
    console.print("Select project type:")
    choices = {"1": "hardware", "2": "3D Design", "3": "software", "4": "custom"}
    for k, v in choices.items():
        console.print(f"  {k}. {v}")
    project_type = choices.get(input("Enter choice (1/2/3/4): ").strip(), "custom")
    
    project_path = os.path.join(PROJECTS_DIR, project_type, name)
    if os.path.exists(project_path):
        console.print("Project already exists.")
        return
    
    os.makedirs(project_path, exist_ok=True)
    templates = get_templates().get(project_type, {"folders": [], "files": []})
    
    for folder in templates["folders"]:
        os.makedirs(os.path.join(project_path, folder), exist_ok=True)
    
    for filename in templates["files"]:
        file_path = os.path.join(project_path, filename)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as f:
            if filename.endswith("README.md"):
                f.write(f"# {project_type.capitalize()} Project\n\nDescribe your {project_type} project here.")
            elif filename.endswith(".py"):
                f.write("# Main script\nprint('Hello, World!')")
    
    console.print(f"Project '{name}' created in {project_path}")

def open_project(name):
    """Open an existing project: life-os open-project <name>"""
    project_path = find_project(name)
    if project_path:
        console.print(f"Opening project: {project_path}")
        os.system(f"open {project_path}")
    else:
        console.print("Project not found.")

def delete_project(name):
    """Delete an existing project: life-os delete-project <name>"""
    project_path = find_project(name)
    if project_path:
        shutil.rmtree(project_path)
        console.print(f"Project '{name}' deleted.")
    else:
        console.print("Project not found.")

def list_projects():
    console.print("\nListing all projects...\n")

    if not os.path.exists(PROJECTS_DIR):
        console.print("No projects found.")
        return

    categories = [f for f in os.listdir(PROJECTS_DIR) if os.path.isdir(os.path.join(PROJECTS_DIR, f))]

    projects = []
    for category in categories:
        category_path = os.path.join(PROJECTS_DIR, category)
        projects_in_category = [p for p in os.listdir(category_path) if os.path.isdir(os.path.join(category_path, p))]
        projects.extend([(p, category) for p in projects_in_category])

    if not projects:
        console.print("No projects found.")
    else:
        for project, category in projects:
            console.print(f"  ➜ {project} ({PROJECTS_DIR}/{category}/{project})")

def archive_project(name):
    """Move a project to the archive: life-os archive-project <name>"""
    project_path = find_project(name)
    archive_path = os.path.join(PROJECTS_DIR, "archive", name)
    if project_path:
        shutil.move(project_path, archive_path)
        console.print(f"Project '{name}' archived.")
    else:
        console.print("Project not found.")

def zip_project(name):
    """Compress a project into a .zip file: life-os zip-project <name>"""
    project_path = find_project(name)
    zip_path = os.path.join(PROJECTS_DIR, f"{name}.zip")
    if project_path:
        shutil.make_archive(zip_path.replace(".zip", ""), 'zip', project_path)
        console.print(f"📦 Project '{name}' compressed to {zip_path}")
    else:
        console.print("Project not found.")

def find_project(name):
    """Find a project by name."""
    for root, dirs, _ in os.walk(PROJECTS_DIR):
        if name in dirs:
            return os.path.join(root, name)
    return None