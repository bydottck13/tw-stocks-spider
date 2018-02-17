#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
from datetime import datetime
from twstocklists import stock_ex_list
import sys, time

mops_url = 'http://mops.twse.com.tw/mops/web/ajax_t146sb05'
twse_url = 'http://isin.twse.com.tw/isin/C_public.jsp?strMode=2'
tej_url = 'http://www.tej.com.tw/webtej/doc/uid.htm'
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
	'TYPEK' : 'all' }
stocks_list = {**stock_ex_list}

def update():
	#print("Starting to parser ids", datetime.now().isoformat(timespec='minutes'))
	with urllib.request.urlopen(tej_url) as response:
		ids_html = response.read()
		#print("Finished to parser ids", datetime.now().isoformat(timespec='minutes'))
		ids_soup = BeautifulSoup(ids_html, 'html.parser')
		trs = ids_soup.findAll('tr')
		print(trs[0].findAll('td')[0])
		print(trs[1].findAll('td')[0])
		"""for tr in trs:
			first_td_tag = tr.find('td')
			if first_td_tag.text.strip() != '1101　台泥':
				continue
			print(first_td_tag.text)"""

def gather():
	for stock_id, stock_name in stocks_list.items():
		print("Stock id is", stock_id, stock_name)
		post_request['co_id'] = stock_id

		post_data = urllib.parse.urlencode(post_request).encode()
		with urllib.request.urlopen(mops_url, data=post_data) as response:
			print('Response Code:', response.getcode())
			stock_html = response.read()
			if len(stock_html) < 500:
				print('No retrieved any data...')
				#time.sleep(30)
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

if __name__ == "__main__":
	if len(sys.argv) < 1:
		print('Usage: python3 twstocksspider.py [update|gather]')
		exit()
	if sys.argv[1] == 'update':
		update()
	elif sys.argv[1] == 'gather':
		gather()

