#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#github.com/AngelSecurityTeam/Cam-Hackers
import requests,re,os
import time
import sys

os.system("clear")
print("""

\033[1;97m  _       __________    __________  __  _________\033[0m
\033[1;97m | |     / / ____/ /   / ____/ __ \/  |/  / ____/\033[0m
\033[1;97m | | /| / / __/ / /   / /   / / / / /|_/ / __/   \033[0m
\033[1;97m | |/ |/ / /___/ /___/ /___/ /_/ / /  / / /___   \033[0m
\033[1;97m |__/|__/_____/_____/\____/\____/_/  /_/_____/\033[3;97mv1.1\033[0m
  \033[1;91m██ 20% *___*
   \033[1;92m███ 40% *___*
    \033[1;93m████ 60% *___* 
      \033[1;97m█████ 80% *___*
       \033[1;96m██████ @NABIL RAHMAN*___*

     
▒█▄░▒█ ░█▀▀█ ▒█▀▀█ ▀█▀ ▒█░░░ 
▒█▒█▒█ ▒█▄▄█ ▒█▀▀▄ ▒█░ ▒█░░░ 
▒█░░▀█ ▒█░▒█ ▒█▄▄█ ▄█▄ ▒█▄▄█
                                    
                                
   █▀█ █▀▀ █▀▀ █ █▀▀ █ ▄▀█ █░░
   █▄█ █▀░ █▀░ █ █▄▄ █ █▀█ █▄▄                              
           👊FUCK THE SYSTEM✌ @NABIL RAHMAN                                                                    

\033[1;31m1)\033[1;37mUnited States                                   
\033[1;31m68)\033[1;37mPakistan
\033[1;31m21)\033[1;37mIndia                                                          
\033[1;31m59)\033[1;37mBangladeh             
\033[1;31m91)\033[1;37mExtra
""")



 
try:                                                               
    num = int(input("NABIL SAY: SELECT : "))


    if num == 1:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,720):
			
                url = ("https://www.insecam.org/en/bycountry/US/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        
        except:
            print (" ") 
    elif num == 21:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,22):
			
                url = ("https://www.insecam.org/en/bycountry/IR/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        
        except:
            print (" ") 
    elif num == 59:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,4):
			
                url = ("https://www.insecam.org/en/bycountry/BD/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        
        except:
            print (" ")
    elif num == 68:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,4):
			
                url = ("https://www.insecam.org/en/bycountry/PK/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        
        except:
            print (" ")
                                                                                                   
    else:
        print(" ")

except KeyboardInterrupt:
        print (" ")
