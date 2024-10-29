#!/usr/bin/env python3
import socket
import requests
from colorama import init, Fore
from pyfiglet import Figlet
import os

# Colorama başlatılmasını sağlıyoruz.
init(autoreset=True)

# Figlet kütüphanesini kurup, ekranı temizleyip yazdırıyoruz.
os.system("apt-get install figlet")
os.system("clear")

# Programın başlığını belirtiyoruz
f = Figlet(font='slant')
print(Fore.BLUE + f.renderText('Usom Check'))
print(Fore.RED + "          | - | Made By : F3NR1R - Cyber Security | - |         ")

# Usom'un resmi linkini tanımlatıyoruz.
usom_url = "https://www.usom.gov.tr/url-list.txt"

# Fetch the list from USOM
try:
    response = requests.get(usom_url)
    response.raise_for_status()  # Raise an error if the request failed
    usom_list = response.text.splitlines()
except requests.exceptions.RequestException as e:
    print(Fore.RED + f"Error fetching USOM list: {e}")
    exit(1)

# Tanımlatılacak olan website url adresini giriyoruz.
site_search = input("Enter the website to check: ")

# Usom listesine göre karşılaştırıp sonuç veriyoruz.
try:
    found = False
    print(25 * "*")
    for line in usom_list:
        if site_search in line:
            aa = line.strip()
            print(Fore.YELLOW + aa)
            try:
                # Domaini ip adresle çözümletiyoruz
                ip_address = socket.gethostbyname(aa)
                print(Fore.GREEN + aa + Fore.RESET + " : " + Fore.RED + ip_address + Fore.RESET)
            except socket.gaierror:
                print(Fore.RED + f"{aa} : Could not resolve" + Fore.RESET)
            found = True
    if not found:
        print(Fore.RED + "The website was not found in the USOM list.") # Usom listesinde görülmediği ortaya çıkıyor, yani girilen website güvenli olabilir.
except KeyboardInterrupt:
    print(Fore.RED + "\nProcess interrupted by user.") # Hata kodu döndürüyoruz.
    exit(1)
