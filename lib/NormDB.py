# -*- coding: utf-8 -*-
from web import database
# import SAE CONSTANTS

MYSQL_DB = "AccessLoger"
MYSQL_USER = "flame"
MYSQL_PASS = "emalf"
MYSQL_HOST = "122.202.100.230"
MYSQL_PORT = 3306

DB = database(
	dbn = 'mysql',
	host = MYSQL_HOST, 
	user = MYSQL_USER, 
	pw = MYSQL_PASS, 
	db = MYSQL_DB, 
	port = MYSQL_PORT)