import os, ipaddress 
# Script evaluates if an IP address is valid.

os.system('cls')
 
while True:
    ip = input('Enter an IP Address: ')
    try: 
        print(ipaddress.ip_address(ip))
        print('Valid IP Address!')
    except: 
        print('Invalid IP Address.')
    finally: 
        if ip.lower() =='q':
           break
