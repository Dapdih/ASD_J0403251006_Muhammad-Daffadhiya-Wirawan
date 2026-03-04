#================================================
# Nama : MUHAMMAD DAFFADHIYA WIRAWAN
# NIM : J0403251006
# KELAS : TPL B1
#================================================

#================================================
# Latihan 2 melengkapi Potongan Kode
#================================================
def insertion_sort(data):
 
 for i in range(1, len(data)):
    key = data[i]
    j = i - 1

 while j >= 0 and ______________________:
    data[j + 1] = data[j]
    j -= 1

    ______________________

    return data



#jawaban
def insertion_sort(data):
    #Loop mulai dari index ke 1
    for i in range(1, len(data)):
        key = data[i] #simpan nilai yang disisipkan

        j = i - 1 #index elemen sebelum key
        #Pindahkan elemen yang lebih besar dari key ke posisi setelahnya
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j] #geser elemen ke kanan
            j -= 1
        data[j + 1] = key 
    return data

def insertion_sort_desc(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] < key:  # Ubah > menjadi < untuk descending
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

angka = [12, 11, 13, 5, 6, 7]
print("Ascending :", insertion_sort(angka[:]))
print("Descending:", insertion_sort_desc(angka[:]))

# 1. Kondisi ascending: while j >= 0 and data[j] > key
#    Artinya geser elemen ke kanan selama elemen sebelumnya lebih besar dari key.
#
# 2. Untuk descending, ubah data[j] > key menjadi data[j] < key
#    Sehingga elemen yang lebih kecil dari key yang digeser ke kanan.
