import os
import argparse
from dotenv import load_dotenv
from settings import Settings

def export_envs(environment: str = "dev") -> None:
    """
    This function loads the corresponding .env file based on the provided environment argument.
    It raises a FileNotFoundError if the file doesn't exist.
    """
    env_file = f".env.{environment}"  # Construct the .env file name dynamically
    if os.path.exists(env_file):
        load_dotenv(env_file)  # Load the .env file
        print(f"Loaded environment variables from {env_file}")  # Optional: Debugging message
    else:
        raise FileNotFoundError(f"{env_file} not found")  # Raise an error if file does not exist

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Load environment variables from specified .env file.")
    parser.add_argument("--environment", type=str, default="dev", help="The environment to load (dev, test, prod)")
    args = parser.parse_args()

    # Load environment variables based on the provided environment
    export_envs(args.environment)

    # Instantiate settings to access environment variables
    settings = Settings()

    # Print the settings to verify the environment variables
    print("APP_NAME:", settings.APP_NAME)
    print("ENVIRONMENT:", settings.ENVIRONMENT)
