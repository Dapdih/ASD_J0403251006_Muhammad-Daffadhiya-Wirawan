#================================================
# Nama : MUHAMMAD DAFFADHIYA WIRAWAN
# NIM : J0403251006
# KELAS : TPL B1
# PRAKTIKUM 5 : REKURSIF
#================================================

#================================================
# Materi rekursif : Faktorial
#================================================

def faktorial(n):
    #definisikan base case
    if n <= 1:
        return 1
    #definisikan recursive case
    return n * faktorial(n - 1)

print("======Program Faktorial======")
print("Hasil Faktorial : ", faktorial(100))