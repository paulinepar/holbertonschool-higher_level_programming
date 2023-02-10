#!/usr/bin/python3
'''
    Write a class Student that defines a student
'''


class Student():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        list = {}
        if attrs is not None:
            for i in attrs:
                if i in self.__dict__:
                    list[i] = self.__dict__[i]
            return list
        else:
            return self.__dict__
