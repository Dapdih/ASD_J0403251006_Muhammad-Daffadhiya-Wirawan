#================================================
# Nama : MUHAMMAD DAFFADHIYA WIRAWAN
# NIM : J0403251006
# KELAS : TPL B1
#================================================

#================================================
# Insertion Sort (Ascending)
#================================================

def insertion_sort(data):
    #Loop mulai dari index ke 1
    for i in range(1, len(data)):
        key = data[i] #simpan nilai yang disisipkan

        j = i - 1 #index elemen sebelum key
        #Pindahkan elemen yang lebih besar dari key ke posisi setelahnya
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j] #geser elemen ke kanan
            j -= 1
        data[j + 1] = key #tempatkan
    return data

angka = [12, 11, 13, 5, 6, 7]
print("Hasil Insertion Sort (Ascending):", insertion_sort(angka))

# 1. Mengapa perulangan dimulai dari indeks 1?
#    Karena elemen indeks 0 dianggap sudah terurut, sehingga proses penyisipan dimulai dari indeks 1.
#
# 2. Apa fungsi variabel key?
#    Menyimpan nilai elemen yang sedang disisipkan agar tidak hilang saat elemen lain digeser.
#
# 3. Mengapa digunakan while, bukan for?
#    Karena jumlah pergeseran tidak pasti, while lebih fleksibel untuk berhenti sesuai kondisi.
#
# 4. Operasi apa yang terjadi di dalam while?
#    Elemen yang lebih besar dari key digeser ke kanan satu posisi hingga ditemukan posisi yang tepat.