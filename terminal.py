import subprocess
import os
from dotenv import load_dotenv
from colorama import Fore, Style

load_dotenv()  # Load variables from .env file

# Variables
TOKEN = os.environ.get("TOKEN")
terminal_started = False
apt_commands_array = ["apt install", "apt update", "apt upgrade", "apt-get install", "apt-get update",
                      "apt-get upgrade"]
timeout = 60


def command_with_output(command):
    output = subprocess.check_output(command, shell=True)
    return output.decode().strip()


def cli_start_string_coloring(user, host, pwd):
    colored_user_host = Fore.LIGHTGREEN_EX + user + "@" + host + Style.RESET_ALL
    colored_pwd = Fore.LIGHTBLUE_EX + pwd + Style.RESET_ALL
    start_string = f"{colored_user_host}:{colored_pwd}$ "
    return start_string


def main():
    global terminal_started
    if terminal_started:
        print("")
    else:
        terminal_started = True
        print(Fore.LIGHTYELLOW_EX + "Terminal initiated!\n" + Fore.LIGHTGREEN_EX + "To successfully complete the "
                                                                                   "task, execute the command using "
                                                                                   "the appropriate token in the "
                                                                                   "following format:\n" + Fore.CYAN
              + "python3 app.py --token=XXXXXXXXXXXX\n")

    while True:
        user = command_with_output("whoami")
        hostname = command_with_output("hostname")
        pwd = command_with_output("pwd")

        user_command = input(cli_start_string_coloring(user, hostname, pwd))

        # Before the command
        if "apt" in user_command:
            for apt_command in apt_commands_array:
                if apt_command in user_command:
                    user_command += " -y"

        if user_command == "ll":
            user_command = "ls -la"

        process = subprocess.Popen([user_command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True,
                                   executable='/bin/bash')
        # After the command
        try:
            output, error = process.communicate(timeout=timeout)
            if error:
                print(error.decode().strip())
            else:
                if TOKEN in output.decode():
                    print(f'Forbidennicht!11 Sensitive information!')
                elif user_command.startswith('cd '):
                    new_dir = user_command.split(' ')[1]
                    os.chdir(new_dir)
                else:
                    print(output.decode().strip())
        except subprocess.TimeoutExpired:
            process.kill()  # Kill the process if it times out
            print("Command timed out of 20 seconds.")


# Main cycle
while True:
    if __name__ == '__main__':
        try:
            main()
        except:
            pass

#
