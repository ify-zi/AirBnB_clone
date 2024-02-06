#!/usr/bin/env python3
"""
    File_storage module
"""


import json


class FileStorage:
    """
        serialization and deserialization class
    """

    def __init__(self):
        """
            Initialization method
        """
        self.__file_path
        self.__objects

    def all(self):
        """
            return all dictionary of __object
        """
        obj_dict = self.__objects.__dict__.copy()
        return obj_dict

    def new(self, obj):
        """
            set the object with a an id
        """
        if obj:
            setattr(self.__objects, obj.id, obj)

    def save(self):
        """
            serializes python objects to JSON file
        """
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(self.__objects, f)
