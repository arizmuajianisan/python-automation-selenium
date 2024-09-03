import os


def clean_directories(directories):
    """
    Deletes all .tmp and .zip files in the specified directories.

    :param directories: A list of directories to clean.
    """
    # Iterate through each directory in the list
    for directory in directories:
        # List all files in the directory
        files = os.listdir(directory)

        # Iterate through the files and delete .tmp and .zip files
        for file in files:
            if file.endswith(".tmp") or file.endswith(".zip"):
                file_path = os.path.join(directory, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")


if __name__ == "__main__":
    # Example usage:
    directories_to_clean = ["path/to/folder1", "path/to/folder2", "path/to/folder3"]
    clean_directories(directories_to_clean)
