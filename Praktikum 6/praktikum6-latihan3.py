#================================================
# Nama : MUHAMMAD DAFFADHIYA WIRAWAN
# NIM : J0403251006
# KELAS : TPL B1
#================================================

#================================================
# Latihan 3 Insertion Sort Tracing
#================================================

def insertion_sort(data):
    print("Data Awal:", data)
    print("=" * 50)

    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        print(f"Iterasi ke-{i}")
        print(f"  Key: {key}")
        print(f"  Bagian kiri (terurut) : {data[:i]}")
        print(f"  Bagian kanan (belum)  : {data[i:]}")

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            print(f"  Geser {data[j]} ke indeks {j + 1}")
            j -= 1

        data[j + 1] = key
        print(f"  Sisipkan {key} di indeks {j + 1}")
        print(f"  Hasil: {data}")
        print("-" * 50)

    return data

angka = [5, 2, 4, 6, 1, 3]
print("Hasil Insertion Sort:", insertion_sort(angka))

# 1. Setelah iterasi i=1: [2, 5, 4, 6, 1, 3] (key=2 disisipkan sebelum 5)
#
# 2. Setelah iterasi i=3: [2, 4, 5, 6, 1, 3] (key=6 tetap di tempatnya)
#
# 3. Pada iterasi i=4 (key=1), terjadi 4 kali pergeseran (6, 5, 4, 2 digeser ke kanan)