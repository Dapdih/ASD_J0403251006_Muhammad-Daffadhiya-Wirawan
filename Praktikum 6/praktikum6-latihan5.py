#================================================
# Nama : MUHAMMAD DAFFADHIYA WIRAWAN
# NIM : J0403251006
# KELAS : TPL B1
#================================================

#================================================
# Latihan 5 melengkapi Fungsi Merge
#================================================
def merge(left, right):
    
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
     
        if __________________________:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result



# jawaban
def merge_sort(data):
    if len(data) <= 1:
        return data
    
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

angka = [38, 27, 43, 3, 9, 82, 10]
print("Hasil Merge Sort (Ascending):", merge_sort(angka))

# 1. Kondisi ascending: if left[i] < right[j]
#    Elemen yang lebih kecil dimasukkan duluan ke result sehingga hasilnya terurut dari kecil ke besar.
#
# 2. result.extend() menambahkan sisa elemen yang belum diproses ke result.
#    Setelah salah satu list habis, elemen sisanya pasti sudah terurut dan langsung ditambahkan.