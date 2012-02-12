#!/usr/bin/env python
# encoding: utf-8
"""
taker.py

Created by 姚 远 on 2011-03-29.
Copyright (c) 2011 Lapin. All rights reserved.
"""

import lib.Handler as BrowserFactory
from lib.BeautifulSoup import BeautifulSoup
import os

class Crawler:
	"""docstring for Crawler"""
	def __init__(self, ip):
		BrowserFactory.ip_addr = ip
		self.br = BrowserFactory.BindableBrowser()
		self.current_page = None
		self.br.set_handle_equiv(True)
		self.br.set_handle_redirect(True)
		self.br.set_handle_referer(True)
		self.br.set_handle_robots(False)
		self.br.addheaders = [('User-agent','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.1.1-1.fc9 Firefox/3.0.1')]

	def location(self,ip):
		try:
			self.current_page = self.br.open('http://www.114best.com/ip/114.aspx?w=%s' % ip)
		except Exception:
			return "Earth"
		soup = BeautifulSoup(self.current_page)
		lo = soup.findAll('div', { "id" : "output" })[0].findAll('b')[1].text.encode('utf-8','ignore')
		return lo