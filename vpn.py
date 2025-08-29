# import required madules 

import os

from time import sleep

import random

#list of vpn server codes

codelist = ["TR" , "US-C" , "US" , "US-W", "CA" ,"CA-W"
            
            "FR" , "DE" , "NL" , "NO" , "RO" , "CH" , "GB" , "HK"]



try:

    #conect to vpn

    os.system("windscribe conect")

while True:
        #assigning a rsndom server
     choicecode = random.choice(codelist)

sleep(random.randrange(120 , 300))

print("!!!changing the ip address")

os.system("windscribe connect" + choice codelist)

except:

os.system("windscribe disconect")

print("sorry, some error has occurred")