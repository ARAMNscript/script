import urllib
import requests
import os
print("\n\n")
print("*"*20)
print('ADMIN finder Arman Hackers')
print("*"*20)
print("\n")
print("\n")
site = input(">>> Enter Your Site  :    ") # http://github.com
if 'http://' in site:
    site = site
else:
    site = 'http://' + site
print("\n\n")
print("<?>  Check Url ...")
print("\n")
u = requests.get(site)
if u.status_code == 200 :
    print("<+>  Website ON  :   ",site)
else:
    print("<->  Website Down  :   ",site)
    exit
print("\n")
os.system('cls')
patch = open('uu.txt')
for admin in patch:
    try:
        s = site + '/' + admin
        s = str(s)
        url = urllib.request.urlopen(s)
        print("<+!>  Finded Admin  :   ",s)
        break
    except urllib.error.URLError:
        print("<-?>  No Admin  :   ",s)
        print("\n")
