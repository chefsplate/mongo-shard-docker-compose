import subprocess
import os
import platform

# --- Create MongoDB cluset - configure it with the scripts

# Run docker compose
docker_compose_command = "docker-compose up -d"

# Sh if linux / bat if windows
if platform.system() == "Linux":
    init_sh_command = "sh init.sh"
elif platform.system() == "Windows":
    init_sh_command = "init.bat"
else:
    print("Unsupported operating system")
    exit(1)

# Fichier courrant
current_folder = os.getcwd()

try:
    # Docker compose
    subprocess.run(docker_compose_command, shell=True, cwd=current_folder, check=True)
    
    # File bat / sh
    subprocess.run(init_sh_command, shell=True, cwd=current_folder, check=True)
    
    print("Commands executed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Command execution failed: {e.returncode}")
except Exception as e:
    print(f"An error occurred: {e}")