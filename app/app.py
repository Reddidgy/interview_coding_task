import os
from dotenv import load_dotenv
import sys

load_dotenv()  # Load variables from .env file

# Global variables
real_token = os.environ.get("TOKEN")
error_message = "Error. Please provide token with --token=XXXXXXXXXXXXXXX parameter"


def main():
    if len(sys.argv) > 1:
        if sys.argv[1].startswith("--token="):
            token_to_challenge = sys.argv[1].split("=")[1]
        elif sys.argv[1].startswith("--token") and len(sys.argv) > 2:
            token_to_challenge = sys.argv[2]
        else:
            print(error_message)
            exit()
    else:
        print(error_message)
        exit()

    if real_token == token_to_challenge:
        print("Task completed. Token is correct!\nCongratulations! :)")
    else:
        print("Token is incorrect! Task isn't completed!")


if __name__ == '__main__':
    main()
