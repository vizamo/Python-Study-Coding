"""Information about directories/files in current dit in JSON."""
import json
import os
from pathlib import Path


class ObjectAttributes:

    def __init__(self, path, filename):
        """."""
        self.path = path
        self.filename = filename
        self.path_to_obj = path + "/" + filename

    def mask(self) -> str:
        """Return object permission mask."""
        return oct(os.stat(self.path_to_obj).st_mode)[-3:]

    def owner(self) -> str:
        """Return file owner."""
        return Path(self.path_to_obj).owner()

    def type(self) -> str:
        """Return, does object is file or directory."""
        if os.path.isfile(self.path_to_obj):
            return "file"
        return "directory"


class ConvertDirectory:

    def main_directory(self, path=os.getcwd()):
        """
        :param path - way to main directory, default its current dir
        Main_directory is static information
        Children is dirs and files in current directory.
        """
        objects_in_dir: list = os.listdir(path)
        object_attributes = ObjectAttributes(path, "")
        main_directory = {
            "name": ".",
            "path": ".",
            "mask": object_attributes.mask(),
            "owner": object_attributes.owner(),
            "type": "directory",
        }
        if objects_in_dir:
            children = self.find_info_ab_dir(objects_in_dir, path)
            main_directory['children'] = children

        print(self.convert_to_json(main_directory))

    def find_info_ab_dir(self, objects_in_dir: list, path: str):
        """
        :param objects_in_dir - list of all files/directories in path.
        Empty list, if no files in directory.
        :param path - way to examined directory
        :return all child object which in main_directory:
        """
        children = []
        for object_in_dir in objects_in_dir:
            object_attributes = ObjectAttributes(path, object_in_dir)
            path_to_obj = object_attributes.path_to_obj
            obj_type = object_attributes.type()
            file_info = {
                "name": object_in_dir,
                "path": path_to_obj,
                "mask": object_attributes.mask(),
                "owner": object_attributes.owner(),
                "type": obj_type,
            }

            # If object is directory, get all files in it
            if obj_type == "directory":
                dir_objects = os.listdir(path_to_obj)
                files_in_dir = self.find_info_ab_dir(dir_objects, path_to_obj)
                if files_in_dir:
                    file_info['children'] = files_in_dir
            children.append(file_info)
        return children

    @staticmethod
    def convert_to_json(main_directory):
        """Convert dict to json with pretty line indent."""
        to_json = json.dumps(main_directory, indent=4)
        return to_json


ConvertDirectory().main_directory()
