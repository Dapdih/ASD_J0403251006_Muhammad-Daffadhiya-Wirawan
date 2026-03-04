#================================================
# Nama : MUHAMMAD DAFFADHIYA WIRAWAN
# NIM : J0403251006
# KELAS : TPL B1
#================================================

#================================================
# Merge Sort (Iterasi / Bottom-Up)
#================================================

def merge(data, left, mid, right):
    L = data[left:mid + 1]
    R = data[mid + 1:right + 1]
    i = j = 0
    k = left

    # Membandingkan elemen dari kedua bagian
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            data[k] = L[i]
            i += 1
        else:
            data[k] = R[j]
            j += 1
        k += 1

    # Menambahkan sisa elemen yang belum diproses
    while i < len(L):
        data[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        data[k] = R[j]
        j += 1
        k += 1

def MergesortIteratif(data):
    n = len(data)
    ukuran = 1  # Ukuran sub-array dimulai dari 1

    print("Data Awal:", data)
    print("=" * 50)

    step = 1
    # Iterasi: gandakan ukuran sub-array setiap langkah
    while ukuran < n:
        left = 0
        # Gabungkan sub-array berpasangan dengan ukuran saat ini
        while left < n - 1:
            mid = min(left + ukuran - 1, n - 1)
            right = min(left + 2 * ukuran - 1, n - 1)

            if mid < right:
                print(f"Langkah {step}: merge {data[left:mid+1]} dan {data[mid+1:right+1]}")
                merge(data, left, mid, right)
                print(f"Hasil: {data}")
                step += 1

            left += 2 * ukuran
        ukuran *= 2
        print("-" * 50)

    return data

angka = [38, 27, 43, 3, 9, 82, 10]
print("Hasil Merge Sort Iteratif (Ascending):", MergesortIteratif(angka))