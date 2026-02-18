#==========================================================
# Program Manajemen Stok Barang
# Menggunakan Dictionary untuk menyimpan data stok barang
#==========================================================

nama_file = "stok_barang.txt"

#==========================================================
# Fungsi 1: Membaca data stok barang dari file
#==========================================================

def baca_stok_barang(nama_file):
    """Membaca data stok barang dari file txt"""
    data_dict = {}
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()
                if not baris:  # Skip baris kosong
                    continue
                parts = baris.split(",")
                if len(parts) != 3:
                    continue  # Lewati baris yang tidak sesuai format
                kode_barang, nama_barang, stok_str = parts
                try:
                    stok = int(stok_str)
                    data_dict[kode_barang] = {"nama": nama_barang, "stok": stok}
                except ValueError:
                    continue
    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan. Program akan membuat file baru saat data disimpan.")
    return data_dict


#==========================================================
# Fungsi 2: Menampilkan semua barang
#==========================================================

def tampilkan_semua_barang(data_dict):
    """Menampilkan seluruh data stok barang"""
    if len(data_dict) == 0:
        print("Data stok barang kosong.")
        return 
    
    print("\n==== Daftar Stok Barang ====")
    print(f"{'Kode Barang':12} | {'Nama Barang':20} | {'Stok':>6}")
    print("-" * 42)
    
    for kode in sorted(data_dict.keys()):
        nama = data_dict[kode]["nama"]
        stok = data_dict[kode]["stok"]
        print(f"{kode:12} | {nama:20} | {stok:>6}")
    print()



#==========================================================
# Fungsi 3: Mencari barang berdasarkan kode
#==========================================================

def cari_barang(data_dict):
    """Mencari data barang berdasarkan kode barang"""
    kode_cari = input("Masukkan kode barang yang dicari: ").strip()
    
    if kode_cari in data_dict:
        nama = data_dict[kode_cari]["nama"]
        stok = data_dict[kode_cari]["stok"]
        
        print("\n==== Data barang ditemukan ====")
        print(f"Kode Barang : {kode_cari}")
        print(f"Nama Barang : {nama}")
        print(f"Stok        : {stok}")
        print()
    else:
        print("\nBarang tidak ditemukan.\n")   


#==========================================================
# Fungsi 4: Tambah barang baru
#==========================================================

def tambah_barang_baru(data_dict):
    """Menambah data barang baru ke dalam dictionary"""
    kode_barang = input("Masukkan kode barang: ").strip()
    
    if kode_barang in data_dict:
        print("\nKode sudah digunakan.\n")
        return
    
    nama_barang = input("Masukkan nama barang: ").strip()
    
    try:
        stok_awal = int(input("Masukkan stok awal: ").strip())
        if stok_awal < 0:
            print("\nStok tidak boleh negatif.\n")
            return
        
        data_dict[kode_barang] = {"nama": nama_barang, "stok": stok_awal}
        print(f"\nBarang '{nama_barang}' dengan kode '{kode_barang}' berhasil ditambahkan.\n")
    except ValueError:
        print("\nInput stok tidak valid. Harus berupa angka.\n")        


#==========================================================
# Fungsi 5: Update stok barang
#==========================================================

def update_stok_barang(data_dict):
    """Update stok barang (tambah atau kurangi)"""
    kode_update = input("Masukkan kode barang yang akan diupdate: ").strip()
    
    if kode_update not in data_dict:
        print("\nBarang tidak ditemukan.\n")
        return
    
    nama = data_dict[kode_update]["nama"]
    stok_lama = data_dict[kode_update]["stok"]
    
    print(f"\nData barang ditemukan:")
    print(f"Kode Barang : {kode_update}")
    print(f"Nama Barang : {nama}")
    print(f"Stok saat ini: {stok_lama}")
    
    print("\nPilih operasi:")
    print("1. Tambah stok")
    print("2. Kurangi stok")
    
    operasi = input("Pilih operasi (1-2): ").strip()
    
    if operasi not in ["1", "2"]:
        print("\nOperasi tidak valid.\n")
        return
    
    try:
        jumlah = int(input("Masukkan jumlah: ").strip())
        if jumlah < 0:
            print("\nJumlah tidak boleh negatif.\n")
            return
        
        if operasi == "1":
            data_dict[kode_update]["stok"] += jumlah
            print(f"\nStok berhasil ditambah. Stok baru: {data_dict[kode_update]['stok']}\n")
        else:  # operasi == "2"
            stok_baru = data_dict[kode_update]["stok"] - jumlah
            if stok_baru < 0:
                print(f"\nStok tidak boleh negatif. Stok saat ini: {stok_lama}\n")
            else:
                data_dict[kode_update]["stok"] = stok_baru
                print(f"\nStok berhasil dikurangi. Stok baru: {stok_baru}\n")
    except ValueError:
        print("\nInput jumlah tidak valid. Harus berupa angka.\n")


#==========================================================
# Fungsi 6: Simpan data ke file
#==========================================================

def simpan_stok_barang(nama_file, data_dict):
    """Menyimpan data stok barang ke file txt"""
    try:
        with open(nama_file, "w", encoding="utf-8") as file:
            for kode in sorted(data_dict.keys()):
                nama = data_dict[kode]["nama"]
                stok = data_dict[kode]["stok"]
                baris = f"{kode},{nama},{stok}\n"
                file.write(baris)
        print(f"\nData berhasil disimpan ke file {nama_file}.\n")
    except Exception as e:
        print(f"\nGagal menyimpan file: {e}\n")


#==========================================================
# Fungsi 7: Menu utama
#==========================================================

def main():
    """Fungsi utama untuk menjalankan program"""
    
    # Load data stok barang dari file
    stok_barang = baca_stok_barang(nama_file)
    
    while True:
        print("\n==== Menu Stok Barang ====")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")
        
        pilihan = input("Pilih menu (0-5): ").strip()
        
        if pilihan == "1":
            tampilkan_semua_barang(stok_barang)
        elif pilihan == "2":
            cari_barang(stok_barang)
        elif pilihan == "3":
            tambah_barang_baru(stok_barang)
        elif pilihan == "4":
            update_stok_barang(stok_barang)
        elif pilihan == "5":
            simpan_stok_barang(nama_file, stok_barang)
        elif pilihan == "0":
            print("\nProgram selesai.")
            break
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.\n")


if __name__ == "__main__":
    main()