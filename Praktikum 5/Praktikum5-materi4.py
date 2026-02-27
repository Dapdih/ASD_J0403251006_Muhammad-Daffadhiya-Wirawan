#================================================
# Nama : MUHAMMAD DAFFADHIYA WIRAWAN
# NIM : J0403251006
# KELAS : TPL B1
# PRAKTIKUM 5 : REKURSIF
#================================================

#================================================
# Materi rekursif : Kombinasi Biner (n)
#================================================

def biner(n, hasil=""):
    # Base case: jika string sudah n, print
    if len(hasil) == n:
        print(hasil)
        return
    # Rekursif: tambahkan '0' dan '1' ke hasil
    biner(n, hasil + '0')
    biner(n, hasil + '1')

biner(3) #memanggil fungsi biner dengan n = 3 untuk menghasilkan semua kombinasi biner dengan panjang 3