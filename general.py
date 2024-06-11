import os
import uuid
import subprocess
import platform

def GenerateUUID():
    return str(uuid.uuid4())

# Get the system platform
def get_system_platform():
    return platform.system()

# Get the Python version
def get_python_version():
    return platform.python_version()

# Get the current working directory
def get_current_directory():
    return os.getcwd()

# Execute a shell command
def execute_shell_command(command: str):
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Shell command executed: {command}.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing shell command: {e}")