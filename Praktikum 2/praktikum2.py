#==========================================================
#3 Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 1: Membuat fungsi load data
#==========================================================

nama_file = "data_mahasiswa.txt"

def baca_data_mahasiswa(nama_file):
    data_dict = {}
    with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
        for baris in file:
        #Menghapus karakter newline di akhir baris
            baris = baris.strip()
            parts = baris.split(",")
            if len(parts) != 3:
                continue  # Lewati baris yang tidak sesuai format
            nim, nama, nilai_str = parts
            nilai_int = int(nilai_str)
            data_dict[nim] = {"nama": nama, "nilai": nilai_int}
    return data_dict


#buka_data = baca_data_mahasiswa(nama_file)
#print("jumlah data terbaca ", len(buka_data))


#==========================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 2: Membuat fungsi menampilkan data
#==========================================================

def tampilkan_data_mahasiswa(data_dict):
    if len(data_dict) == 0:
        print("Data mahasiswa kosong.")
        return 
    
    #membuat header table
    print("==== Daftar Mahasiswa ====")
    print(f"{'NIM':10} | {'Nama' : <12} | {'Nilai' : >5}")
    print("-" * 32)
    
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim:10} | {nama : <12} | {nilai : >5}")
        
#memanggil fungsi menampilkan data
#tampilkan_data_mahasiswa(buka_data)



#==========================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 3: Membuat fungsi mencari data
#==========================================================

def cari_data_mahasiswa(data_dict):
    #mencari data mahasiswa berdasarkan NIM
    nim_cari = input("Masukkan NIM yang dicari: ").strip()
    
    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]
        
        print("\n==== Data mahasiswa ditemukan ====")
        print(f"NIM   : {nim_cari}")
        print(f"Nama  : {nama}")
        print(f"Nilai : {nilai}")
    else:
        print("\nData mahasiswa tidak ditemukan.")

#memanggil fungsi mencari data
#cari_data_mahasiswa(buka_data)   


#==========================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 4: Membuat fungsi update nilai
#==========================================================

def update_nilai_mahasiswa(data_dict):
    nim_update = input("Masukkan NIM yang akan diupdate nilainya: ").strip()
    
    if nim_update in data_dict:
        nama = data_dict[nim_update]["nama"]
        nilai_lama = data_dict[nim_update]["nilai"]
        
        print(f"\nData mahasiswa ditemukan:")
        print(f"NIM   : {nim_update}")
        print(f"Nama  : {nama}")
        print(f"Nilai lama : {nilai_lama}")
        
        try:
            nilai_baru = int(input("Masukkan nilai baru: ").strip())
            data_dict[nim_update]["nilai"] = nilai_baru
            print("\nNilai berhasil diupdate.")
        except ValueError:
            print("Input nilai tidak valid. Harus berupa angka.")
    else:
        print("\nData mahasiswa tidak ditemukan.")
    print(f"Update berhasil. Nilai {nim_update} sekarang adalah {data_dict.get(nim_update, {}).get('nilai', 'N/A')}")

#update_nilai_mahasiswa(buka_data)        


#==========================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 5: Membuat fungsi menyimpan data
#==========================================================

def simpan_data_mahasiswa(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            baris = f"{nim},{nama},{nilai}\n"
            file.write(baris)
    print(f"\nData berhasil disimpan ke file {nama_file}.")
    
#memanggil fungsi menyimpan data
#simpan_data_mahasiswa(nama_file, buka_data)
#print("Data berhasil disimpan.")



#==========================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 6: Membuat Menu
#==========================================================


def main():
    
    #menjalankan fungsi 1 load data
    buka_data = baca_data_mahasiswa(nama_file)
    
    while True:
        print("\n==== Menu Data Mahasiswa ====")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Mahasiswa")
        print("3. Update Nilai Mahasiswa")
        print("4. Simpan Data Mahasiswa")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ").strip()
        
        if pilihan == "1":
            tampilkan_data_mahasiswa(buka_data)
        elif pilihan == "2":
            cari_data_mahasiswa(buka_data)
        elif pilihan == "3":
            update_nilai_mahasiswa(buka_data)
        elif pilihan == "4":
            simpan_data_mahasiswa(nama_file, buka_data)
        elif pilihan == "5":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
    
