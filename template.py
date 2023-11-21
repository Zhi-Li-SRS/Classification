import logging
import os
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")

name = "src"
# * create a list of files in this project folder
list_of_files = [
    ".github/workflows/.gitkeep",
    f"{name}/__init__.py",
    f"{name}/exception/__init__.py",
    f"{name}/logger/__init__.py",
    "utils/__init__.py",
    "utils/main_utils.py",
    "data/__init__.py",
    "models/__init__.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "test.py",
]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory: {file_dir} for the file {file_name}")

    if (not os.path.exists(file_name)) or (os.path.getsize(file_name) == 0):
        with open(file_path, "w") as f:
            pass
            logging.info(f"Creating empty file: {file_name}")
    else:
        logging.info(f"{file_name} is already created")
