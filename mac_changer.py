#!/usr/bin/env python

import subprocess

#Replace value with device to change
interface = "wlan0"

#Replace value with desired MAC Address
new_mac = "00:11:22:33:44:66"

print("[+] Changing MAC Address for " + interface + " to " + new_mac)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)