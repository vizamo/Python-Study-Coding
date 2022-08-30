"""Move files in specified backup directory if they are modified week ago or longer"""
import os
import time


class MoveOldFiles:

    week_in_seconds = 604800
    backup_dir = "../test/backup/"

    def move_old_files(self):
        """
        Move files in backup directory
        if they are modified week ago or longer.
        """
        files_in_directory = [file for file in os.listdir()
                              if os.path.isfile(file)]
        moved_files = []
        for file in files_in_directory:
            epoch_dif = self.calc_epoch_dif(file)
            if epoch_dif >= self.week_in_seconds:
                os.replace(file, self.backup_dir + file)
                moved_files.append(file)
        if moved_files:
            print(f"To directory {self.backup_dir} moved {moved_files}")
        else:
            print("No matching files")

    @staticmethod
    def calc_epoch_dif(filename) -> float:
        """Calculate difference in time now and last modification time"""
        return time.time() - os.path.getmtime(filename)


MoveOldFiles().move_old_files()
