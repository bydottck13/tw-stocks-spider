import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = 'http://mops.twse.com.tw/mops/web/ajax_t146sb05'
postrequest = {'encodeURIComponent' : '1',
	"step" : "1",
	"firstin" : "1",
	"off" : "1",
	"keyword4" : "",
	"code1" : "",
	"TYPEK2" : "",
	"checkbtn" : "",
	"queryName" : "co_id",
	"inpuType" : "co_id",
	"TYPEK" : "all",
	"co_id" : "9943" }

data = urllib.parse.urlencode(postrequest).encode()
html = urllib.request.urlopen(url, data=data).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('td')
for tag in tags:
	print(tag.text)