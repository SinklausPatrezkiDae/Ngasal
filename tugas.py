from os import system
from time import sleep
import getpass
import sys

#fungsi clear screen
def cls():
    return system('cls')
#fungsi menu
def menu():
    cls()
    print("|===============================|")
    print("|      MENU AWAL PROGRAM        |")
    print("|-------------------------------|")
    print("|  |>> 1. [REGISTER]            |")
    print("|  |>> 2. [LOGIN]               |")
    print("|-------------------------------|")

def menuRegister():
    cls()
    print("|====================================|")
    print("|              REGISTER              |")
    print("|------------------------------------|")

def menuLogin():
    cls()
    print("|------------------------------------|")
    print("|              LOGIN                 |")
    print("|------------------------------------|")


def uname(pesan):
    while True:
        ipt = input(pesan)
        if not ipt.isdigit():
            return ipt
        else:
            menuLogin()
            print("\n[WARNING] : Nama Kok Angka")

def iptlogin(pesan):
    ipt = input(pesan)
    while ipt != 'y' and ipt != 't':
        menuRegister()
        print("\n[WARNING] : Inputan Hanya Menerima y ATAU t")
    return ipt

def pw(pesan):
    ipt = getpass.getpass(pesan)
    return ipt

def pwconfirm(pesan):
    ipt = getpass.getpass(pesan)
    return ipt

def pilMenu(pesan):
    while True:
        try:
            ipt = int(input(pesan))
        except ValueError:
            menu()
            print("\n[WARNING] : Inputan Hanya Menerima Angka Saja")
        else:
            return ipt

def sudahlogin():
    cls()
    print("|-----------------------------|")
    print("|      WWW.FACEBOOK.COM       |")
    print("|-----------------------------|")
    print("| >> SELAMAT DATANG ",iptUname)
    print("|-----------------------------|")

#main
#menyiapkan list sebagai temp storage dan var lainnya
listUname =[]
listPw = []
cnt = 0
chance = 0
terdaftar ='y'
#selama terdaftar = y maka program akan berjalan
while terdaftar == 'y':
    menu()
    iptpil = pilMenu("| >> Masukkan Pilihan : ")
    while iptpil != 1 and iptpil != 2:
        menu()
        print("\n[WARNING] : Masukkan 1 ATAU 2 saja!")
        iptpil = pilMenu("| >> Masukkan Pilihan : ")

    #Pohon Keputusan
    #jika pil = 1 masuk menu register
    if iptpil == 1:
        sleep(0.7)
        menuRegister()
        uName = uname("| >> Username : ")
        pW = pw("| >> Password : ")
        iptconfirm = pwconfirm("| >> Konfirmasi Password : ")
        while iptconfirm != pW:
            menuLogin()
            print("\n[WARNING] : Konfirmasi Gagal")
            iptconfirm = pwconfirm("| >> Konfirmasi Password : ")
        cnt+=1
        listUname.append(uName)
        listPw.append(pW)

    #selain itu jika pil = 2 masuk menu login
    elif iptpil == 2:
        sleep(0.7)
        menuLogin()
        iptUname = uname("| >> Username : ")
        while iptUname not in listUname:
            menuLogin()
            print("\n[WARNING] : Username Tidak Tersedia!")
            iptUname = uname("| >> Username : ")
        iptPw = pw("| >> Password : ")
        while iptPw != listUname.index(iptUname) and chance<3:
            menuLogin()
            chance+=1
            print("\n[WARNING] : Password Salah!")
            print("| >> KESEMPATAN KE ",chance," Gagal")
            iptPw = pw("| >> Password : ")
            if chance == 3:
                cls()
                print("========== PROGRAM BERAKHIR ===========")
                sys.exit()
            else:
                pass

        #hentikan perulangan    
        terdaftar = 't'

        #menampilkan output sudah berhasil login
        cls()
        for i in range(8):
            print("Loading...")
            sleep(0.2)

        cls()
        sudahlogin()





