"""
Configuration module to load settings from a YAML file.
"""
import yaml

def load_config(path="config.yaml"):
    """
    Loads the configuration from the given YAML file.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print(f"ERROR: Configuration file not found at '{path}'.")
        print("Please copy 'config.yaml.example' to 'config.yaml' and fill in your details.")
        return None
