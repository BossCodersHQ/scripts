from scripts.utils.os import get_curr_dir


def get_output_dir():
    """Get the data directory for the daily coding problem module."""
    return get_curr_dir(__file__) / "output"

def get_assets_dir():
    """Get the assets directory for the daily coding problem module."""
    return get_curr_dir(__file__) / "assets"
