#!/usr/bin/env python
# -*- coding: utf-8 -*-

from model import person
from database import Database


class persondao():
    def __init__(self):
        self.__database = Database()
        self.__collection = self.__database[person.LABEL]

    def insert_one(self, person):
        return self.__collection.insert_one(person)

    def insert_many(self, people):
        return self.__collection.insert_many(people)

    def update_one(self, _id, person):
        return self.__collection.update_one({person.ID: _id}, {'$set': person})

    def delete_one(self, person):
        if person is not None:
            self.__collection.delete_one(person)

    def list_all(self):
        return [person(**doc) for doc in self.__collection.find()]

    def find_by_id(self, _id):
        res = self.__collection.find_one({person.ID: int(_id)})
        return person(**res) if res else None

    def find_by_name(self, name):
        '''Returns a list of person with the given name'''
        return [person(**doc) for doc in self.__collection.find({'name': {'$regex': name, '$options': 'i'}})]

    def count_documents(self):
        return self.__collection.estimated_document_count()

    def exist(self):
        return person.LABEL in self.__database.list_collection_names()

    def drop(self):
        self.__collection.drop()

    def last_id(self):
        p = self.__collection.find_one({'$query': {}, '$orderby': {person.ID: -1}})
        return p[person.ID] if p is not None else 0
