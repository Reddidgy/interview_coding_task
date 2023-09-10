import os
from dotenv import load_dotenv
import sys
from colorama import Fore, Style

load_dotenv()  # Load variables from .env file

# Global variables
real_token = os.environ.get("TOKEN")
error_message = "\nError. Please provide token with --token=XXXXXXXXXXXXXXX parameter\n"


def main():
    if len(sys.argv) > 1:
        if sys.argv[1].startswith("--token="):
            token_to_challenge = sys.argv[1].split("=")[1]
        elif sys.argv[1].startswith("--token") and len(sys.argv) > 2:
            token_to_challenge = sys.argv[2]
        else:
            print(Fore.LIGHTRED_EX + error_message + "\n")
            exit()
    else:
        print(Fore.LIGHTRED_EX + error_message + Style.RESET_ALL)
        exit()

    if real_token == token_to_challenge:
        print(Fore.LIGHTGREEN_EX + "\nTask completed. Token is correct!\n\nCongratulations! :)\n" + Style.RESET_ALL)
    else:
        print(Fore.LIGHTRED_EX + "\nToken is incorrect! Task isn't completed!\n" + Style.RESET_ALL)


if __name__ == '__main__':
    main()
