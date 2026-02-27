#================================================
# Nama : MUHAMMAD DAFFADHIYA WIRAWAN
# NIM : J0403251006
# KELAS : TPL B1
# PRAKTIKUM 5 : REKURSIF
#================================================

#================================================
# Latihan 4 : Kombinasi Huruf
#================================================
def kombinasi(n, hasil=""):
    if len(hasil) == n:
        print(hasil)
        return
    
    kombinasi(n, hasil + 'A')
    kombinasi(n, hasil + 'B')

kombinasi(2)

# Total kombinasi = 2^n (2 pilihan huruf per posisi, sebanyak n posisi)
# kombinasi(2) → 2^2 = 4 hasil: AA, AB, BA, BB