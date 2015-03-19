import urllib2,urllib,cookielib
import time,thread

class Basic(object):

	def __init__(self,url,datas,keyword=None):
		self.url = url
		self.keyword = keyword
		self.datas = datas
		self.enable = True
		self.cookie = cookielib.MozillaCookieJar("Cookie.txt")
		self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))

	def InitOpener(self):
		urllib2.install_opener(self.opener)
		req = urllib2.Request(self.url,self.datas)
		req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:35.0) Gecko/20100101 Firefox/35.0')
		urlfile = urllib2.urlopen(req)
		#urlfile = urllib2.urlopen(self.url,self.datas)
		time.sleep(2)
		self.cookie.save()

	def RROpen(self,search_url):
		urlfile = urllib2.urlopen(search_url)
		fName = time.strftime('%Y_%m_%d_%H_%M_%S') + '.html'
		f = file(fName,'w')
		f.write(urlfile.read())
		f.close()

if __name__=="__main__":
	datas = urllib.urlencode({'email':'cbl198903@163.com','password':'cbl1989'})
	renren = Basic('http://www.renren.com/ajaxLogin',datas)
	renren.InitOpener()
	renren.RROpen("http://www.renren.com/859627679/profile")
