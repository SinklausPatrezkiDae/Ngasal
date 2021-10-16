from os import system
import os
import terminaltables
#fungsi clear screen
def cls():
    return system('cls')

#fungsi menampilkan menu awal program
def menu():
    cls()
    print("|===========================|")
    print("|    MENU AWAL PROGRAM      |")
    print("|---------------------------|")
    print("| Pilihan Operasi |         |")
    print("|---------------------------|")
    print("| >> [1.] Binary Ke Decimal |")
    print("| >> [2.] Decimal Ke Binary |")
    print("|===========================|")

#fungsi validasi inputan bilangan hanya menerima angka
def angka(pesan):
    while True:
        try:
            ipt = int(input(pesan))
        except ValueError:
            print("|---------------------------------------------|")
            print("|- WARNING -| : Inputan Hanya Menerima Angka -|")
            print("|---------------------------------------------|")
        else:
            return ipt

#fungsi validasi inputan awal program hanya menerima 1 atau 2 saja
def pil(pesan):
    ipt = input(pesan)
    while ipt != "1" and ipt !="2":
        menu()
        print("|-----------------------------------------------|")
        print("|- WARNING -| : Pilihan Operasi Tidak Tersedia -|")
        print("|-----------------------------------------------|")
        ipt = input(pesan)
    return ipt

#fungsi menampilkan menu konversi binary ke decimal
def menu1():
    cls()
    print("|===============================|")
    print("|   KONVERSI BINARY KE DECIMAL  |")
    print("|===============================|")

def menu2():
    cls()
    print("|===============================|")
    print("|   KONVERSI DECIMAL KE BINARY  |")
    print("|===============================|")

#fungsi konversi Binary ke decimal
def binaryTodecimal():
    listangka = []
    listhasil = []
    cnt=0
    menu1()
    iptjumlah = angka("|>> Masukkan Jumlah Bilangan : ")
    print("|===============================|")
    for i in range(iptjumlah):
        iptbil = angka("|>> Masukkan Bilangan Biner : ")
        while iptbil != 0 and iptbil != 1:
            print("\n|- WARNING -| : Masukkan 1 ATAU 0 Saja")
            iptbil = angka("|>> Masukkan Bilangan Biner : ")
        listangka.append(iptbil)
        cnt+=1
    listangka.reverse()
    print("|===============================|")
    print(" >> ")
    for i in range(len(listangka)):
        print(listangka[i],end=" ")
    print()
    print("|===============================|")


    for i in range(len(listangka)):
        x = listangka[i] * 2 ** i
        print(f'|- {listangka[i]} * 2 ^ {i} = {x}')
        listhasil.append(x)

    y = sum(listhasil)
    print("|===============================|")
    print(f'|>> Decimal Dari {listangka} : {y}')
    print("|===============================|")

#fungsi kokversi decimal ke binary
def decimalToBinary():
    menu2()
    bil = angka("| >> Masukkan bilangan : ")
    x = bin(bil) [2:]
    print("|-------------------------------|")
    print(f'| >> Biner dari {bil} : {x}')
    print("|-------------------------------|")

def iptulang(pesan):
    ipt = input(pesan).lower()
    while ipt != 'y' and ipt != 't':
        print(f'|- WARNING -| : Inputan hanya menerima y ATAU t saja')
        ipt = input(pesan).lower()
    return ipt

def akhir():
    print('|-----------------|')
    print('|- AKHIR PROGRAM -|')
    print('|-----------------|')


def mulai():
    ulang = 'y'

    while ulang == 'y':
        menu()
        iptPil = pil("| >> Masukkan Pilihan Operasi : ")
        if iptPil == "1":
            binaryTodecimal()
        else:
            decimalToBinary()
        ulang = iptulang("| >> Ulangi Program? <y/t> : ")
    akhir()

mulai()

    
