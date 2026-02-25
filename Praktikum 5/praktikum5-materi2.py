#================================================
# Nama : MUHAMMAD DAFFADHIYA WIRAWAN
# NIM : J0403251006
# KELAS : TPL B1
# PRAKTIKUM 5 : REKURSIF
#================================================

#================================================
# Materi rekursif : Calls Stack
# Tracing Bilangan (masuk-keluar)
#input 3
# 3-2-1 | 1-2-3
#================================================

def trace(n):
    if n == 0:
        print("Selesai")
        return
    
    print(f"Masuk: {n}") #menunjukkan saat masuk ke dalam fungsi dengan nilai n
    trace(n - 1) #memanggil fungsi trace dengan nilai n yang dikurangi
    print(f"Keluar: {n}") #menunjukkan saat keluar dari fungsi dengan nilai n


print("======Program Trace Calls Stack======")
trace(3) #memanggil fungsi trace dengan nilai awal 3    
