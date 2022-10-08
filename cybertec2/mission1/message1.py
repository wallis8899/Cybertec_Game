import colorama
import sys,os,pyfiglet,time,subprocess
from colorama import Fore
from pyautogui import sleep

colorama.init(autoreset=True)

exploit1 =("exploiting.....................................................................................................\n")
exploit2 = "Checking if target is vulnerable\n"
exploit3 = "Target seems vulnerable\n"
exploit4 = "copying......................../././././././././././././././.\n"

def typer():
 with open("file/mission.txt") as f:
    for char in f:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)

def help():
 with open("file/help.txt") as f:
    for char in f:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)

def exploit():
    for char in exploit1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)


    for char in exploit2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
        
    for char in exploit3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)

def download():
        
    for char in exploit4:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
