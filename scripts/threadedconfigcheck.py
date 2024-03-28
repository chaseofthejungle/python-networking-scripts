from datetime import datetime
from netmiko import ConnectHandler
from threading import Thread

beginTime = datetime.now()
allThreads = []

def show_routers(ip):
device = ConnectHandler(device_type = 'cisco_ios', ip = ip, username = 'testuser', password = 'testpass')
commandOutput = device.send_command("show run | in hostname")
commandOutput = commandOutput.split(" ")
hostname = commandOutput[1]
print ("\nDevice Hostname for IP Address %s is: %s" % (ip, hostname))

for n in range(1, 5):
ip = "192.168.20.{0}".format(n)
t = Thread(target = show_routers, args = (ip,))
t.start()
allThreads.append(t)

for t in allThreads:
t.join()

print ("\nTotal Time to Execute Device Checks: ")
print(datetime.now() - beginTime)
