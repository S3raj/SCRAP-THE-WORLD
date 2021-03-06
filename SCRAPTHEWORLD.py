# Project by SURAJ DHAMAK

import socket
import sys
import os
import subprocess
from bs4 import BeautifulSoup
import requests

#GET IP ADDRESS OF ANY URL 
def ipaddress():
    url=input("Enter the URL : ")
    try:
        ip=socket.gethostbyname(url)
        print("IP Found  : ",ip)
    except:
        print("URL Not found")
#SCAN THE PORTS
def portscan():
    target=input("Enter The host to be scan : ")
    port=int(input("Enter the Port(You want scan) : "))
    print("-"*50)
    print("Scanning Target : ",target,"at port",port)
    ip=socket.gethostbyname(target)
    print("Target IP : ",ip)    
    print("Port      : ",port)
    print("-"*50)
    try:
        print("Scanning.....\n")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print("[+] Port {} is open".format(port))
        else:
            print("[+] Port {} is closed".format(port))
        s.close()
    
    except KeyboardInterrupt:
        print("\n Exitting Program !!!!")
        sys.exit()
    except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
    except socket.error:
        print("\ Server not responding !!!!")
        sys.exit() 
#SEARCH FOR HIDDEN DIRECTORIES
def dirsearch():
    url=input("Enter the URL to scan : ")
    path=input("Enter the wordlist path :")
    print("-"*50)
    print("Scanning Target : ",url)
    ip=socket.gethostbyname(url)
    print("Target IP : ",ip)    
    print("-"*50)        
    print("[+] parsing the wordlist.....")
    try:
        with open(path) as file:
            check=file.read().strip().split("\n")
            print("[+] PARSING DONE ")
            print("[+] TOTAL PATHS TO BE CHECK : ",str(len(check)))
    except IOError:
        print('[+] FAILED')
        print('[+] Failed to read the wordlist specified')
        sys.exit(1)
    def checkpath(cp):
        u='http://'+url+'/'+cp
        #print (u)
        try:
            r = requests.head(u)
            code=r.status_code
        except requests.ConnectionError:
            print("failed to connect")
        if(code == 200 or code == 301 or code == 403):
            print("[+]",u," [",code,"]")
            
    print("[+] Begin scanning....")
    for i in range(len(check)):
        #print(check[i])
        checkpath(check[i])
    print('\n Scan complete....')
    
#FIND INTERESTING LINKS    
def Links():
    url=input("Enter the URL : ")
    print("[+] Fetching links.....")
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    for link in soup.find_all('a'):
        lin=link.get('href')
        if(lin.startswith('http')):
            print("[+] ",lin)
    print("Fetched Successfully...")
    
print('''

 _____  _____ _____  _  _   _____    _______ _    _ ____   __          _____  _____  _      _____  
  / ____|/ ____|  __ \| || | |  __ \  |__   __| |  | |___ \  \ \        / / _ \|  __ \| |    |  __ \ 
 | (___ | |    | |__) | || |_| |__) |    | |  | |__| | __) |  \ \  /\  / / | | | |__) | |    | |  | |
  \___ \| |    |  _  /|__   _|  ___/     | |  |  __  ||__ <    \ \/  \/ /| | | |  _  /| |    | |  | |
  ____) | |____| | \ \   | | | |         | |  | |  | |___) |    \  /\  / | |_| | | \ \| |____| |__| |
 |_____/ \_____|_|  \_\  |_| |_|         |_|  |_|  |_|____/      \/  \/   \___/|_|  \_\______|_____/ 
                                                                                                     
                                                                  - SURAJ DHAMAK
''')
    #options
print('1 - Get IP address for a website')
print('2 - Check ports')
print('3 - Find hidden Directories')
print('4 - Find any interesting links or contents found in webpage')
print()
    
    #input
    
opt=int(input("Enter the Option :"))
if(opt == 1 ):
    ipaddress()
elif(opt == 2):
    portscan()
elif(opt == 3):
    dirsearch()
elif(opt == 4):
    Links()
else:
    print("Enter a valid option")

