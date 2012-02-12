# -*- coding: utf-8 -*-
import web
from lib.common import encrypt
from lib.common import decrypt

COOKIE_EXPIRE = 0
COOKIE_DOMAIN = 'http://one-auction.com/'

class Cookie:
	"""
	docstring for CookieSet
	read, write the cookie
	"""
	def __init__(self,ua,ip):
		self.ua = ua
		self.ip = ip

	def GET(self):
		"""set cookie"""
		try:
			"getting cookie"
			uis = decrypt(web.cookies().uis).split(',')
			username = uis[0]
			password = uis[1]
			BAuth = self.BasicAuth(username,password)
			if BAuth:
				return BAuth
			return False
		except Exception,e:
			"if there is no cookie"
			return False
	
	def SET(self,COOKIE_EXPIRE=COOKIE_EXPIRE,**kwargs):
		for key in kwargs.keys():
			web.setcookie(key,encrypt(kwargs[key]),COOKIE_EXPIRE)