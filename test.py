"""
UAS Algoritma dan Pemrograman
Nama : Sinklaus Patrezki Dae
Kelas : 2A
Prodi S1 Sistem Informasi 
Fakultas Teknologi Informasi
"""

#FUNGSI MENU
from os import system
import datetime
from time import sleep

tanggal = datetime.datetime.now()


def cls():
	return system('cls')

def menu():
	print(45*"=")
	print("PERHITUNGAN GAJI POKOK KARYAWAN CV LOGOS") 
	print(45*"=")

def pilihan():
	print(45*"=")
	print(f'Kode \t Golongan \t Gaji')
	for i in range(len(listKode)): #untuk i di dalam banyaknya data dalam listKode (for loop otomatis menambahkan increment)
		print(f'{listKode[i]} \t {listGol[i]} \t Rp.{listGaji[i]:,}') #tampilkan list kode, listgol, listgaji
	print(45*"=") 

def iptgol():
	while True: #infinite loop (akan mengulang secara terus menerus sampai inputan yang dimasukkan benar)
		try: #menangkap error pada inputan user
			ipt = int(input("Golongan : "))
		except: #dan mengubahnya menjadi pesan error (sehingga program tidak force close)
			cls()
			menu()
			pilihan()
			print(f'\nInputan Hanya Menerima Angka')
		else:
			return ipt  

def iptanak():
	ipt = input("Punya Anak? : ").upper()
	while ipt != "SUDAH" and ipt != "BELUM":
		cls()
		menu()
		pilihan()
		print(f'\n[warning] : Masukkan Sudah atau belum saja')
		ipt = input("Punya Anak? : ").upper() #.upper mengubah inputan user menjadi huruf besar
	return ipt



def iptjk():
	ipt = input("Jenis Kelamin : ").upper()
	while ipt != "LAKI-LAKI" and ipt != "PEREMPUAN":
		cls()
		menu()
		pilihan()
		print(f'\n[Warning] : Masukkan Laki-laki ATAU perempuan saja')
		ipt = input("Jenis Kelamin : ").upper()
	return ipt

def iptkawin():
	ipt = input("Status Kawin : ").upper()
	while ipt != "KAWIN" and ipt != "BELUM":
		cls()
		menu()
		pilihan()
		print(f'\n[warning] : Masukkan (kawin/belum)')
		ipt = input("Status Kawin : ").upper()
	return ipt

def output():
	cls()
	#tampilkan gaji pokok
	print(45*"=") #print samadengan sebanyak 45 kali dalam 1 baris
	print(f'SLIP GAJI PEGAWAI')
	print(f'{tanggal}')
	print(45*"=")
	print(f'Nama          : {iptnama}')
	print(f'Golongan      : {gol}')
	print(f'Jenis Kelamin : {jk}')
	print(f'Status Kawin  : {kawin}')
	if kawin == "KAWIN" and anak == "SUDAH":
		print(f'Punya Anak    : {anak}')
		print(45*"=")
		print(f'Tunjangan Istri : Rp.{tunIstri:,}')
		print(f'Tunjangan Anak  : Rp.{tunAnak:,}')
	elif kawin == "KAWIN" and anak == "BELUM":
		print(f'Punya Anak    : {anak}')
		print(45*"-")
		print(f'Tunjangan Istri : Rp.{tunIstri:,}')
		print(f'Tunjangan Anak  : Tidak Dapat Tunjangan Anak')
	else:
		pass
	print(45*"-")
	print(f'Gaji Pokok    : Rp.{gajiPokok:,}')
	print(f'Gaji Bruto    : Rp.{gajiBruto:,}')
	print(45*"-")
	print(f'Biaya Jabatan : Rp.{byjabatan:,}') 
	print(f'Iuran Pensiun : Rp.{iuranpensiun:,}')
	print(f'Iuran Organisasi : Rp.{iuranorganisasi:,}')
	print(45*"-")
	print(45*"=")
	print(f'Gaji Netto    : Rp.{gajiNetto:,}')
	print(45*"=")

def ipttambah():
	print()
	ipt = input("Tambah Karyawan? [y/t]: ").lower()
	while ipt != 'y' and ipt != 't':
		cls()
		menu()
		pilihan()
		print(f'\n[warning] : Masukkan y ATAU T saja')
		ipt = input("Tambah Karyawan? [y/t]: ").lower()
	return ipt

def output2():
	cls()
	print(45*"=")
	print(f'List Gaji Pegawai \n{tanggal}')
	print(45*"=")
	i = 0
	while i < cnt:
		print(45*"-")
		print(f'PEGAWAI KE {i+1}')
		print(45*"-")
		print(f'Nama       : {listnama[i]}')
		print(f'Golongan   : {listgol[i]}')
		print(f'Gaji Pokok : Rp.{listgajipokok[i]:,}')
		print(f'Gaji Bruto : Rp.{listgajibruto[i]:,}')
		print(f'Gaji Netto : Rp.{listgajinetto[i]:,}')
		print(45*"-")
		i+=1

#list/array untuk ketentuan perhitungan gaji
listKode = [1,2,3]
listGol = ["Golongan 1", "Golongan 2","Golongan 3"]
listGaji = [2_500_000,4_500_000,6_500_000]

#list sebagai temp storage untuk menampung nama dari berbagai user (lebih dari 1 pegawai)
listnama = []
listgol = []
listgajipokok = []
listgajibruto = []
listgajinetto = []

#counter
cnt = 0 #untuk mengcounter data pegawai yang sudah diisi sebelumnya
tambah = 'y'

while tambah == 'y':

	#memanggil fungsi
	cls()
	menu()
	pilihan()

	iptnama = input("Nama : ").upper() #inputan nama

	gol = iptgol() #inputan golongan
	while gol < 1 or gol > 3: #validasi inputan golongan hanya menerima 1 sampai 3 saja
		cls() #bersihkan layar
		menu() #memanggil fungsi untuk menampilkan menu (ada di line 18)
		pilihan() #memanggil fungsi untuk menampilkan pilihan golongan (ada di line 23)
		print(f'\n[warning] : Golongan Tidak Tersedia!') #menampilkan pesan erro jika inputan lebih dari 3 atau kurang dari 1
		gol = iptgol()	

	jk = iptjk() #inputan jenis kelamin

	kawin = iptkawin() # inputan kawin
	if kawin == "KAWIN": #jika pegawai sudah skidipapap maka tampilkan inputan anak
		anak = iptanak() # inputan anak
	else : #selain itu lewati
		pass

	# ambil index golongan dari inputan user
	for i in range(len(listKode)): #untuk nilai i di range banyaknya data dalam liskode
		if gol == listKode[i]: # jika inputan golongan samadengan index dari listKode
			golongan = listGol[i] #buat variabel baru yang merupakan referensi dari var lisGol[i] (biar gk pusing tambahin index)
			gajiPokok = listGaji[i] # sama 
		pass


	#tunjangan istri
	if jk == "LAKI-LAKI" and kawin == "KAWIN":
		if gol == listKode[0]:
			tunIstri = 1/100 * gajiPokok
		elif gol == listKode[1]:
			tunIstri = 3/100 * gajiPokok
		else:
			tunIstri = 5/100 * gajiPokok
	else :
		tunIstri = 0
		print(f'Tidak ada Tunjangan Istri')

	#tunjangan anak
	if kawin == "KAWIN" and anak == "SUDAH" :
		tunAnak = 0.02 * gajiPokok
	else :
		tunAnak = 0
		print(f'Tidak ada Tunjangan Anak')

	#Gaji Bruto
	if kawin == "KAWIN" and anak == "BELUM":
		gajiBruto = gajiPokok + tunIstri
	elif kawin == "KAWIN" and anak == "SUDAH":
		gajiBruto = gajiPokok + tunIstri + tunAnak
	else :
		gajiBruto = gajiPokok

	#biaya jabatan
	byjabatan = 0.005 * gajiBruto
	iuranpensiun = 15_500
	iuranorganisasi = 3_500

	#Gaji Netto
	gajiNetto = gajiBruto - byjabatan - iuranpensiun - iuranorganisasi

	#output
	output() # fungsi menampilkan keseluruhan data dari pegawai (ada di line 74)

	#menampung inputan user kedalam temp storage
	listnama.append(iptnama)
	listgol.append(gol)
	listgajipokok.append(gajiPokok)
	listgajibruto.append(gajiBruto)
	listgajinetto.append(gajiNetto)
	cnt+=1 # increment counter agar data yang sudah terisi sebelumnya bisa tersimpan

	tambah = ipttambah()

	output2() #fungsi menampilkan data dari setiap pegawai (ada di line 120)


#exit 
print(45*"=")
print(f"PROGRAM BERAKHIR")
print(45*"=")
sleep(2)
iptexit = input("\nPress anykey to exit")
print(45*"-")
