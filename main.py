import os
import sys
import web

curdir = os.path.dirname(__file__)
sys.path.append(curdir)

from views.index import index
from views.user import user
from views.analyze import analyze

web.config.debug = True

urls = (
	'/','index',
	'/user/(.*)','user',
	'/mega_analyze','analyze'
)

application = web.application(urls, globals()).wsgifunc()