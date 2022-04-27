from typing import Union
from pathlib import Path


class File:
    """
    A wrapper that handles reading and writing to the file in a more convienient way.

    Call read to get the original file string.

    Call write to save your file string to the file.

    Handles backups automatically.
    """

    def __init__(self, file_name: Union[str, Path], backup: bool = True):
        self.file_name: Path = Path(file_name)
        self.backup: bool = backup

    def write(self, string: str, mode: str = "w"):
        """
        Overwrites the final file string.
        """
        if self.backup:
            # Check if the backup already exists. Refuse to overwrite.
            backup_file_name: Path = Path(str(self.file_name) + ".bk")
            if backup_file_name.is_file():
                raise Exception("Backup file already exists. Will not overwrite.")

            # Rename the file to the backup file
            self.file_name.rename(backup_file_name)

        # Write to the file name the new string
        with self.file_name.open(mode) as f:
            f.write(string)

    def read(self, mode: str = "r"):
        """
        Reads the file.
        """
        with self.file_name.open(mode) as f:
            return f.read()

    def __str__(self):
        return self.read()
