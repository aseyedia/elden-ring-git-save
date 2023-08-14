import os
import shutil
import datetime
import yaml


def load_config():
    # Get the directory of the currently executing script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the config file
    config_path = os.path.join(script_dir, "config.yml")

    print(f"Loading config from: {config_path}...")  # This will help in debugging

    with open(config_path, "r") as file:
        return yaml.safe_load(file)


def initialize_git_repo(repo_path):
    print(f"Checking if repository exists at {repo_path}...")
    if not os.path.exists(repo_path):
        print(f"Repository not found. Creating directory at {repo_path}...")
        os.makedirs(repo_path)

    git_dir = os.path.join(repo_path, ".git")
    if not os.path.exists(git_dir):
        print("Initializing git repository...")
        os.chdir(repo_path)
        os.system("git init")


def backup_save_file(config):
    save_file_path = config["save_file_path"]
    repo_path = config["repo_path"]

    initialize_git_repo(repo_path)

    backup_name = "savefile_{}.sav".format(datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
    print(f"Copying save file to {backup_name}...")
    shutil.copy2(save_file_path, os.path.join(repo_path, backup_name))

    print("Committing to git repository...")
    os.chdir(repo_path)
    os.system("git add .")
    os.system(f"git commit -m 'Backup: {backup_name}'")


if __name__ == "__main__":
    print("Backup script started.")
    config = load_config()
    backup_save_file(config)
    print("Backup completed.")
