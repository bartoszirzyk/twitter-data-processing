
import re
import urllib2

def findRedirection(url):
	req = urllib2.Request(url= url)
	resp = urllib2.urlopen(req, timeout=3)
	return resp.geturl()

def filterURLs(tweet):
	return  [findRedirection(x) for x in re.findall(r'(https?://[^\s]+)', tweet)] 


output = []
test = "https://www.google.com dsadsanfajsdnfdlasnf http://www.wp.pl"
result = filterURLs(test)
print(result)