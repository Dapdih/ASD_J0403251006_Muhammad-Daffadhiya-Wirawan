#================================================
# Nama : MUHAMMAD DAFFADHIYA WIRAWAN
# NIM : J0403251006
# KELAS : TPL B1
# PRAKTIKUM 5 : REKURSIF
#================================================

#================================================
# Studi Kasus : Generator Pin
#================================================

def generator(panjang, hasil=""):
    if len(hasil) == panjang:
        print(hasil)
        return
    
    for angka in ["0", "1", "2"]:
        generator(panjang, hasil + angka)

generator(3)

# Total kombinasi = 3^panjang (3 pilihan angka per posisi, sebanyak panjang posisi)
# generator(3) → 3^3 = 27 hasil: 000, 001, 002, ..., 222