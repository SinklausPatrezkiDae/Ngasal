from os import system
#fungsi tampilanawalprogram
def tampilanawal():
    print(35*"=")
    print("PROGRAM MENAMPILKAN DATA MAHASISWA")
    print(35*"=")

#fungsi clear screen
def cls():
    return system('cls')

#fungsi validasi inputan hanya menerima angka
def angka():
    while True:
        try:
            ipt = int(input("Masukkan Nilai : "))
        except :
            cls()
            tampilanawal()
            print("\n[!] : Inputan Hanya Menerima Angka")
        else :
            return ipt

#fungsi input nama
def nama():
    ipt = input("Masukkan Nama : ").upper()
    return ipt

#list untuk menampung nama dan nilai mahasiswa
listnama=[]
listnilai=[]

#menyiapkan variabel input lagi dan counter
iptlagi = 'y'
cnt = 0

while iptlagi == 'y':
    cls()
    #memanggil fungsi tampilanawal
    tampilanawal()

    #memanggil fungsi Inputan
    name = nama()
    nilai = angka()

    #validasi inputan angka hanya menerima 0-100 saja.
    while nilai < 0 or nilai > 100 :
        cls()
        tampilanawal()
        print("\n[!] : Inputan Hanya Menerima Angka 0-100 saja")
        nilai = angka()

    #menyimpan inputan nama dan nilai kedalam list
    cnt+=1
    listnama.append(name)
    listnilai.append(nilai)

    #inputan untuk menambah mahasiswa
    iptlagi = input("\nInput Lagi? (y/t) : ").lower()

    #validasi iptlagi hanya meneriam y/t saja
    while iptlagi !='y' and iptlagi !='t':
        cls()
        print("\n[!] : Inputan Hanya Menerima y/t saja")
        iptlagi = input("Input Lagi? (y/t) : ").lower()

    #output
    print()
    print(70*"=")
    print("NO",2*"\t","NAMA MAHASISWA",2*"\t","NILAI MAHASISWA")
    i = 0
    while i < cnt :
        print()
        print(i+1,2*"\t",listnama[i],4*"\t",listnilai[i])
        i+=1
    print(70*"=")

    #rumus rata_rata
    rata_rata = sum(listnilai)/len(listnilai)

    #output jumlah mahasiswa dan rata_rata nilai
    print("Jumlah Mahasiswa : ",len(listnama))
    print("Rata-Rata Nilai : ",rata_rata)

iptexit = input("\nPress anykey to exit")
