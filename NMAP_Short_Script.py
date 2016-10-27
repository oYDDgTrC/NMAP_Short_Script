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


def NmapPingTraceroute (IP_List):
	for IP in IP_List:
		print (IP)
		print (subprocess.call(["nmap", "-sn" , "-PO[1]" , IP])) 
		print (subprocess.call(["nmap", "-sn" , "--traceroute" , IP])) 

def Baseline (IP_List):
	for IP in IP_List:
		print ("\n" + IP)
		print (subprocess.call(["nmap", "-Pn", "-p" "U:0-65535,T:0-65535" , "-PO[1]" , IP])) 
def BaselineLargeNetworks(IP_List):
	for IP in IP_List:
		print ("\n" + IP)
		print (subprocess.call(["nmap", "-Pn", "-p T:0-65535", "-sU" "--top-ports 500" , "-PO[1]" , IP])) 

print ("***Nmap Scan***")
print ("(1) = Ping / Traceroute\n")
print ("(2) = Baseline Scan \n")
print ("(3) = Baseline Large Networks Scan \n")
Scan_choice = input("What type of scan would you like to perform? :  ") 

if Scan_choice == "1":
	NmapPingTraceroute(string_array)
	print ("Have a nice day!!!!")
elif Scan_choice == "2":
	Baseline(string_array)
	print ("Have a nice day!!!!")
elif Scan_choice == "3":
	BaselineLargeNetworks(string_array)
	print ("Have a nice day!!!!")
else:
	print ("No choice was made... ")