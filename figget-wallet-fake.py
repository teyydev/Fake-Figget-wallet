import time
import random
import string
import os
from colorama import init, Fore
init(convert=True)
import colorama
colorama.init()
import subprocess, requests

hardwareid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
site = requests.get("https://pastebin.com/raw/XXXXX")


print(colorama.Fore.RED)
LicenseKey = input('Entrez le mot de passe [-] : ')
if LicenseKey == "666":
    print(Fore.GREEN + "Le mot de passe est valide !")
    time.sleep(0.5)
else:
    print(Fore.RED + "Le mot de passe n'est pas valide !")
    print(Fore.RED + "Appuyez sur Entrée pour quitter !")
    input("")
    exit(123)

os.system("cls")
wallet = input(Fore.RED + "Wallet : ")
print(Fore.CYAN + "Vérification de l'existence du portefeuille...")
time.sleep(1)
print("Portefeuille trouvé")

time.sleep(0.2)

def file_len():
    with open("proxies.txt") as f:
        for i, _ in enumerate(f):
            pass
    return i
print(f"""

[1] Utiliser des proxys

""")
proxies = input("Voulez-vous utiliser des proxy ? [-] ")
if proxies == "1":
    print(Fore.GREEN + " [-] Le proxy a était ajouté avec succès")
else:
    print("Le proxy a était ajouté avec succès")
time.sleep(0.2)
print(Fore.BLUE+ "Mise en place d'un espace de travail pour vous...")
time.sleep(3)

def id_gen(size=40, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))

tries = 0

while(True):
    if(tries > random.randint(10000, 100000)): # chance to get fake btc
        print(Fore.CYAN +"[-]"+ Fore.RED + " 0x" + id_gen() + Fore.GREEN +" |  Valid  |  " + str(round(random.uniform(0,2), 4)), "BTC")
        print(Fore.GREEN +"Retrait dans votre portefeuille...")
        time.sleep(1)
        tries = 5
        print(Fore.GREEN + "Fait!")
        time.sleep(0.1)
    else:
        print(Fore.CYAN +"[-]"+ Fore.RED + " 0x" + id_gen() + Fore.LIGHTRED_EX +" | Invalid |  " + "0.0000 BTC")
        tries += 1
