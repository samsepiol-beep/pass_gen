#!/usr/share/python3

# Author Samsepiol

import string
import random

# defines the length of the password
long = int(input("[!] Enter password length: "))

# generates the characters to use in the password
caracter = string.ascii_letters + string.digits

# generates the password with the specified length
password = "".join(random.choice(caracter) for i in range(long))

# print the password
print(f"[+] Generated password is: {password}")
