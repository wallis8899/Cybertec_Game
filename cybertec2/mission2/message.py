import sys,os,time
from playsound import playsound
import colorama
from colorama import Fore
from pyfiglet import figlet_format
exploit1 = "exploiting.............................\n"
exploit2 = "Checking if vulnerable\n"
exploit3 = "vulnerable\n"
ftp1 = "Accessing\n"
ftp2 = "Checking username and password\n"
ftp3 = "Creentials correct........................\n"


def help():
    print(f"{Fore.GREEN} nmap to scan ip = namp target ip\n",
"cp to copy = cp file name  server\n",
"clear to clear = clear\n",
"cat to open a file = cat filename\n",
"search exploits to search for exploits = search exploits\n",
"fpt to connect to a frp server = ftp username@password ip\n",
"exec = to exploit system = exec exploitname ip\n",
"mail to open available emails = mail \n")


def help():
    print(f"{Fore.BLUE}Agent,\n",
"    You did a great job, and i have a new one for you.\n",
"      I want you to hack the Kevin server and open a file\n",
"      called info.txt,You will find the username and password\n",
"      for an ftp server,copy a file called users.txt.\n",
"Note:Donot open the ""users.txt file \n",)


def exploit():
    for char in exploit1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)

    for char in exploit2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)

    for char in exploit3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)


def ftp():
    for char in ftp1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)

    for char in ftp2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)

    for char in ftp3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)

def failed():
    playsound("files/failed.mp3")
    print(figlet_format("MISSION FAILED", font = "isometric3"))

def mail():
    print(f"{Fore.GREEN}Agent,\n",
"      You did a great job, and i have a new one for you\n",
"      I want you to hack the Kevin server and open a file\n",
"      called info.txt,You will find the username and password\n",
"      for an ftp server,copy a file called users.txt\n",
"Note:Donot open the ""users.txt file\n",
"                                                               \n",
"Kevin server\n",
"ip = 185.0.72.18\n",
"                                                                 \n",
"Target ftp server\n",
"ip = 10.22.15.32\n")
