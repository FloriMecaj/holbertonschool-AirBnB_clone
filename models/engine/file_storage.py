#!/usr/bin/python3
import json
import os


"""Write a class FileStorage """


class FileStorage:

    def __init__(self, file_path):
        self.__file_path = file_path
        self.__objects = {}
        self.reload()  # Load objects from file if it exists

    def all(self):
        return self.__objects

    def new(self, obj):
        class_name = obj.__class__.__name__
        key = f"{class_name}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, 'w') as file:
            json.dump(self.__objects, file)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                self.__objects = json.load(file)
        else:
            pass  # Do nothing if the file doesn't exist
