import subprocess
import os
from dotenv import load_dotenv
from colorama import Fore, Style, Back
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PythonLexer

load_dotenv()  # Load variables from .env file

# Variables
TOKEN = os.environ.get("TOKEN")
terminal_started = False
apt_commands_array = ["apt install", "apt update", "apt upgrade", "apt-get install", "apt-get update",
                      "apt-get upgrade"]
timeout = 60
terminal_title = "Stole Token Task"
sensitive_info_message = "\nSensitive information is securely protected. Please attempt an alternative approach.\n"
variables_protection_message = ("\nUtilizing variables in this context is restricted. Kindly employ the actual token "
                                "value instead.\n")
terminal_started_message = Fore.LIGHTYELLOW_EX + "\nTerminal initiated!" + Style.RESET_ALL
help_message = ("\nTo complete the task, execute the command using " \
                                                                                    "the appropriate token in the " \
                                                            "following format:\n" + Back.BLACK + Fore.LIGHTWHITE_EX +\
               "\npython3 app.py --token=XXXXXXXXXXXX\x1b[0m\n\n" + Fore.LIGHTYELLOW_EX +\
                "Type " + Back.BLACK + Fore.LIGHTWHITE_EX + "help" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX +
                " anytime to see this message.\n" + Style.RESET_ALL)


def command_with_output(command):
    output = subprocess.check_output(command, shell=True)
    return output.decode().strip()


def cli_start_string_coloring(user, host, pwd):
    colored_user_host = Fore.LIGHTGREEN_EX + user + "@" + host + Style.RESET_ALL
    colored_pwd = Fore.LIGHTBLUE_EX + pwd + Style.RESET_ALL
    start_string = f"{colored_user_host}:{colored_pwd}$ "
    return start_string


def ubuntu_command(command):
    process = subprocess.Popen([command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True,
                               executable='/bin/bash')
    return process


def main():
    global terminal_started
    if not terminal_started:
        terminal_started = True
        title_change_process = ubuntu_command('echo -ne "\033]0;Stole Token Task\007"')
        output, error = title_change_process.communicate(timeout=timeout)
        print(output.decode().strip())
        print(terminal_started_message)
        print(help_message)

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

        if "ll" in user_command:
            user_command = user_command.replace("ll", "ls -la")

        if "app.py" in user_command and "$" in user_command:
            print(Fore.LIGHTRED_EX + variables_protection_message)
            user_command = ""

        if user_command == "help":
            print(help_message)
            user_command = ""

        process = ubuntu_command(user_command)
        # After the command
        try:
            output, error = process.communicate(timeout=timeout)
            if error:
                print(error.decode().strip())
            else:
                if TOKEN in output.decode():
                    print(Fore.LIGHTRED_EX + sensitive_info_message)
                elif user_command.startswith('cd '):
                    new_dir = user_command.split(' ')[1]
                    os.chdir(new_dir)
                elif user_command.startswith("cat ") and ".py" in user_command:
                    # print codeblock colored for user comfort
                    print(highlight(output.decode(), PythonLexer(), TerminalFormatter()))
                else:
                    print(output.decode().strip())
        except subprocess.TimeoutExpired:
            process.kill()  # Kill the process if it times out
            print("Command timed out of 60 seconds.")


# Main cycle
while True:
    if __name__ == '__main__':
        try:
            main()
        except:
            pass

# while True: # todo: return good cycle
#     main()
