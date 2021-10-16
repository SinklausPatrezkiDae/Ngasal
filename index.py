from os import system
def cls():
    return system('cls')
listnama = ['erick','ariel','talia']
listpw = ["1","2","3"]
cls()


iptuname = input("Username : ")
while iptuname not in listnama:
    iptuname = input("Username : ")

urutanUname = listnama.index(iptuname)

iptPw = input("Password : ")
while iptPw not in listpw:
    iptPw = input("Password : ")

while listnama[urutanUname] != iptPw:
    iptPw = input("Password : ")

    
print(listnama[urutanUname], listpw[urutanUname])
