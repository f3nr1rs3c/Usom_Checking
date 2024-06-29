#!/usr/bin/env python3
import socket
import os
from colorama import init, Fore
from pyfiglet import Figlet

# Initialize Colorama
init(autoreset=True)

os.system("apt-get install figlet")
os.system("clear")

f = Figlet(font='slant')
print(Fore.BLUE + f.renderText('Usom Check'))
print(Fore.RED + "          | - | Made By : F3NR1R - Cyber Security | - |         ")

data_file = r"C:\Users\Admin\Desktop\Usom\usom-list.txt"

if not os.path.isfile(data_file):
    print(Fore.RED + f"Error: {data_file} not found!")
    exit(1)

site_search = input("Enter the website: ")
with open(data_file, "r", encoding="latin-1") as file_read:
    output = file_read.readlines()

try:
    print(25 * "*")
    for l in output:
        if site_search in l:
            aa = l.split("/")[0].strip("\n")
            print(Fore.YELLOW + aa)
            try:
                print(Fore.GREEN + aa + Fore.RESET + " : " + Fore.RED + socket.gethostbyname(aa) + Fore.RESET)
            except socket.gaierror:
                print(Fore.RED + f"{aa} : Could not resolve" + Fore.RESET)
except KeyboardInterrupt:
    pass
