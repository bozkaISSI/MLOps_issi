import os
import subprocess
import yaml

def load_secrets_from_sops_yaml(file_path: str) -> None:
    """
    Decrypt a SOPS-encrypted YAML file and load the key-values into environment variables.
    """
    result = subprocess.run(["sops", "-d", file_path], capture_output=True, text=True)

    if result.returncode != 0:
        raise RuntimeError(f"Failed to decrypt secrets file: {result.stderr}")

    try:
        secrets = yaml.safe_load(result.stdout)
    except yaml.YAMLError as e:
        raise ValueError(f"Invalid YAML format in decrypted secrets file: {e}")

    for key, value in secrets.items():
        os.environ[key.upper()] = str(value)
