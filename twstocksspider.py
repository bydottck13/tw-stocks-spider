import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
from datetime import datetime

mops_url = 'http://mops.twse.com.tw/mops/web/ajax_t146sb05'
twse_url = 'http://isin.twse.com.tw/isin/C_public.jsp?strMode=2'
post_request = {'encodeURIComponent' : '1',
	'step' : '1',
	'firstin' : '1',
	'off' : '1',
	'keyword4' : '',
	'code1' : '',
	'TYPEK2' : '',
	'checkbtn' : '',
	'queryName' : 'co_id',
	'inpuType' : 'co_id',
	'TYPEK' : 'all',
	'co_id' : '' }
stocks_list = ['2230', '2357', '2379', '2380', '2317']

#print("Starting to parser ids", datetime.now().isoformat(timespec='minutes'))
with urllib.request.urlopen(twse_url) as response:
	ids_html = response.read()
	#print("Finished to parser ids", datetime.now().isoformat(timespec='minutes'))
	ids_soup = BeautifulSoup(ids_html, 'html.parser')
	trs = ids_soup.findAll('tr')
	for tr in trs:
		first_td_tag = tr.find('td')
		if first_td_tag.text.strip() != '1101　台泥':
			continue
		print(first_td_tag.text)


for stock in stocks_list:
	print("Stock id is", stock)
	post_request['co_id'] = stock

	post_data = urllib.parse.urlencode(post_request).encode()
	with urllib.request.urlopen(mops_url, data=post_data) as response:
		stock_html = response.read()
		stock_soup = BeautifulSoup(stock_html, 'html.parser')
		income_list = list()

		tables = stock_soup.findAll('table')
		for table in tables:
			first_td_tag = table.find('tr').find('td')
			if first_td_tag.text != '本年迄今累計營收':
				continue
			# Found the income table
			trs = table.findAll('tr')
			for i in range(0, len(trs), 2):
				title_tds = trs[i].findAll('td')
				income_tds = trs[i+1].findAll('td')
				if len(title_tds) != len(income_tds):
					continue
				month_list = list()
				for j in range(len(title_tds)):
					income_tuple = (title_tds[j].text, income_tds[j].text.strip())
					month_list.append(income_tuple)
				income_list.append(month_list)

		for month_income in income_list[::-1]:
			print(month_income)
		print("")
