# -*- coding: utf-8 -*-
def striptag(value):
	import re
	"""Returns the given HTML with all tags stripped."""
	result = re.sub(r'<[^>]*?>', '', value.decode('utf8','ignore')+'>')
	result = re.sub(r'&[^>]*?;', '', result)
	if result[-1:] == '>':
		return result[:-1]
	else:
		return result

#fix the problem that web.py cannot add html attribute 'class'
def add_class(form,value):
	from lib.BeautifulSoup import BeautifulSoup
	i = BeautifulSoup(form).input
	i['class'] = value
	return str(i)


def getPageNum(CurrPage,LastID,PageLength):
	CurrPage += 1
	LastPage = (LastID/PageLength) + 1
	PrevPage = CurrPage - 1
	NexPage = CurrPage + 1
	if NexPage > LastPage:NexPage = LastPage + 1
	if PrevPage < 2:PrevPage = 2
	PageList = range(PrevPage - 1,NexPage)
	return {'PageList':PageList,'LastPage':LastPage,'PrevPage':PrevPage-1,'NexPage':NexPage-1}

def split(value,separator):
	return value.split(separator)

def boundary(year):
	from datetime import date
	start = date(year,1,1)
	end = date(year,12,31)
	return (start,end)

def strfmonth(month):
	mDict = {1:'JAN',2:'FEB',3:'MAR',4:'APR',5:'MAY',6:'JUN',7:'JUL',8:'AUG',9:'SEP',10:'OCT',11:'NOV',12:'DEC'}
	return mDict[month]

def encrypt(s):
	from base64 import urlsafe_b64encode as encode
	b64 = encode(s)
	r = []
	for i in b64:
		r.append(i)
	r.reverse()
	return "".join(r)

def decrypt(s):
	from base64 import urlsafe_b64decode as decode
	r = []
	for i in s:
		r.append(i)
	r.reverse()
	return decode("".join(r))

def DayAndMonth():
	import datetime
	d = datetime.date.today()
	strd = datetime.datetime.strftime(d, "%Y-%m-%d")
	strm = datetime.datetime.strftime(d, "%Y-%m")
	return strd,strm

def DateToTimeStamp(date):
	import datetime
	import time
	x = datetime.datetime.strptime(date,"%Y-%m-%d")
	x = x.timetuple()
	return int(time.mktime(x))*1000 - 36000000

def HourToTimeStamp(date):
	import datetime
	import time
	x = datetime.datetime.strptime(date,"%Y-%m-%d %H:%M:%S")
	x = x.timetuple()
	return int(time.mktime(x))*1000 - 36000000