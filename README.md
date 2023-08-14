# elden-ring-git-save
I was tired of my Elden Ring game progress totally resetting because of interference and overwriting from Steam Cloud. I first lost a 70-hour completionist run to Steam Cloud and then an hour from a new game, so I decided to do something about it. This tool that will automatically save Elden Ring saves as git commits on your PC. 

## Features
- **Auto-monitoring**: Continuously check if Elden Ring is running.
- **Automated Backups**: Backup your save files every time Elden Ring closes.
- **Version Control**: Initialize and maintain a git repository for save file version control.
- **Restoration**: Easily restore any previous save point using git's commit history.

## Prerequisites
- Python 3.x (installed and added to PATH)
- Conda (for environment management)
- Git (installed and added to PATH)

## Installation

1. Clone the repository:

Open Command Prompt or PowerShell and run:
```
git clone https://github.com/your-username/elden-ring-git-save.git

```

2. Navigate to the cloned directory:

```
cd elden-ring-git-save
```

3. Set up a Conda environment:

```
conda env create -f environment.yml
```

4. Activate the Conda environment:

```
conda activate your_environment_name
```

5. Update the config.yml file:

Open config.yml in your preferred text editor and update the paths for your save files and target git repository.

## Usage

1. Run the monitoring script:

```
python monitor.py
```

This script will continuously check if Elden Ring is running and will trigger the backup script when Elden Ring closes.

2. To manually backup your save:

```
python main.py
```

You can also add `monitor.py` to your Windows Task Scheduler to start anytime you log on.