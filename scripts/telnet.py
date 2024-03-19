import telnetlib

# This is just an example! Please use secure usernames and passwords.
HOST = "192.168.58.4"
user = "administrator"
password = "password"

tn123 = telnetlib.Telnet(HOST)
tn123.read_until(b"User ID: ")
tn123.write(user.encode("utf8") + b"\n")
tn123.read_until(b"Password: ")
tn123.write(password.encode("utf8") + b"\n")
tn123.write(b"show clock detail\n") # Confirms NTP timestamp.

print(tn123.read_all().decode("utf8"))
