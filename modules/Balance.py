#!/usr/bin/env python
# encoding: utf-8
"""
Balance.py

Created by 姚 远 on 2011-12-27.
Copyright (c) 2011 ManaFlame. All rights reserved.
"""

from modules.base import Base
import urllib2

class Balance(Base):
	"""docstring for Settings"""
	def add(self,**kw):
		id = self.last_id() + 1
		self.sdb.insert(self.table,id=id,**kw)
	
	def out(self,uid,day,value,page):
		import datetime
		ds = datetime.datetime.strptime("%s 00:00:00" % day, "%Y-%m-%d %H:%M:%S")
		de = datetime.datetime.strptime("%s 23:59:59" % day, "%Y-%m-%d %H:%M:%S")
		SQL = "SELECT id FROM %s WHERE page = '%s' AND user=%s AND value < 0 AND time >= '%s' AND time <= '%s'"
		PARA = (self.table,page,uid,ds,de)
		x = self.sdb.query(SQL % PARA)
		r = len(x)
		if not r:
			self.add(page=page,value=value,user=uid)
		else:
			w = "id = %s" % x[0].id
			self.sdb.update(self.table,where=w,value=value,user=uid,page=page)
		
	def ShowAll(self,UserId):
		return self._get(user=UserId)

	def Left(self,UserId):
		balances = self.ShowAll(UserId)
		b = 0
		for balance in balances:
			b += balance.value
		return b
	
	def Total(self,UserId):
		data = self._where("value","value > 0 AND user = %s" % UserId)
		t = 0
		for item in data:
			t += item.value
		return t