# -*- coding: utf-8 -*-
import os
import web

from views.base import View
from lib.spider import Crawler
from lib.AnaCookie import Cookie
from lib.common import encrypt

html = """
<html>
<script type="text/javascript" src="http://one-auction.com/js/jquery.js"></script>
<script type="text/javascript">
$(window).unload(function() {
	$.post("http://117.102.189.222/mega_analyze", { cis: "%s" } );
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
		cis = ua + ip
		if came:
			pass
		else:
			cookie.SET(cis=cis)
		return html % encrypt(cis)
		
	def POST(self):
		info = web.input()
		print info
		return info