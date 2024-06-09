#!/usr/bin/env python3

import os
import sys
import subprocess
import shutil

def install_packages():
    requirements_file = 'requirements.txt'
    if os.path.exists(requirements_file):
        print("Installing required packages from requirements.txt...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', requirements_file, '--break-system-packages'])
    else:
        print("requirements.txt not found. Please ensure it is in the same directory as this script.")

def create_config(bot_token, chat_id):
    config_dir = os.path.expanduser('~/.config/teletify')
    config_file = os.path.join(config_dir, 'config.ini')
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)
    print("Creating configuration file...")
    with open(config_file, 'w') as file:
        file.write("[telegram]\n")
        file.write(f"bot_api_key = {bot_token}\n")
        file.write(f"default_chat_id = {chat_id}\n")
    print(f"Configuration file '{config_file}' created.")

def copy_script():
    script_name = 'main.py'
    destination = '/usr/local/bin/teletify'
    if os.path.exists(script_name):
        shutil.copy(script_name, destination)
        os.chmod(destination, 0o755)
        print(f"Script '{script_name}' copied to '/usr/bin/teletify'")
    else:
        print(f"Script '{script_name}' not found in the current directory.")

if __name__ == '__main__':
    bot_token = input("Enter your bot token: ")
    chat_id = input("Enter your default chat ID: ")

    install_packages()
    create_config(bot_token, chat_id)
    copy_script()
    print("Setup completed successfully.")