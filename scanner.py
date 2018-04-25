#!/usr/bin/python
from nmap import PortScanner
from os import system
#run as sudo

#start = input('Define x of 192.168.x.0/24 for first subnet:\t')
#end = input('Define x of 192.168.x.0/24 for last subnet:\t')
#file_loc = input('Define path of scan destination\nex. ~/Documents/scan.csv\nPath:\t')

subnet = 192

while subnet <= 255:
	
	nm = PortScanner()
	cidr = '192.168.' + str(subnet) + '.0/24'
	print('!!! Starting on:',cidr,'!!!')
	
	try:
		nm.scan(hosts=cidr,arguments='-A -Pn')
		to_csv = nm.csv()

		print('!!! Successfully scanned',cidr,'!!!')
		system("beep")
	
		print(to_csv)
		with open('net_scan.csv', 'a+') as f:
			f.write(to_csv)
			f.close()
	except:
		print('!!! SOME PROBLEM WITH SCAN OF',cidr,'!!!')

	subnet += 1
