#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import MongoClient
from pymongo.database import Database as MongoDB


class Database(MongoDB):
    __DBNAME = "dbtest"
    __HOST = "localhost"
    __PORT = 27017

    def __init__(self, dbname=__DBNAME, host=__HOST, port=__PORT):
        self.mongoclient = MongoClient(f"mongodb://{host}:{port}/")
        MongoDB.__init__(self, client=self.mongoclient, name=dbname)
