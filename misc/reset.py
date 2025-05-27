import os
import shutil

def reset(root_dir):
    """
    Deletes the __pycache__ and instance folders from the given root directory
    and all subdirectories.
    """
    if root_dir is None:
        raise ValueError("root_dir cannot be None")

    for dirpath, _, _ in os.walk(root_dir, topdown=False):
        if os.path.basename(dirpath) in ('__pycache__'):
            print(f"Deleting: {dirpath}")
            shutil.rmtree(dirpath)

if __name__ == "__main__":
    root_directory = '.'
    reset(root_directory)

