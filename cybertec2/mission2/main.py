from playsound import playsound
from pyautogui import sleep
from pyfiglet import figlet_format
import sys,os,time
import colorama
from colorama import Fore
import message as m2

while True:
     pss = input("Enter password given to you in mission1 to continue:")
     if pss == "778899":
      break


exploit1 = "exploiting.............................\n"
exploit2 = "Checking if vulnerable\n"
exploit3 = "vulnerable\n"
ftp1 = "Accessing\n"
ftp2 = "Checking username and password\n"
ftp3 = "Creentials correct........................\n"





print(figlet_format("MISSION2", font = "standard"))

while True:
    op = input("DO YOU WANT TO CONTINUE Yes/No > ")
    if op == "Yes":
        break
    else:
        quit()

playsound('files/check.mp3')

while True:
    commands = input(f"{Fore.YELLOW} server > ")

    if commands == "ls":
        print(f"{Fore.BLUE} help.txt")

    if commands == "clear":
        os.system("clear")

    if commands == "cat help.txt":
        m2.help()

    if commands == "nmap 185.0.72.18":
        print("scanning....................")
        sleep(2)
        print(f"{Fore.GREEN}Port : 72 closed")
        print(f"{Fore.GREEN}Port : 88 opened")
        print(f"{Fore.GREEN}Port : 92 closed")

    if commands == "search exploits":
        print(f"{Fore.GREEN}72.exec")
        print(f"{Fore.GREEN}88.exec")
        print(f"{Fore.GREEN}92.exec")
    if commands == "mail":
        m2.mail()

    if commands == "exec 88.exec 185.0.72.18":
        m2.exploit()
        break
print(figlet_format(f"{Fore.BLUE}KEVIN"))
while True:
    command3 = input(f"{Fore.BLUE}Kevin > ")

    if command3 == "ls":
        print(f"{Fore.BLUE} info.txt")
    
    if command3 == "cat info.txt":
        print(f"{Fore.GREEN} Username : cvet")
        print(f"{Fore.GREEN} Password : 7799")
    
    if command3 == "ftp cvet@7799 10.22.15.32":
        m2.ftp()
        break

    if command3 == "ls":
        print(f"{Fore.BLUE} help.txt")

    if command3 == "clear":
        os.system("clear")


while True:

    command4 = input("Chrisvet > ")
    if command4 == "ls":
        print(f"{Fore.BLUE} users.txt")
        print(f"{Fore.BLUE} passwords.txt")

    if command4 == "cat users.txt":
        m2.failed()
        quit()

    if command4 =="cat passwords.txt":
        print("File Encrypted")
        playsound("file/encrypt.mp3")

    if command4 == "cp users.txt server":
        print("Mission complete")
        playsound("files/mission.mp3")
        quit()
