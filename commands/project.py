import os
import shutil
from rich.console import Console

console = Console()

PROJECTS_DIR = os.path.expanduser("~/life-os/projects")

# ──────────────────────────── Project Management ──────────────────────────── #
def start_project(name):
    """Create a new project: life-os start-project <name> (type will be asked)"""
    console.print(f"Select project type for {name}:")
    console.print("  1. Hardware")
    console.print("  2. Software")
    console.print("  3. Custom")
    choice = input("Enter choice (1/2/3): ").strip()
    
    project_types = {"1": "hardware", "2": "software", "3": "custom"}
    project_type = project_types.get(choice, "custom")
    project_path = os.path.join(PROJECTS_DIR, project_type, name)

    if os.path.exists(project_path):
        console.print("Project already exists.")
        return
    
    os.makedirs(project_path, exist_ok=True)
    
    # Copy from templates
    template_path = os.path.join(os.path.dirname(__file__), "..", "templates", project_type)
    if os.path.exists(template_path):
        shutil.copytree(template_path, project_path, dirs_exist_ok=True)

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
    """Find a project by name"""
    for root, dirs, _ in os.walk(PROJECTS_DIR):
        if name in dirs:
            return os.path.join(root, name)
    return None