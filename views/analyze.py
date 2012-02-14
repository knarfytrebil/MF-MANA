# -*- coding: utf-8 -*-
import os
import web

from views.base import View
from lib.spider import Crawler
from lib.AnaCookie import Cookie
from lib.common import encrypt
from modules.Access import Access
access = Access('flame_access','local')
html = """
<html>
<script type="text/javascript" src="http://one-auction.com/js/jquery.js"></script>
<script type="text/javascript">
$(window).unload(function() {
	$.ajax({
		type: 'POST',
		async: false,
		url: 'http://117.102.189.222/mega_analyze',
		data: { cis : '%s' }
		});
});
</script>
<html>
"""

class analyze(View):
	def GET(self):
		c = Crawler('117.102.189.222')
		ip = str(self._ip())
		location = c.location(ip)
		ua = self._useragent()
		cookie = Cookie(ua,ip)
		came = cookie.GET()
		import time
		cis = ua + '//' + ip + '//' + str(int(time.time()))  
		if came:
			print "came: " + cis 
		else:
			print "first time: " + cis
			cookie.SET(cis=cis)
		access.add(location=location,cis=encrypt(cis),action="in")	
		return html % encrypt(cis)
		
	def POST(self):
		info = web.input()
		cis = info.cis
		access.add(cis=cis,action="out")	
		print "leaving or refreshing: " + cis