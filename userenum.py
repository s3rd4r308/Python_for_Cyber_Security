#!/usr/bin/python3

import argparse
import requests
import sys
from termcolor import colored

parser = argparse.ArgumentParser(prog='userenum', description='Username Enumerator for Login Pages')
parser.add_argument('--url', '-u', help='url of the login page', required=True)
parser.add_argument('--list', '-l', help='username list', required=True)
args = parser.parse_args()

print(colored("USERNAME ENUMERATOR BY @s3rd4r308\n", "green"))
print(colored("Only for Educational Purposes\n", "red"))

url = args.url
userList = args.list

file = open(userList, "r").readlines

for i in file:
	header = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:50.0) Gecko/20100101 Firefox/50.0", "Content-Type" : "application/x-www-form-urlencoded", "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Encoding" : "gzip, deflate, br", "Accept-Language" : "en-US,en;q=0.5"}
	cookie = {"PHPSESSID" : ""} #if the web server generates it for you (the parameter should be controlled)
	user = i.strip()
	data = {"username" : user, "password" : "just_a_random_string"} #these username and password parameters should be controlled either because it can change server to server
	r = requests.post(url, data=data, cookies=cookie, headers=header)
	#do not forget to check the login page is specifically saying that there is not a username like this or else it is no going to work
	if "Invalid" or "invalid" or "not found" or "Not Found" in r.text:
		print(colored(f"[+] User Found : {user}", "green"))
	else:
		print(colored("[-] Could not find any potential user", "red"))
		print("\n[*] Exitting...")
		sys.exit()
