import subprocess
import time

class EnvironmentSetup:
    def __init__(self):
        self.commands = [
            "sudo apt update",
            "sudo apt install -y npm",
            "npm install -g pm2",
            "git clone https://github.com/commune-ai/commune.git",
            "sudo apt update && sudo apt upgrade -y",
            "sudo apt install -y software-properties-common",
            "sudo add-apt-repository -y ppa:deadsnakes/ppa",
            "sudo apt install -y python3.10",
            "sudo apt install -y python3-pip",  # Install pip for Python 3
            "cd commune && sudo apt-get install -y python-click",
            "pip install -U numpy",
            "pip install --upgrade pip",
            "pip install protobuf==3.20",
            "pip install streamlit grpcio-tools",
            "pip install -e ./",
            "cd scripts && ./install_rust_env.sh && cd ..",
            "curl -SL https://github.com/docker/compose/releases/download/v2.20.3/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose",
            "sudo chmod +x /usr/local/bin/docker-compose",
            "sudo apt install -y docker.io",  # Install Docker
            "cd /commune && rm -rf ./subspace && make pull",
            "pip install -U click",
            "sudo systemctl start docker",    # Start Docker service
            "sudo systemctl enable docker",   # Enable Docker service on boot
            "sudo apt install -y sshpass",    # Install sshpass
            "sudo apt install -y ansible",    # Install Ansible
            "sudo apt install -y nvidia-driver-525",  # Install Nvidia Driver 525
            "wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin",
            "sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600",
            "wget https://developer.download.nvidia.com/compute/cuda/12.0.0/local_installers/cuda-repo-ubuntu2204-12-0-local_12.0.0-525.60.13-1_amd64.deb",
            "sudo dpkg -i cuda-repo-ubuntu2204-12-0-local_12.0.0-525.60.13-1_amd64.deb",
            "sudo cp /var/cuda-repo-ubuntu2204-12-0-local/cuda-*-keyring.gpg /usr/share/keyrings/",
            "sudo apt-get update",
            "sudo apt-get -y install cuda"
        ]

    def run_commands_with_delay(self, delay_seconds=5):
        for command in self.commands:
            try:
                subprocess.run(command, shell=True, check=True)
                print(f"Command '{command}' executed successfully.")
            except subprocess.CalledProcessError as e:
                print(f"Error running command: {e}")
            time.sleep(delay_seconds)

if __name__ == "__main__":
    # Create an instance of EnvironmentSetup
    env_setup = EnvironmentSetup()

    # Run the commands with a 5-second delay between each action
    env_setup.run_commands_with_delay(5)

