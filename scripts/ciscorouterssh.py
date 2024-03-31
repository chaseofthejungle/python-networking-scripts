from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.5.180',
    'username': 'sampleadmin',
    'password': 'samplepass'
}
 
ssh_connection = ConnectHandler(**device) 

# display devices configed on router, their IP addresses, and operational statuses
devinfo = ssh_connection.send_command('show ip int brief')
print(devinfo)
 
ssh_connection.disconnect()
