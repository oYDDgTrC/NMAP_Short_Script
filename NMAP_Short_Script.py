#!/bin/bash

import subprocess
import ipaddress
import socket
import struct 

hosts = input("Enter IPs to Nmap scan separated by ',' : ")
string_array = []
IP_array = []

string_array = hosts.split(",")
for host in string_array:
	IP_array.append(ipaddress.ip_address(host))
# Uses subprocess to call regular CLI commands. Subprocess has no return value by default. 
def NmapPingTraceroute (IP_List):
	for IP in IP_List:
		print ("\n" + IP)
		subprocess.call(["nmap", "-sn" , "-PO[1]" , IP])
		subprocess.call(["nmap", "-sn" , "--traceroute" , IP]) 
		
def NmapFullPortScan (IP_List):
	for IP in IP_List:
		print ("\n" + IP)
		subprocess.call(["nmap", "-v", "-A", "T5", "-sS", "-sU", "-p0-65535", IP])

def BaselineLargeNetworks(IP_List):
	for IP in IP_List:
		print ("\n" + IP)
		subprocess.call(["nmap", "-Pn", "-sU" , "--top-ports 500" , "-PO[1]" , IP])
		subprocess.call(["nmap", "-Pn", "-sT" , "-PO[1]" , IP])

print ("***Nmap Scan***")
print ("(1) = Ping / Traceroute\n")
print ("(2) = Standard Full Port Scan\n")
print ("(3) = Baseline Large Networks Scan \n")
Scan_choice = input("What type of scan would you like to perform? :  \n") 

if Scan_choice == "1":
	NmapPingTraceroute(string_array)
	break
elif Scan_choice == "2":
	NmapFullPortScan(string_array)
	break
elif Scan_choice == "3":
	BaselineLargeNetworks(string_array)
	break
else:
	print ("No choice was made... ")

print ("Have a nice day!!!!")
	
