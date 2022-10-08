from pyfiglet  import figlet_format
from playsound import playsound
import colorama
from colorama import Fore
import sys
import os
import time
import message1 as m1
colorama.init(autoreset=True)

print(figlet_format(f"CYBERTEC", font = "standard"))
playsound("file/welcom.mp3")
m1.typer()
os.system("clear")
playsound("file/mission1.mp3")

while True:
    command = input(f"{Fore.GREEN} server > ")
    if command == "ls":
        print("mission.txt")
    
    if command == "cat mission.txt":
        m1.typer()

    if command == "help":
        m1.help()

    if command == "nmap 127.0.0.1":
    
        print(f"Port : 80 http open")
        print(f"Port : 22 ftp close")
    
    if command == "search exploit":
        print("http80.exec")
        print("ftp22.exec")
    if command == "clear":
        os.system("clear")

    if command == "exec http80.exec 127.0.0.1":
        m1.exploit()
        print(figlet_format("N.S.A SERVER", font = "standard"))
        playsound("file/Nsa.mp3")
        break

while True:
    command2 = input(f"{Fore.BLUE}N.S.A > ")
    if command2 == "ls":
        print("important.txt")
        print("data.txt")

    if command2 == "clear":
        os.system("clear")    

    if command2 == "cp important.txt server":
        m1.download()
        playsound("file/mission.mp3")
        break
print("Use 997788 to extract level 2")
