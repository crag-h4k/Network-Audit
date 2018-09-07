#!/usr/bin/python
#execute as root
from time import time
from nmap import PortScanner
from datetime import datetime
from cleaner import clean
def scan(subnet,filename):
    raw_timestamp = time()
    timestamp = datetime.fromtimestamp(raw_timestamp).strftime('%H:%M:%S %d-%m-%Y')
    nm = PortScanner()
    #subnet = '192.168.' + str(start) + '.0/24'
    init_msg = 'Starting on: ' + subnet + ' ' + timestamp + '\n'	
    success_msg = 'Successfully scanned '+ subnet + ' ' + timestamp + '\n'
    error_msg = 'Some problem scanning ' + subnet + ' ' + timestamp + '\n'

        #nmap -A -Pn 192.168.192.0/24
    print(init_msg)
    nm.scan(hosts=subnet, arguments='-A -sV')
    to_csv = nm.csv()

    with open(filename, 'a+') as f:
        f.write(to_csv)
        f.close()
        print(success_msg,to_csv)
        #clean(filename)		

subnet = '192.168.185.101-120' 
filename = 'scan.csv'
scan(subnet,filename)

