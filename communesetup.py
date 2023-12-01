import subprocess
import time

class EnvironmentSetup:
    def __init__(self):
        self.commands = [
            "sudo apt update",
            "sudo apt install npm",
            "npm install pm2",
            "git clone https://github.com/commune-ai/commune.git",
            "sudo apt update && sudo apt upgrade -y",
            "sudo apt install software-properties-common -y",
            "sudo add-apt-repository ppa:deadsnakes/ppa",
            "python3.10 --version",
            "sudo apt install python3.10",
            "sudo apt install python3-pip -y",  # Install pip for Python 3
            "cd commune",
            "sudo apt-get install -y python-click",
            "pip install -U numpy",
            "pip install --upgrade pip",
            "pip install protobuf==3.20",
            "pip install streamlit grpcio-tools",
            "pip install -e ./",
            "cd scripts",
            "./install_rust_env.sh",
            "cd ..",
            "curl -SL https://github.com/docker/compose/releases/download/v2.20.3/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose",
            "sudo chmod +x /usr/local/bin/docker-compose",
            "sudo apt install docker.io",
            "cd /commune",
            "rm -rf ./subspace",
            "make pull",
            "pip install -U click"
        ]

    def run_commands_with_delay(self, delay_seconds=5):
        for command in self.commands:
            subprocess.run(command, shell=True, check=True)
            time.sleep(delay_seconds)

# Create an instance of EnvironmentSetup
env_setup = EnvironmentSetup()

# Run the commands with a 5-second delay between each action
env_setup.run_commands_with_delay(5)

                subprocess.run(command, shell=True, check=True)
                print(f"Command '{command}' executed successfully.")
            except subprocess.CalledProcessError as e:
                print(f"Error running command: {e}")

if __name__ == "__main__":
    setup = EnvironmentSetup()
    setup.setup_environment()

