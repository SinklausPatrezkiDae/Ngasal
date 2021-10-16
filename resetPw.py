username = ["tomo","melati"]
passwrod = ["uhuy","ahay"]

perubahan = input("Apakah ingin mengubah password : ").lower()

def reset_password():
    iptUname = input("Masukkan username anda : ").lower()
    if iptUname in username:
        urutan = username.index(iptUname)
        pwbaru = input("Masukkan Password baru : ")
        konpwbaru = input("Konfirmasi Password : ")
        if pwbaru == konpwbaru:
            passwrod[urutan] = konpwbaru
            print("sukses\n")
            print("Checklist daftar password baru : ",passwrod)
        else:
            print("Password tidak sama")
    else:
        print("Username tidak ditemukan")
reset_password()



