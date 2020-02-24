#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

import conf

host = "192.168.0.202"
datauser = "root"
datapass = "fsp200@HW"
database = "zsldatabase"


class MysqlBase():
    def _init_():
        pass
        #self.host = "192.168.0.202"
        #self.datauser = "root"
        #self.datapass = "fsp200@HW"
        #self.database = "zsldatabase"

    def connect(self,host,user,passwd,database):
        self.db = MySQLdb.connect(host,user,passwd,database,charset='utf8')

