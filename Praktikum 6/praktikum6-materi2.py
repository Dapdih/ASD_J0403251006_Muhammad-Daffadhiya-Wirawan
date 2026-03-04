#================================================
# Nama : MUHAMMAD DAFFADHIYA WIRAWAN
# NIM : J0403251006
# KELAS : TPL B1
#================================================

#================================================
# Insertion Sort dengan tracing
#================================================

def insertion_sort(data):
    #melihat data awal
    print("Data Awal: ", data)
    print("="*50)

    #Loop mulai dari index ke 1
    for i in range(1, len(data)):


        key = data[i] #simpan nilai yang disisipkan


        print("Iterasi ke-", i)
        print("Key yang disisipkan: ", key)
        print("Bagian kiri (sudah terurut): ", data[:i])
        print("Bagian kanan (belum terurut): ", data[i:])



        j = i - 1 #index elemen sebelum key
        #Pindahkan elemen yang lebih besar dari key ke posisi setelahnya
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j] #geser elemen ke kanan
            j -= 1
        data[j + 1] = key #tempatkan
        print("Setelah disisipkan: ", data)
        print("="*50)
    return data


angka = [12, 11, 13, 5, 6, 7]
print("Hasil Insertion Sort (Ascending):", insertion_sort(angka))

