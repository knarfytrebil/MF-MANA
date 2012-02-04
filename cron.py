from modules.Log import Logs
from modules.Balance import Balance
from modules.User import User
from modules.Page import Page
from modules.Record import Record

StatusDict = {0:'arrears',1:'paid'}

log = Logs('AccessLog')

balance = Balance('flame_balance','local')
user = User('flame_user','local')
page = Page('flame_page','local')
record = Record('flame_record','local')

USERS = user._get(status='paid')

for u in USERS:
			import datetime
			d = datetime.date.today()
			strd = datetime.datetime.strftime(d, "%Y-%m-%d")
			strm = datetime.datetime.strftime(d, "%Y-%m")
			PageList = u.list.split(',')
			day_balance = 0
			for item in PageList:
				price = page._get(name=item)[0].click
				day_balance = log._hours(strd,"/%s/" % item)[1] * price * -1
				hours = log._hours(strd,"/%s/" % item)[0]
				days = log._days(strm,"/%s/" % item)[0]
				for hour in hours:
					h = hour[0]
					v = hour[1]
					record.renew(h,strd,item,v,'day')
				for day in days:
					d = day[0]
					v = day[1]
					record.renew(d,strm,item,v,'month')
				if day_balance != 0:
					balance.out(u.id,strd,day_balance,item)
			s = 0
			l = balance.Left(u.id)
			t = balance.Total(u.id)
			used = t - l
			rate = used / t * 100
			if l > 0:s = 1
			user._set(u.id,status=StatusDict[s],balance_left=l, balance_total=t, balance_used = used, balance_rate = rate)