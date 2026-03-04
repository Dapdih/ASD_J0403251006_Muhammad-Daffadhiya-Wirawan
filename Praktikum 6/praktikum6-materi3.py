#================================================
# Nama : MUHAMMAD DAFFADHIYA WIRAWAN
# NIM : J0403251006
# KELAS : TPL B1
#================================================

#================================================
# Merge Sort
#================================================

def Mergesort(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2 # Menentukan titik tengah
    L = data[:mid] # Membagi data menjadi dua bagian
    R = data[mid:]
    LSOrt = Mergesort(L) # Rekursif untuk bagian kiri
    RSOrt = Mergesort(R) # Rekursif untuk bagian kanan

    return merge(LSOrt, RSOrt) # Menggabungkan hasil yang sudah terurut

def merge(left, right):
    result = []
    i = j = 0

    #membandingkan elemen dari kedua bagian dan menambahkannya ke hasil
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    #menambahkan sisa elemen yang belum diproses dari kedua bagian

    result.extend(left[i:]) # Menambahkan sisa elemen kiri
    result.extend(right[j:]) # Menambahkan sisa elemen kanan
    return result

angka = [38, 27, 43, 3, 9, 82, 10]
print("Hasil Merge Sort (Ascending):", Mergesort(angka))