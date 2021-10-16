from time import sleep
from os import system

def cls():
    system('cls')

def angka(pesan):
    while True:
        try:
            ipt = int(input(pesan))
        except ValueError:
            cls()
            print("\nMasukkin lagi goblok")
        else:
            return ipt

angka("| Masukkan angka : ")
