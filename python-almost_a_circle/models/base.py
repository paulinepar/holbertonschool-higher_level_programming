#!/usr/bin/python3
'''
    Write the first class Base:
'''
import json


class Base():
    '''class'''

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''dict to json string'''
        if list_dictionaries is None:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        with open(cls.__name__+".json", "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list = []
                for clas in list_objs:
                    list.append(clas.to_dictionary())
                file.write(Base.to_json_string(list))
