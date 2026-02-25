#================================================
# Nama : MUHAMMAD DAFFADHIYA WIRAWAN
# NIM : J0403251006
# KELAS : TPL B1
# PRAKTIKUM 4 : IMPLEMENTASI QUEUE
#================================================

#================================================
# Study kasus : Sistem Antrian Layanan pendidikan
# Implementasi Queue
# Enqueue : Menambahkan ke dalam antrian
# Dequeue : Memanggil yang paling depan untuk mendapatkan layanan
# Stack Front -> A -> B -> C -> Rear
# Front -> A -> Rear
#================================================

# 1) mendefinisikan node
class Node:
    def __init__(self, nim, nama):
        self.nim = nim  #menyimpan nilai nim pada node
        self.nama = nama  #menyimpan nilai nama pada node
        self.next = None  #menyimpan referensi ke node berikutnya

# 2) mendefinisikan queue, terdiri daari front dan rear
class QueueAkademik:
    def __init__(self):
        self.front = None  #menyimpan referensi ke node paling depan
        self.rear = None   #menyimpan referensi ke node paling belakang

    def is_empty(self):
        return self.front is None  #mengembalikan True jika antrian kosong
    
    def enqueue(self, nim, nama):
        new_node = Node(nim, nama)  #membuat node baru dengan nim dan nama yang diberikan

        if self.is_empty():  #jika antrian kosong
            self.front = new_node  #set front dan rear ke node baru
            self.rear = new_node
        else:  #jika antrian tidak kosong
            self.rear.next = new_node  #set next dari rear ke node baru
            self.rear = new_node  #update rear ke node baru

    def dequeue(self):
        if self.is_empty(): #jika antrian kosong
            print("Antrian kosong, tidak bisa dequeue")
            return None

        nim = self.front.nim  #simpan nim dari node paling depan
        nama = self.front.nama #simpan nama dari node paling depan
        self.front = self.front.next #update front ke node berikutnya
        if self.front is None: #jika setelah dequeue antrian menjadi kosong, set rear juga ke None
            self.rear = None

        return nim, nama #kembalikan nim dan nama yang di-dequeue
    
    def tampilkan(self):
        current = self.front #mulai dari front
        print("Front ->", end="")
        while current is not None: #selama masih ada node yang bisa ditelusuri
            print(f"[{current.nim}, {current.nama}] ->", end="") #tampilkan nim dan nama pada node saat ini
            current = current.next #pindah ke node berikutnya
        print("None <- Rear") #tampilkan akhir dari antrian



def main():
    #instantiasi queue
    q = QueueAkademik()

    while True:
        print("====== Sistem Antrian Layanan Pendidikan ======")
        print("1. Tambah Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Tampilkan Antrian")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ")
        if pilihan == '1':
            nim = input("Masukkan NIM: ")
            nama = input("Masukkan Nama: ")
            q.enqueue(nim, nama) #menambahkan mahasiswa ke dalam antrian
            print(f"Mahasiswa dengan NIM {nim} dan Nama {nama} telah ditambahkan ke dalam antrian.")
        elif pilihan == '2':
            result = q.dequeue() #melayani mahasiswa paling depan
            if result is not None:
                nim, nama = result
                print(f"Mahasiswa dengan NIM {nim} dan Nama {nama} telah dilayani.")
        elif pilihan == '3':
            q.tampilkan() #menampilkan isi antrian
        elif pilihan == '4':
            print("Terima kasih telah menggunakan sistem antrian. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu 1-4.")
        
if __name__ == "__main__":
    main()

