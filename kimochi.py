from os import system
def cls():
    return system('cls')

def angka1(pesan):
    while True:
        try:
            ipt = int(input(pesan))
        except ValueError:
            cls()
            print("\n[WARNING] : INPUTAN HANYA MENERIMA ANGKA")
        else:
            return ipt
def angka2(pesan):
    while True:
        try:
            ipt = int(input(pesan))
        except ValueError:
            cls()
            print("\n[WARNING] : INPUTAN HANYA MENERIMA ANGKA")
        else:
            return ipt
#Main
cls()
iptA = angka1("|>> Masukkan Nilai A = ")
iptB = angka2("|>> Masukkan Nilai B = ")
C = 0
D = 0

#pengkondisian
if iptA>iptB:
    C = iptA*iptB
else:
    C = iptA+iptB
    D = C*C

print("Nilai C = ",C)
print("Nilai D = ",D)


