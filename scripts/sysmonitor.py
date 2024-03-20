import psutil

# Retrieve CPU, memory, and disk usage
cpu_use = psutil.cpu_percent()
memory_use = psutil.virtual_memory().percent
disk_use = psutil.disk_usage("/").percent

# Retrieve input/output data rates for all devices on a network
io_counters = psutil.net_io_counters(pernic=True)
for device, counters in io_counters.items():
    print(f"Network Device {device}:")
    print(f"  rate for transmitted bytes (TX): {counters.bytes_sent}")
    print(f"  rate for received bytes (RX): {counters.bytes_recv}")

# Retrieve available connections and list them to screen
connections = psutil.net_connections()
for connection in connections:
    print(f"{connection.laddr} <-> {connection.raddr} ({connection.status})")

# Output data to screen
print(f"CPU in use: {cpu_use}%")
print(f"Memory in use: {memory_use}%")
print(f"Disk in use: {disk_use}%")
