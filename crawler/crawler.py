import urllib2,urllib,cookielib
import time,thread

class basic_handler(object):

	def __init__(self,url,datas,user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:35.0) Gecko/20100101 Firefox/35.0',keyword=None):
		self.url = url
		self.keyword = keyword
		self.datas = datas
		self.user_agent = user_agent
		self.enable = True
		self.cookie = cookielib.MozillaCookieJar("Cookie.txt")
		self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))

	def initOpener(self):
		urllib2.install_opener(self.opener)
		req = urllib2.Request(self.url,self.datas)
		req.add_header('User-Agent',self.user_agent)
		urlfile = urllib2.urlopen(req)
		time.sleep(2)
		self.cookie.save()

	def saveHTML(self,search_url):
		urlfile = urllib2.urlopen(search_url)
		fName = time.strftime('%Y_%m_%d_%H_%M_%S') + '.html'
		f = file(fName,'w')
		f.write(urlfile.read())
		f.close()

	def get_cookie(self):
		print self.cookie