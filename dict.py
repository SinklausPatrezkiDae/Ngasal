from os import system
def cls():
    return system('cls')

def iptnama(pesan):
    while True:
        ipt = input(pesan)
        if not ipt.isdigit():
            return ipt
        else:
            print("\n[WARNING] : Inputan Tidak Menerima Angka : ")

def password(pesan):
    ipt = input(pesan)
    return ipt

class User:
    def __init__(self,uName,pw):
        self.uName = uName
        self.pw = pw
    
    def showData(self):
        print(30*"=")
        print("User Name = ",self.uName)
        print("Password  = ",self.pw)
        print(30*"=")

cls()
cnt = 0
jwb = 'y'
while jwb == 'y':
    iptUname = iptnama("| > Masukkan Username : ")
    iptpw = password("| > Masukkan Password : ")

    user = User(iptUname,iptpw)
    cnt+=1
    jwb = input("input lagi? : ")

print(user.__dict__)



