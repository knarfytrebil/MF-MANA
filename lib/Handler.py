import urllib2
import httplib
import socket
import copy
import mechanize
import mechanize._response

# class BindableHandler(mechanize.BaseHandler):
#     """docstring for BindableHandler"""
#     def __init__(self, customized_handler):
#         self._customized_handler = customized_handler
#     def http_open(self, req):
#         """docstring for http_open"""
#         return mechanize._response.closeable_response(self._customized_handler.do_open(req))
        
# def make_http_handler():
#     """docstring for make_http_handler"""
#     customized_handler = BindableHTTPHandler()
#     return BindableHandler(customized_handler)

class BindableHTTPConnection(httplib.HTTPConnection):
    def connect(self):
        """Connect to the host and port specified in __init__."""
        self.sock = socket.socket()
        self.sock.bind((self.source_ip, 0))
        if isinstance(self.timeout, float):
                self.sock.settimeout(self.timeout)
        self.sock.connect((self.host,self.port))

def BindableHTTPConnectionFactory(source_ip):
    def _get(host, port=None, strict=None, timeout=0):
        bhc=BindableHTTPConnection(host, port=port, strict=strict, timeout=timeout)
        bhc.source_ip=source_ip
        return bhc
    return _get

class BindableHTTPHandler(urllib2.HTTPHandler):
    def http_open(self, req):
        return self.do_open(BindableHTTPConnectionFactory(ip_addr), req)

class BindableBrowser(mechanize.Browser):
    """docstring for BindableBrowser"""
    handler_classes = copy.copy(mechanize.Browser.handler_classes)
    handler_classes["http"] = BindableHTTPHandler
#opener = urllib2.build_opener(BindableHTTPHandler)
#opener.open("http://google.com/").read() # Will fail, 127.0.0.1 can't reach google.com.

#ip_addr = '192.168.11.119'
# br = BindableBrowser()
# print br.open("http://python.org")