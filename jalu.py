from os import system
import terminaltables

#fungsi clear screen
def cls():
	return system('cls')

#fungsi validasi inputan hanya menerima angka
def angka(pesan):
	while True :
		try:
			ipt = int(input(pesan))
		except ValueError:
			menu()
			print("| WARNING | : INPUTAN HANYA MENERIMA ANGKA")
		else:
			return ipt

#fungsi validasi inputan hanya menerima y/t saja
def ulang1():
	ipt = input("|- INPUT LAGI? <Y/T> -| :  ").lower()
	while ipt != "y" and ipt != "t":
		menu()
		print("|- WARNING -| : MASUKKAN Y ATAU T SAJA")
		ipt = input("|- INPUT LAGI? <Y/T> -| :  ").lower()
	return ipt

def menu():
	cls()
	print("|=========================|")
	print("|    MENU AWAL PROGRAM    |")
	print("|=========================|")

#MAIN
listnama = ['ANDI','BAGUS','CITRA']
listnilai = [80,40,60]
liststs = ['L','TL','TL']
cnt = 0
sts = ""
tambah = "y"
while tambah == "y":
	menu()

	iptnama = input("| >> Masukkan Nama : ").upper()
	iptnilai = angka("| >> Masukkan Nilai : ")
	while iptnilai < 0 or iptnilai > 100:
		menu()
		print("|- WARNING -| Inputan Hanya Menerima Angka 0 Sampai 100 Saja")
		iptnilai = angka("| >> Masukkan Nilai : ")

	listnama.append(iptnama)
	listnilai.append(iptnilai)

	#pengkondisian
	if iptnilai > 60:
		liststs.append("L")
	else:
		liststs.append("TL")

	cnt+=1
	print("|-------------------------|")
	tambah = ulang1()
	print("|-------------------------|")


kolom = ['NO','NAMA','NILAI','STATUS']

baris = [(i+1,listnama[i],listnilai[i],liststs[i])for i in range(len(listnama))]

table_data = [kolom]
table_data.extend(baris)
table = terminaltables.AsciiTable(table_data)
cls()
print(table.table)

jumlah = sum(listnilai)
rata_rata = jumlah/len(listnilai)

print("| >> NILAI RATA RATA = ",int(rata_rata))

iptexit = input("\n| >> Tekan Enter untuk untuk keluar")