#!/usr/bin/env python
# encoding: utf-8
"""
Record.py

Created by 姚 远 on 2011-12-27.
Copyright (c) 2011 ManaFlame. All rights reserved.
"""

from modules.base import Base
from lib.common import DateToTimeStamp
from lib.common import HourToTimeStamp

def isLeap(yr):
    if not yr % 4 and (yr % 100 or not yr % 400):
        return [None,31,29,31,30,31,30,31,31,30,31,30,31]
    return [None,31,28,31,30,31,30,31,31,30,31,30,31]

def days_in_month(year,month):
	return isLeap(year)[month]

def zform(intg):
	if len(str(intg)) == 1:
		return "0%s" % intg
	else:
		return str(intg)

rdic = {'day':0,'month':1}

class Record(Base):
	"""docstring for Settings"""
	def add(self,**kw):
		id = self.last_id() + 1
		self.sdb.insert(self.table,id=id,**kw)
	
	def renew(self,hour,date,page,value,RecType):
		if self._thereis(hour,date,page,RecType):
			w = "hour='%s' AND date='%s' AND page='%s' AND kind='%s'" % (hour,date,page,rdic[RecType])
			self.sdb.update(self.table,where=w,value=value,kind=rdic[RecType])
		else:
			self.add(hour=hour,date=date,page=page,value=value,kind=rdic[RecType])
	
	def _thereis(self,hour,date,page,RecType):
		SQL = "SELECT id FROM %s WHERE hour = '%s' AND date='%s' AND page='%s' AND kind = '%s'"
		PARA = (self.table,hour,date,page,rdic[RecType])
		r = self.sdb.query(SQL % PARA)
		print len(r)
		return len(r)
	
	def Get(self,date,page,RecType):
		data = self._get(date=date,page=page,kind=rdic[RecType])
		x = []
		y = []
		i = 0
		for item in data:
			if RecType == "day":
				x.append([ HourToTimeStamp("%s %s:00:00" % (date,item.hour)) ,int(item.value)])
			elif RecType == "month":
				x.append([ DateToTimeStamp("%s-%s" % (date,item.hour)),int(item.value)])
				y.append([ DateToTimeStamp("%s-%s" % (date,item.hour)),int(self.frate(item.id)*item.value) ])
			i += item.value
		return x,i
	
	def _frate(self,parent):
		from modules.Rate import Rate
		rate = Rate('flame_fake_rate','local')
		return rate._get(parent=parent)[0].rate