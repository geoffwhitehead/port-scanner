# Ref: Followed tutorial found on http://null-byte.wonderhowto.com/how-to/sploit-make-python-port-scanner-0161074/ by Sergeant Sploit

#!usr/bin/env/python
from socket import *
import sys, time
from datetime import datetime

host = ''
max_port = 50000
min_port = 1


def scan_host(host, port, r_code=1):
    try:
        s = socket(AF_INET, SOCK_STREAM)  # set up a socket

        code = s.connect_ex((host, port))  # connect to target using socket

        if code == 0:  # if the connection attempt is successful...
            r_code = code  # log result then close the connection
            s.close()
    except Exception, e:
        print(e)

    return r_code  # return the connection result

try:
    host = raw_input("[*} Enter the target host address: ")
except KeyboardInterrupt:
    print("\n\n[*] User requested interrupt.")
    print("[*] Application shutting down")
    sys.exit(1)

#host_ip = gethostbyname(host)  # returns the hosts ip address based on a URL
#print("Host: " + host_ip)

for port in range(min_port, max_port):  # for each of the ports in the range do...
    #print(port)
    try:
        response = scan_host(host, port)  # scan
        if response == 0:  # if response is 0... port is open
            print("[*] Port %d: open" % (port))
    except Exception, e:
	print(e)
    except KeyboardInterrupt:
        print("\n\n[*] User requested interrupt.")
        print("[*] Application shutting down")
        sys.exit(1)

print("Complete")
