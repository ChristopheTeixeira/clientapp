import psutil
import json
import socket

ips = ""
for nic, addrs in psutil.net_if_addrs().items():
    for addr in addrs:
        if(socket.AF_INET is addr.family and "127.0.0.1" not in addr.address):
            ips += (addr.address)

jsondict = dict()
jsondict["cpu"] = psutil.cpu_percent(interval=1)
jsondict["mem"] = psutil.virtual_memory().percent
jsondict["disk"] = psutil.disk_usage('/').percent
jsondict["ips"] = ips



print(json.dumps(jsondict))




