# -*- coding: utf-8 -*-
from web import database
# import SAE CONSTANTS
from sae import const

MYSQL_DB = const.MYSQL_DB
MYSQL_USER = const.MYSQL_USER
MYSQL_PASS = const.MYSQL_PASS
MYSQL_HOST = const.MYSQL_HOST
MYSQL_PORT = int(const.MYSQL_PORT)

SDB = database(
	dbn = 'mysql',
	host = MYSQL_HOST, 
	user = MYSQL_USER, 
	pw = MYSQL_PASS, 
	db = MYSQL_DB, 
	port = MYSQL_PORT)