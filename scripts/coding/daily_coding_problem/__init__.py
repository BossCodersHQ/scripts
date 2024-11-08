from scripts.utils.os import get_curr_dir


def get_data_dir():
    """Get the data directory for the daily coding problem module."""
    return get_curr_dir(__file__) / "data"
