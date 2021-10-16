from os import system

def cls():
    return system('cls')

def ipthuruf(pesan):
    while True:
        ipt = input(pesan)
        if ipt.isalpha():
            return ipt
        else:
            cls()
            print("\nInputan Hanya Menerima Huruf")
cls()
huruf = ipthuruf("||-->> Masukkan Nama : ")
print("Halo " + huruf)