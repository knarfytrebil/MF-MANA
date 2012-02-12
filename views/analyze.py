# -*- coding: utf-8 -*-
import os
import web

from views.base import View
from lib.spider import Crawler
from lib.AnaCookie import Cookie

class analyze(View):
	def GET(self):
		c = Crawler('117.102.189.222')
		ip = str(self._ip())
		location = c.location(ip)
		ua = self._useragent()
		cookie = Cookie(ua,ip)
		came = cookie.GET()
		if came:
			return "you came before:" + location + " " + ua
		else:
			return "you never came:" + location + " " + ua