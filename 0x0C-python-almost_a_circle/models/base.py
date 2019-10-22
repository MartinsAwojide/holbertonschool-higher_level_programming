#!/usr/bin/python3
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """json strng representation"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes a json representation to a file"""
        filename = cls.__name__ + ".json"
        new_list = []
        if list_objs:
            for i in list_objs:
                new_list.append(i.to_dictionary())
        with open(filename, "w") as f:
            string = cls.to_json_string(new_list)
            f.write(string)

    @staticmethod
    def from_json_string(json_string):
        """return list if json representation"""
        new_list = []
        if json_string:
            new_list = json.loads(json_string)
        return new_list

    @classmethod
    def create(cls, **dictionary):
        """Creates a dummy instance and updates it"""
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """A function that loads from a file and returns a list of instances"""
        filename = cls.__name__ + ".json"
        new_list = []
        try:
            with open(filename, "r") as f:
                lines = f.read()
                lines_converted = cls.from_json_string(lines)
                for i in range(len(lines_converted)):
                    new_list.append(cls.create(**lines_converted[i]))
                return new_list
        except:
            return new_list
