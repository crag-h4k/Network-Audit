#!/usr/bin/python
#execute as root
from time import time
from nmap import PortScanner
from datetime import datetime

start = 192
end = 255

while start <= end:
	raw_timestamp = time()
	timestamp = datetime.fromtimestamp(raw_timestamp).strftime('%Y-%m-%d %H:%M:%S')

	nm = PortScanner()
	subnet = '192.168.' + str(start) + '.0/24'
	print('!!! Starting on:',ip_range,'!!!',timestamp)
	
	try:
		#nmap -A -Pn 192.168.192.0/24
		nm.scan(hosts=subnet, arguments='-A')
		to_csv = nm.csv()

		print('Successfully scanned',subnet,timestamp)
		print(to_csv)
		with open('net_scan.csv', 'a+') as f:
			f.write(timestamp,'\n',to_csv)
			f.close()
	except:
		print('SOME PROBLEM WITH SCAN OF', subnet, timestamp)

	start += 1
