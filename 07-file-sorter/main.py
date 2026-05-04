from pathlib import Path

categories = {
    ".mp3": "Music",
    ".wav": "Music",
    ".flac": "Music",
    ".avi": "Videos",
    ".mp4": "Videos",
    ".gif": "Videos",
    ".txt": "Documents",
    ".pptx": "Documents",
    ".csv": "Documents",
    ".xls": "Documents",
    ".odp": "Documents",
    ".pages": "Documents",
    ".bmp": "Images",
    ".png": "Images",
    ".jpg": "Images",
}

source_folder = Path("~/Github/Python-training/07-file-sorter/data").expanduser()

for file in source_folder.iterdir():
    if file.is_file():
        extension = file.suffix
        folder_name = categories.get(extension, "Others")
        dest_folder = source_folder / folder_name
        dest_folder.mkdir(exist_ok=True)
        file.rename(dest_folder / file.name)