#!/usr/bin/python3

import string
import secrets
import argparse
import sys
from termcolor import colored

parser = argparse.ArgumentParser(prog="password_gen", description="Password Generator")
parser.add_argument("-l", "--length", help="length of the password", required=True)
args = parser.parse_args()

print(colored("Only for Educational Purposes\n", "red"))
print(colored("USERNAME ENUMERATOR BY @s3rd4r308\n", "green"))

length = args.length

lowercases = string.ascii_lowercase
uppercases = string.ascii_uppercase
digits = string.digits
punctuations = string.punctuation

chars = lowercases + uppercases + digits + punctuations

password = ""

for i in range(int(length)):
	print(colored("[*] Generating The Password...\n", "blue"))
	password += "".join(secrets.choice(chars))

print(colored("[+] Password Generated", "green"))
print(colored(f"[+] Password: {password}", "green"))
