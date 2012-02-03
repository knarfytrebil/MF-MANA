#!/usr/bin/env python
# encoding: utf-8
"""
Log.py

Created by 姚 远 on 2011-12-27.
Copyright (c) 2011 ManaFlame. All rights reserved.
"""

from modules.base import Base
import urllib2

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

class Logs(Base):
	"""docstring for Settings"""
	def add(self,name,value,kind):
		id = self.last_id() + 1
		self.sdb.insert(self.table,title=name,value=value,type=kind,id=id)
	
	def _between(self,dir,arg,a,b):
		return self.sdb.query("SELECT * FROM %s WHERE Dir = '%s' AND %s >= '%s' AND %s <= '%s'" % (self.table,dir,arg,a,arg,b))
	
	def _hours(self,Date,Dir):
		from datetime import datetime
		hours = []
		for i in range(0,24):
			hours.append([i,0])
		data = self._day(Date,Dir)
		for item in data:
			hours[item.AccTime.hour][1] += 1
		return hours,len(data)
	
	def _day(self,Date,Dir):
		from datetime import datetime
		ds = datetime.strptime("%s 00:00:00" % Date, "%Y-%m-%d %H:%M:%S")
		de = datetime.strptime("%s 23:59:59" % Date, "%Y-%m-%d %H:%M:%S")
		return self._between(Dir,"AccTime",ds,de)

	def _days(self,Month,Dir):
		from datetime import datetime,date
		days = []
		year = int(Month.split('-')[0])
		month = int(Month.split('-')[1])
		for i in range(1,days_in_month(year,month)+1):
			days.append([i,0])			
		data = self._month(Month,Dir)
		for item in data:
			days[item.AccTime.day][1] += 1
		return days,len(data)

	def _month(self,Month,Dir):
		#month format:2011-12
		from datetime import datetime
		year = int(Month.split('-')[0])
		month = int(Month.split('-')[1])
		ms = datetime.strptime("%s-%s 00:00:00" % (Month,"01"), "%Y-%m-%d %H:%M:%S")
		me = datetime.strptime("%s-%s 00:00:00" % (Month,days_in_month(year,month)), "%Y-%m-%d %H:%M:%S")
		return self._between(Dir,"AccTime",ms,me)
	