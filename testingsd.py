def huruf(pesan):
    while True:
        ipt = input(pesan)
        if not ipt.isdigit():
            return ipt
        else:
            print("\n Masukkan Huruf Saja")