#!/usr/bin/python3
"""Module containing class FileStorage"""
import datetime
import os
import json


class FileStorage:

    """
    Class that serializes instances to a JSON file and deserializes
    JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        return the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        serialized_objects = {}
        #k stands for key
        #o for value
        for k, o in FileStorage.__objects.items():
            serialized_objects[k] = o.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**o)
                        for k, o in obj_dict.items()}
            FileStorage.__objects = obj_dict
