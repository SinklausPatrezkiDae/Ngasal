#program menampilkan angka
from os import system

def cls():
    return system('cls')

def angka(pesan):
    while True:
        try:
            ipt = int(input(pesan))
        except ValueError:
            cls()
            print("\n[WARNING] : inputan hanya menerima angka saja! ")
        else:
            return ipt

nilai = angka("| >> Masukkan Angka : ")
