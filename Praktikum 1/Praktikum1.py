#================================================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latuhan Dasar 1A : Membaca seluruh isi file
#================================================================

#Membuka filee dengan mode read ("r")
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    #Membaca seluruh isi file
    isi_file = file.read()
    
    #Menampilkan isi file ke layar
    print(isi_file)

    print("===Hasil Read===")
    print("tipe data", type(isi_file))
    print("jumlah baris", isi_file.count("\n") + 1)  # Menambahkan 1 untuk baris terakhir jika tidak berakhir dengan newline
    print("jumlah karakter", len(isi_file))

    #membuka file per baris

    print('===Membaca per baris===')
    jumlah_baris = 0
    with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
        for baris in file:
            jumlah_baris += 1
            print("Baris ke-", jumlah_baris)  
            print("isinya :", baris.strip())  # Menggunakan strip() untuk menghilangkan karakter newline di akhir baris

#============================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 2 : parsing baris menjadi kolom data
#============================================

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        #Menghapus karakter newline di akhir baris
        baris = baris.strip()
        
        #Memisahkan kolom data berdasarkan tanda koma
        nim, nama, nilai = baris.split(",")
        
        #Menampilkan hasil parsing
        print("NIM :", nim, "| Nama :", nama, "| Nilai :", nilai)

#============================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 3 : Membaca file dan menyimpan ke list
#============================================

data_list = [] #list kosong untuk menyimpan data mahasiswa

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        #Menghapus karakter newline di akhir baris
        baris = baris.strip()

        
        #Membuat dictionary untuk menyimpan data mahasiswa
        data_mahasiswa = [nim, nama, int(nilai)]

        #Menambahkan dictionary ke dalam list
        data_list.append(data_mahasiswa)
print("===Data Mahasiswa dalam List===")
print(data_list)
print("====jumlah record====")
print("jumlah record :", len(data_list))

print("===menampilkan contoh record===")
print("contoh Record pertama :", data_list[0])

#============================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 4 : Membaca file dan menyimpan ke dictionary
#============================================

data_dict = {} #dictionary kosong untuk menyimpan data mahasiswa

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        #Menghapus karakter newline di akhir baris
        baris = baris.strip()
        
        #Memisahkan kolom data berdasarkan tanda koma
        nim, nama, nilai = baris.split(",")
        
        #Membuat dictionary untuk menyimpan data mahasiswa
        data_mahasiswa = {
            "nama": nama,
            "nilai": int(nilai)
        }
        
        #Menambahkan dictionary ke dalam dictionary utama dengan NIM sebagai kunci
        data_dict[nim] = data_mahasiswa
print("===Data Mahasiswa dalam Dictionary===")
print(data_dict)
print("====jumlah record====")
print("jumlah record :", len(data_dict))
