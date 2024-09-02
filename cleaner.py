import os


def clean_directory(directory):
    """
    Deletes all .csv and .tmp files in the specified directory.

    :param directory: The directory to clean.
    """
    # List all files in the directory
    files = os.listdir(directory)

    # Iterate through the files and delete .csv and .tmp files
    for file in files:
        # if file.endswith(".csv") or file.endswith(".tmp") or file.endswith(".zip"):
        if file.endswith(".tmp") or file.endswith(".zip"):
            file_path = os.path.join(directory, file)
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Failed to delete {file_path}: {e}")
