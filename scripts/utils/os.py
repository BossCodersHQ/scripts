from pathlib import Path

def get_curr_dir(file_path: str) -> Path:
    return Path(file_path).resolve().parent
