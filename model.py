#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections
from util import has_attr, is_empty


class person(collections.MutableMapping):
    LABEL = "person"
    ID = "_id"
    NAME = "name"
    AGE = "age"
    GENDER = "gender"

    def __init__(self, _id=None, name=None, age=None, gender=None):
        self._id = _id
        self.name = name
        self.age = age
        self.gender = gender

    def __getattr__(self, name):
        return self.__getitem__(name)

    def __setattr__(self, name, value):
        self.__setitem__(name, value)

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        if (self.ID == key and value is None) or (is_empty(value) and self.ID != key and has_attr(self, key)):
            return
        self.__dict__[key] = value

    def __delitem__(self, key):
        del self.__dict__[key]

    def __iter__(self):
        return iter(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __str__(self):
        '''Returns simple dict representation of the mapping'''
        return str(self.__dict__)

    def __repr__(self):
        '''Echoes class, id, & reproducible representation in the REPL'''
        return f'{super().__repr__()}, {__class__.__name__}({self.__dict__})'
