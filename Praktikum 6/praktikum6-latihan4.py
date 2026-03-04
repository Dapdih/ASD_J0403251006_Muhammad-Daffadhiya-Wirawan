#================================================
# Nama : MUHAMMAD DAFFADHIYA WIRAWAN
# NIM : J0403251006
# KELAS : TPL B1
#================================================

#================================================
# Latihan 4 Merge Sort
#================================================
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


# 1. Base case adalah kondisi berhenti rekursi, yaitu ketika list berisi 1 atau 0 elemen (sudah terurut).
#
# 2. Fungsi memanggil dirinya sendiri (rekursi) untuk membagi list menjadi bagian lebih kecil hingga base case tercapai.
#
# 3. Fungsi merge() menggabungkan dua list yang sudah terurut menjadi satu list terurut.