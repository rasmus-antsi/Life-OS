# Life OS

A command-line productivity tool for managing projects and organizing files. Life OS provides a simple interface for creating, managing, and organizing your digital workspace.

## Features

### Project Management
- **Create Projects**: Start new projects with predefined templates (hardware, 3D design, software, or custom)
- **Open Projects**: Quickly open existing projects in your file manager
- **List Projects**: View all your projects organized by category
- **Delete Projects**: Remove projects you no longer need
- **Archive Projects**: Move completed projects to an archive folder
- **Zip Projects**: Compress projects into .zip files for backup or sharing

### File Organization
- **Organize Downloads**: Automatically sort files from your Downloads folder into categorized folders
- **Smart Categories**: Files are organized by type (Documents, Images, Videos, Music, Archives, Code, 3D Files, etc.)
- **List Organized Files**: View all organized files by category
- **Reset Organization**: Clear all organized files if needed

## Installation

### Prerequisites
- Python 3.6 or higher
- macOS (the tool is designed for macOS file paths)

### Setup Instructions

1. **Clone or download this repository**:
   ```bash
   git clone <repository-url>
   cd Life-OS
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Make the script executable**:
   ```bash
   chmod +x main.py
   ```

4. **Run the setup** (this will create a symlink for terminal access):
   ```bash
   python main.py
   ```

   The first time you run this, it will automatically create a symlink at `/usr/local/bin/life-os` so you can use the command from anywhere in your terminal.

5. **Verify installation**:
   ```bash
   life-os help
   ```

## Usage

Once installed, you can use `life-os` from anywhere in your terminal:

### Project Management Commands
```bash
# Create a new project
life-os start-project "My New Project"

# Open an existing project
life-os open-project "My New Project"

# List all projects
life-os list-projects

# Delete a project
life-os delete-project "My New Project"

# Archive a project
life-os archive-project "My New Project"

# Compress a project to .zip
life-os zip-project "My New Project"
```

### File Organization Commands
```bash
# Organize files from Downloads folder
life-os organize-files

# List all organized files
life-os list-organized

# Reset organized files (delete all)
life-os reset-organized
```

### General Commands
```bash
# Show help menu
life-os help

# Show the Life OS banner
life-os
```

## Directory Structure

Life OS creates the following directory structure in your home folder:

```
~/life-os/
├── projects/           # All your projects organized by type
│   ├── hardware/      # Hardware projects
│   ├── 3D Design/     # 3D design projects
│   ├── software/      # Software projects
│   ├── custom/        # Custom projects
│   └── archive/       # Archived projects
└── organized/         # Organized files from Downloads
    ├── Documents/     # PDFs, Word docs, etc.
    ├── Images/        # Photos, graphics, etc.
    ├── Videos/        # Video files
    ├── Music/         # Audio files
    ├── Archives/      # ZIP, TAR files
    ├── Code/          # Source code files
    ├── 3D Files/      # 3D model files
    └── Others/        # Unrecognized file types
```

## Project Templates

When creating a new project, you can choose from these templates:

- **Hardware**: Creates folders for 3D Files, KiCAD Files, and Code
- **3D Design**: Creates folders for Final Version and Test Files
- **Software**: Creates src and tests folders with a basic main.py file
- **Custom**: Creates only a README.md file

## Configuration

The tool uses the following default paths (defined in `settings.py`):
- Projects: `~/life-os/projects/`
- Organized files: `~/life-os/organized/`
- Downloads source: `~/Downloads/`

You can modify these paths by editing the `settings.py` file.

## Troubleshooting

### Permission Issues
If you get permission errors when creating the symlink, you may need to run:
```bash
sudo python main.py
```

### Command Not Found
If `life-os` command is not found after installation:
1. Check if `/usr/local/bin` is in your PATH
2. Try running: `export PATH="/usr/local/bin:$PATH"`
3. Add the above line to your shell profile (`.zshrc`, `.bash_profile`, etc.)

### File Organization Issues
- Make sure your Downloads folder exists at `~/Downloads/`
- Check that you have write permissions to the `~/life-os/` directory

## Requirements

- Python 3.6+
- Rich (for beautiful terminal output)
- Standard Python libraries (os, shutil, sys)

## License

This project is open source. Feel free to modify and distribute according to your needs.