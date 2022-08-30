"""Find, check and delete files, which have 777 permission mask."""
import inotify.adapters
import os
import time
import subprocess as notification


class Permission:

    path = os.getcwd()
    full_pm_mask = str(777)
    no_action_mode = False  # don't delete files, just inform about full pm

    def check_mask(self, path_to_file):
        """Return file permission mask."""
        mask = oct(os.stat(path_to_file).st_mode)[-3:]
        if mask == self.full_pm_mask:
            print(f"Found file with full permission: {path_to_file}")
            return True

    def remove_file(self, path_to_file, call_from="monitor"):
        """
        If no_action_mode is False, remove file from dir.
        call_from could be from check or monitor.
        """
        if self.no_action_mode is False:
            sleep_time = 0 if call_from == "check" else 2
            time.sleep(sleep_time)
            os.remove(path_to_file)
            print(f"File {path_to_file} is removed")

    @staticmethod
    def create_notification(header, text):
        """."""
        notification.call(["notify-send", header, text])


class PermissionCheck(Permission):

    def check_all_permissions(self):
        """
        Check all files masks in current dir and subdirectories
        If found file with full permission mask, it will be deleted
        """
        count = 0
        for path_to_dir, dir_names, file_names in os.walk(self.path):
            for file in file_names:
                path_to_file = path_to_dir + "/" + file
                check_mask = self.check_mask(path_to_file)
                if check_mask is True:
                    self.remove_file(path_to_file, "check")
                    count += 1
        if count > 0:
            print(f"Check is ended. Found {count} files with full permission")
        else:
            print("Check is ended. Not found files with full permission")


class PermissionMonitor(Permission):

    def monitor_permission_changes(self):
        """
        Monitors metadata changes
        If change happens, check permission
        If permission changed to 777 - delete this file
        and create notification.
        """
        in_attrib_flag = 4  # Check metadata changes

        # Watch in current dir and subdirectories
        i = inotify.adapters.InotifyTree(self.path, in_attrib_flag)

        for event in i.event_gen(yield_nones=False):
            try:
                (header, type_names, watch_path, filename) = event
                path_to_file = watch_path + "/" + filename
                check_mask = self.check_mask(path_to_file)
                if check_mask is True:
                    not_header = "New file with full permission"
                    not_text = f"{filename} in {watch_path}"
                    self.create_notification(not_header, not_text)
                    self.remove_file(path_to_file, "monitor")
            except FileNotFoundError:
                continue


PermissionCheck().check_all_permissions()
PermissionMonitor().monitor_permission_changes()
