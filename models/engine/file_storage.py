#!/usr/bin/python3
"""
    File_storage module
"""


import json
from models.base_model import BaseModel


classes = {"BaseModel": BaseModel}


class FileStorage:
    """
        serialization and deserialization class
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            return all dictionary of __object
        """
        return self.__objects

    def new(self, obj):
        """
            set the object with a an id
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """
            serializes python objects to JSON file
        """
        json_objects = {}
        for key, value in self.__objects.items():
            json_objects[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """
            deserialize from json to python object dict
        """
        try:
            with open(self.__file_path, 'r') as f:
                file_dict = json.load(f)
            for key in file_dict:
                self.__objects[key] = classes[file_dict[key]["__class__"]]
                (**file_dict[key])
        except FileNotFoundError:
            pass
