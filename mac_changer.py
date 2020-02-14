#!/usr/bin/env python

import subprocess

#Replace value with device to change
interface = input("interface > ")

#Replace value with desired MAC Address
new_mac = input("new MAC > ")

print("[+] Changing MAC Address for " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
