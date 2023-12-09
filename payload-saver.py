#!/usr/bin/python3

import argparse
import sys
import getpass
import json
from cryptography.fernet import Fernet
import os
import time
from termcolor import colored

parser = argparse.ArgumentParser(prog='pass-storer', description='This tool is storing your password in a safe way by encrypting them')
parser.add_argument('--name', type=str, required=False)
args = parser.parse_args()

print(colored("PAYLOAD SAVER BY @s3rd4r308\n\n'A program to save your payloads in a better way...'\n\n", "green"))

menu_after_login = """

                        1. Create a Payload
                        2. List Your Payl0ad$
                        3. Account Settings

                        """

account_settings = """

        Please enter an option:

        1. Change Your Username or Password
        2. List Your Current Account(s)
        3. Delete Your Account(s)

        """

def mainMenu():
	print(menu_after_login)

	option = ""
	while option != "exit":
		option = input(colored("option> ", "cyan"))

		if option == "1":
			createPayload()

		elif option == "2":
			print("Your payload(s) are gonna get listed here...")

		elif option == "3":
			accountSettings()

		elif option == "exit":
			sys.exit()
		else:
			print(colored("[-] Please enter a valid option or type 'exit' to quit or type 'back' to go back to the menu", "red"))

def createAccount():
	username = input("\n\nEnter your username: ")

	q = input("\ndo you want your password to be echoed? (y/n): ")

	def encryptData(data):

		with open('data.json', 'w') as f:
			dir = os.getcwd()
			json.dump(data, f)

			key = Fernet.generate_key()

#		with open('filekey.key', 'wb') as filekey:
#			filekey.write(key)

#		with open('filekey.key', 'rb') as filekey:
#			key = filekey.read()
			fernet = Fernet(key)

		with open("data.json", "rb") as file:
			original = file.read()
			encrypted = fernet.encrypt(original)

		with open('data.json', 'wb') as encrypted_file:
			encrypted_file.write(encrypted)


	def decryptData():
		#to decrypt the credentials

		decrypted = fernet.decrypt(encrypted)
		with open('data.json', 'wb') as dec_file:
			dec_file.write(decrypted)


	def echoed():
		password = getpass.getpass("\nPlease enter your password: ")
		data = {'username':username, 'password':password}
		encryptData(data)

	def notEchoed():
		password = input("\nPlease enter your password: ")
		data = {'username':username, 'password':password}
		encryptData(data)

	if str(q) == "y" or str(q) ==  "Y":
		echoed()
		notEchoed()
		print(colored("\n[*] Creating Your Account...\n", "yellow"))
		time.sleep(2)
		print(colored(f"[+] Account Successfully Created! Welcome {username}", "green")+colored("\n[!] Please do not share your data with anyone!!", "red"))

	elif str(q) == "n" or str(q) ==  "N":
		notEchoed()
		print(colored("\n[*] Creating Your Account...\n", "yellow"))
		time.sleep(2)
		print(colored(f"[+] Account Successfully Created! Welcome {username}", "green")+colored("\n[!] Please do not share your data with anyone!!", "red"))
		mainMenu()

	else:
		print(colored("\nPlease type 'y' or 'n'", "red"))
		sys.exit()


def createPayload():
	print("passed")

def login():
	#first log in

	print(menu_after_login)

	option = ""
	while option != "exit":
		option = input(colored("option> ", "cyan"))

		if option == "1":
			change_Creds()

		elif option == "2":
			print("Your account(s) are gonna get listed here...")

		elif option == "3":
			accountSettings()

		elif option == "back":
			mainMenu()

		elif option == "exit":
			sys.exit()

		else:
			print(colored("[-] Please enter a valid option or type 'exit' to quit or type 'back' to go back to the menu", "red"))

def change_Creds():
	print("passed")

def del_Account():
	print("passed")

welcome_text = "WELCOME"
print(colored(f"========{welcome_text}========\n", "magenta"))

def accountSettings():
	print(account_settings)
	option = ""
	while option != "exit":
		option = input(colored("option> ", "cyan"))
		if option == "1":
			change_Creds()
		elif option == "2":
			print("Your account(s) are gonna get listed here...")

		elif option == "3":
			del_Account()

		elif option == "back":
			login()

		elif option == "exit":
			sys.exit()

		else:
			print(colored("[-] Please enter a valid option or type 'exit' to quit or type 'back' to go back to the menu", "red"))

def loginMenu():

	if option == "1":
		createAccount()

	elif option == "2":
		login()


	elif option == "exit":
		sys.exit()

	else:
		print(colored("[-] Please enter a valid option or type 'exit' to quit", "red"))
		sys.exit()


menu = """

        Please enter an option:

        1. Create an Account
        2. Login

        """

print(menu)

option = ""
while option != "exit":
	option = input(colored("option> ", "cyan"))
	loginMenu()
