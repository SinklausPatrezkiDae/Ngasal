from os import system
import math

#fungsi clear screem
def cls():
	return system('cls')

#fungsi menuawal program
def menu1():
	cls()
	print("|======================================|")
	print("|           LATIHAN 2 NOMOR 2          |")
	print("|--------------------------------------|")
	print("| >> PILIHAN OPERASI|                  |")
	print("|--------------------------------------|")
	print("| [1] >> Menghitung Keliling Lingkaran |")
	print("| [2] >> Menghitung Luas Lingkaran     |")
	print("|======================================|")

def menuKeliling():
	cls()
	print("|===========================|")
	print("|     KELILING LINGKARAN    |")
	print("|===========================|")

def menuLuas():
	cls()
	print("|===========================|")
	print("|       LUAS LINGKARAN      |")
	print("|===========================|")


#validasi inputan hanya menerima angka
def angka(pesan):
	while True:
		try:
			ipt = int(input(pesan))
		except ValueError:
			if iptpil == 1:
				menuKeliling()
			elif iptpil == 2:
				menuLuas()
			else:
				menu1()

			print("\n[WARNING] : Inputan Hanya Menerima Angka")
		else:
			return ipt

#validasi inputan hanya menerima y/t saja
def ulang1(pesan):
	ipt = input(pesan)
	while ipt != "y" and ipt != "t":
		if iptpil == 1:
			menuKeliling()
		elif iptpil == 2:
			menuLuas()
		print("\n [WARNING] : Inputan Hanya Menerima y/t saja")
		ipt = input(pesan)
	return ipt

#validasi inputan hanya menerima 1 atau 2 saja
def iptmenu1(pesan):
	ipt = angka(pesan)
	while ipt != 1 and ipt != 2:
		menu1()
		print("\n[WARNING] : Inputan Hanya Menerima 1/2 saja")
		ipt = angka(pesan)
	return ipt

#fungsi mencari keliling lingkaran
def Kelilinglingkaran():
	menuKeliling()
	iptJr = angka("| >> Masukkan Jari - Jari Lingkaran : ")

	if iptJr % 7 == 0:
		keliling = 2 * (22/7) * iptJr
	else:
		keliling = 2 * math.pi * iptJr
	#output
	cls()
	print("|=======================================|")
	print("|           OUTPUT KELILING             |")
	print("|---------------------------------------|")
	print("| >> Jari - Jari Lingkaran = ",iptJr)
	print("| >> Keliling Lingkaran    = ",keliling)
	print("|=======================================|")

def luasLingkaran():
	menuLuas()
	iptJr = angka("| >> Masukkan Jari - Jari Lingkaran : ")
	L = math.pi * iptJr ** 2
	#output
	cls()
	print("|=======================================|")
	print("|              OUTPUT LUAS              |")
	print("|---------------------------------------|")
	print("| >> Jari - Jari Lingkaran  = ",iptJr)
	print("| >> luas Lingkaran         = ",L)
	print("|=======================================|")

#main
ulang = "y"
while ulang == "y":
	iptpil = 0
	menu1()
	iptpil = iptmenu1("| >> Masukkan Pilihan : ")
	if iptpil == 1:
		Kelilinglingkaran()
	else:
		luasLingkaran()
	ulang = ulang1("| >> Ulangi Program? <y/t> : ")





































	

