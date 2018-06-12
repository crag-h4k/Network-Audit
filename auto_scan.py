#!/usr/bin/python3
#execute as root
from time import time
from nmap import PortScanner
from datetime import datetime
from cleaner import clean
from time import sleep 

def auto_scan_host():
	interval = 300
	filename = '202_44.csv'
	addr= '192.168.202.44'
	
	while True:
		raw_timestamp = time()
		timestamp = datetime.fromtimestamp(raw_timestamp).strftime('%H:%M:%S %d-%m-%Y')
		nm = PortScanner()
		
		init_msg = 'Starting on: ' + addr + ' ' + timestamp + '\n'	
		success_msg = 'Successfully scanned '+ addr + ' ' + timestamp + '\n'
		error_msg = 'Some problem scanning ' + addr + ' ' + timestamp + '\n'

		try:
			print(init_msg)
			nm.scan(hosts=addr, arguments='-A')
			to_csv = nm.csv()

			with open(filename, 'a+') as f:
				f.write(to_csv)
				f.close()
			print(success_msg,to_csv)
			clean(filename)
			sleep(interval)

		except KeyboardInterrupt:
			clean(filename)
			break
			
		except:
			with open(filename, 'a+') as f:
				f.write(error_msg)
				f.close()
				
			clean(filename)
			print(error_msg)

auto_scan_host()
