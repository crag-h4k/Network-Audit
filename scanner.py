#!/usr/bin/python
from nmap import PortScanner
#run as root

subnet = 192

while subnet <= 255:
	
	nm = PortScanner()
	ip_range = '192.168.' + str(subnet) + '.0/24'
	print('!!! Starting on:',ip_range,'!!!')
	
	try:
		#nmap -A -Pn 192.168.192.0/24
		nm.scan(hosts=ip_range, arguments='-A')
		to_csv = nm.csv()

		print('Successfully scanned',ip_range)
		print(to_csv)
		with open('net_scan.csv', 'a+') as f:
			f.write(to_csv)
			f.close()
	except:
		print('SOME PROBLEM WITH SCAN OF',ip_range)

	subnet += 1
