import os
import argparse
from dotenv import load_dotenv
from settings import Settings
from utils.secrets_loader import load_secrets_from_sops_yaml  # <-- Import secret loader

def export_envs(environment: str = "dev") -> None:
    """
    Load .env.<environment> file and decrypted secrets YAML file.
    """
    env_file = f".env.{environment}"
    if os.path.exists(env_file):
        load_dotenv(env_file)
        print(f"Loaded environment variables from {env_file}")
    else:
        raise FileNotFoundError(f"{env_file} not found")

    # Decrypt secrets YAML file using SOPS
    secrets_file = f"secrets/{environment}.yaml"
    if os.path.exists(secrets_file):
        load_secrets_from_sops_yaml(secrets_file)
        print(f"Loaded secrets from {secrets_file}")
    else:
        print(f"Warning: {secrets_file} not found. Skipping secrets loading.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load environment variables and secrets.")
    parser.add_argument("--environment", type=str, default="dev", help="Specify environment: dev, test, prod")
    args = parser.parse_args()

    export_envs(args.environment)

    settings = Settings()

    print("APP_NAME:", settings.APP_NAME)
    print("ENVIRONMENT:", settings.ENVIRONMENT)
    print("API_KEY:", settings.API_KEY)  # <-- To verify the secret is loaded
