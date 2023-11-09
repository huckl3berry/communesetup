import subprocess

class EnvironmentSetup:
    def __init__(self):
        self.commands = [
            "sudo apt update",
            "sudo apt upgrade -y",
            "sudo apt install python3-pip -y",
            "sudo apt install nodejs npm -y",
            "sudo apt install build-essential -y",
            "sudo npm install pm2 -g",
            "git clone https://github.com/commune-ai/commune.git",
            "cd commune",
            "pip install -e ./",
            "sudo apt install docker.io -y",  # Install Docker
            "sudo systemctl start docker",    # Start Docker service
            "sudo systemctl enable docker",   # Enable Docker service on boot
            "sudo apt install sshpass -y",    # Install sshpass
            "sudo apt install ansible -y",    # Install Ansible
            "sudo apt install nvidia-driver-525 -y",  # Install Nvidia Driver 525
            "wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin",
            "sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600",
            "wget https://developer.download.nvidia.com/compute/cuda/12.0.0/local_installers/cuda-repo-ubuntu2204-12-0-local_12.0.0-525.60.13-1_amd64.deb",
            "sudo dpkg -i cuda-repo-ubuntu2204-12-0-local_12.0.0-525.60.13-1_amd64.deb",
            "sudo cp /var/cuda-repo-ubuntu2204-12-0-local/cuda-*-keyring.gpg /usr/share/keyrings/",
            "sudo apt-get update",
            "sudo apt-get -y install cuda"
        ]

    def setup_environment(self):
        for command in self.commands:
            try:
                subprocess.run(command, shell=True, check=True)
                print(f"Command '{command}' executed successfully.")
            except subprocess.CalledProcessError as e:
                print(f"Error running command: {e}")

if __name__ == "__main__":
    setup = EnvironmentSetup()
    setup.setup_environment()

