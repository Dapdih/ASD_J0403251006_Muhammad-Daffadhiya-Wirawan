#================================================
# Nama : MUHAMMAD DAFFADHIYA WIRAWAN
# NIM : J0403251006
# KELAS : TPL B1
# PRAKTIKUM 4 : IMPLEMENTASI QUEUE
#================================================

#================================================
# Study kasus : Sistem Antrian Bengkel
# Implementasi Queue
# Enqueue : Menambahkan pelanggan ke dalam antrian
# Dequeue : Memanggil pelanggan paling depan untuk dilayani
# Front -> A -> B -> C -> Rear
#================================================

# 1) mendefinisikan node
class Node:
    def __init__(self, no_antrian, nama, jenis_servis):
        self.no_antrian = no_antrian      #menyimpan nomor antrian pada node
        self.nama = nama                  #menyimpan nama pelanggan pada node
        self.jenis_servis = jenis_servis  #menyimpan jenis servis pada node
        self.next = None                  #menyimpan referensi ke node berikutnya

# 2) mendefinisikan queue, terdiri dari front dan rear
class QueueBengkel:
    def __init__(self):
        self.front = None       #menyimpan referensi ke node paling depan
        self.rear = None        #menyimpan referensi ke node paling belakang
        self.no_antrian = 1     #nomor antrian otomatis dimulai dari 1

    def is_empty(self):
        return self.front is None  #mengembalikan True jika antrian kosong
    
    def enqueue(self, nama, jenis_servis):
        if not nama or not jenis_servis:
            print("Error: Nama pelanggan dan Jenis servis tidak boleh kosong.")
            return
        if not isinstance(nama, str) or not isinstance(jenis_servis, str):
            print("Error: Nama pelanggan dan Jenis servis harus berupa string.")
            return

        no = self.no_antrian
        new_node = Node(no, nama, jenis_servis)  #membuat node baru
        self.no_antrian += 1  #increment nomor antrian

        if self.is_empty():  #jika antrian kosong
            self.front = new_node  #set front dan rear ke node baru
            self.rear = new_node
        else:  #jika antrian tidak kosong
            self.rear.next = new_node  #set next dari rear ke node baru
            self.rear = new_node  #update rear ke node baru
        print(f"Pelanggan '{nama}' dengan No. Antrian {no} ({jenis_servis}) telah ditambahkan ke dalam antrian.")

    def dequeue(self):
        if self.is_empty(): #jika antrian kosong
            print("Antrian kosong, tidak ada pelanggan yang bisa dilayani.")
            return None

        no = self.front.no_antrian      #simpan nomor antrian dari node paling depan
        nama = self.front.nama          #simpan nama dari node paling depan
        jenis_servis = self.front.jenis_servis  #simpan jenis servis
        self.front = self.front.next    #update front ke node berikutnya
        if self.front is None: #jika setelah dequeue antrian menjadi kosong, set rear juga ke None
            self.rear = None

        return no, nama, jenis_servis #kembalikan data pelanggan yang di-dequeue

    def tampilkan(self):
        if self.is_empty():
            print("Antrian kosong.")
            return
        current = self.front #mulai dari front
        print("\n--- Daftar Antrian Bengkel ---")
        print(f"{'No.':<5} {'Nama Pelanggan':<20} {'Jenis Servis':<20}")
        print("-" * 45)
        while current is not None: #selama masih ada node yang bisa ditelusuri
            print(f"{current.no_antrian:<5} {current.nama:<20} {current.jenis_servis:<20}")
            current = current.next #pindah ke node berikutnya
        print("-" * 45)



def main():
    #instantiasi queue
    q = QueueBengkel()

    while True:
        try:
            print("\n====== Sistem Antrian Bengkel ======")
            print("1. Tambah Pelanggan")
            print("2. Layani Pelanggan")
            print("3. Lihat Antrian")
            print("4. Keluar")
            pilihan = input("Pilih menu (1-4): ").strip()
            if pilihan == '1':
                nama = input("Masukkan Nama Pelanggan: ").strip()
                jenis_servis = input("Masukkan Jenis Servis: ").strip()
                q.enqueue(nama, jenis_servis) #menambahkan pelanggan ke dalam antrian
            elif pilihan == '2':
                result = q.dequeue() #melayani pelanggan paling depan
                if result is not None:
                    no, nama, jenis_servis = result
                    print(f"Pelanggan No. {no} - '{nama}' ({jenis_servis}) sedang dilayani.")
            elif pilihan == '3':
                q.tampilkan() #menampilkan isi antrian
            elif pilihan == '4':
                print("Terima kasih telah menggunakan sistem antrian bengkel. Sampai jumpa!")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih menu 1-4.")
        except KeyboardInterrupt:
            print("\nProgram dihentikan oleh pengguna.")
            break
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
        
if __name__ == "__main__":
    main()

