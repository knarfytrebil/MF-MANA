# -*- coding: utf-8 -*-
from web import database
# import SAE CONSTANTS

MYSQL_DB = "flame"
MYSQL_USER = "root"
MYSQL_PASS = "B166er"
MYSQL_HOST = "localhost"
MYSQL_PORT = 3306

DB = database(
	dbn = 'mysql',
	host = MYSQL_HOST, 
	user = MYSQL_USER, 
	pw = MYSQL_PASS, 
	db = MYSQL_DB, 
	port = MYSQL_PORT)