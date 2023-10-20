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
            "sudo apt install ansible -y"     # Install Ansible
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
