#!/usr/bin/env python
# encoding: utf-8
"""
base.py

Created by 姚 远 on 2011-12-27.
Copyright (c) 2011 ManaFlame. All rights reserved.
"""
from lib.NormDB import DB as ndb
from lib.LocalDB import DB as ldb

dbDict = {'norm':ndb,'local':ldb}

class Base():
	"""docstring for Base"""
	def __init__(self,TName,db="norm"):
		self.table = TName
		self.sdb = dbDict[db]

	def count(self,key):
		SQL = 'SELECT COUNT(%s) FROM %s'
		PARA = (key,self.table)
		return self.sdb.query(SQL % PARA)[0].values()[0]
	
	def last_id(self):
		SQL = 'SELECT id FROM %s ORDER BY id DESC'
		PARA = self.table
		try:
			return self.sdb.query(SQL % PARA)[0].id
		except IndexError:
			return 0
		
	def show(self,number,order):
		return self.sdb.select(self.table, limit=number, order=order)
	
	def get(self,key,value):
		myvar = { key : value }
		where = '%s = $%s' % (key,key) 
		results = self.sdb.select(self.table, myvar, where=where,order='id ASC')
		return results

	def _get(self,**kwargs):
		myvar = kwargs
		wherelist = []
		for key in kwargs.keys():
			w = "%s = $%s" % (key,key)
			wherelist.append(w)
		where = " AND ".join(wherelist)
		results = self.sdb.select(self.table, myvar, where=where,order='id ASC')
		return results
		
	def delete(self,id):
		"""docstring for delete"""
		PARA = "%s=%s" % ('id',id)
		self.sdb.delete(self.table, where=PARA)
	
	def page(self,PNum,PAGE_LENGTH):
		A = PAGE_LENGTH * PNum
		B = PAGE_LENGTH * (PNum - 1)
		SQL = """SELECT * FROM %s ORDER BY %s DESC LIMIT %s,%s"""
		PARA = (self.table,'id',B,A)
		return self.sdb.query(SQL % PARA)
	
	def _set(self,id,**kw):
		w = "id=%s" % id
		self.sdb.update(self.table,where=w,**kw)