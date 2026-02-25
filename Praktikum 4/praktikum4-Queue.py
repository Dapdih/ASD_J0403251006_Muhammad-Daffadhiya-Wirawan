#=======================================================
# PERTEMUAN 4 - LINKED LIST STACK QUEUE
#
# NAMA : MUHAMMAD DAFFADHIYA WIRAWAN
# NIM : J0403251006
# KELAS : TPL B1
#=======================================================

#=======================================================
# Implementasi Dasar : Node pada Linked List
#=======================================================

class Node:
    def __init__(self, data):
        self.data = data  #menyimpan nilai pada node
        self.next = None  #pointer ke node berikutnya

#=======================================================
# Implementasi Dasar : Queue pada Linked List
#=======================================================

class QueueLL:
    def __init__(self):
        self.front = None #Pointer ke elemen depan (front) dari queue
        self.rear = None  #Pointer ke elemen belakang (rear) dari queue
    
    def is_empty(self):
        return self.front is None #Queue kosong jika front adalah None
    
    def enqueue(self, data):
        nodeBaru = Node(data) #Membuat node baru dengan data yang diberikan
        
        if self.is_empty() :
            self.front = nodeBaru #Jika queue kosong, front dan rear menunjuk ke node baru
            self.rear = nodeBaru
            return
        
        self.rear.next = nodeBaru #Node rear saat ini menunjuk ke node baru
        self.rear = nodeBaru #Node baru menjadi rear (belakang) dari queue

    def dequeue(self):
        if self.is_empty():
            print("Queue kosong, tidak bisa dequeue")
            return None
        # 1) ambil data yang paling depan
        data = self.front.data #Simpan data dari front yang akan di-dequeue

        # 2) pindahkan front ke node berikutnya
        self.front = self.front.next #Pindahkan front ke node berikutnya
        
        # 3) jika setelah dequeue queue menjadi kosong, set rear juga ke None
        if self.front is None: #Jika setelah dequeue queue menjadi kosong, set rear juga ke None
            self.rear = None
        
        return data #Kembalikan data yang di-dequeue 

    def tampilkan(self):
        current = self.front #Mulai dari front (depan) queue
        print("Front ->", end="")
        while current is not None: #Selama masih ada node yang bisa ditelusuri
            print(current.data, end='->') #Cetak data pada node saat ini
            current = current.next #Pindah ke node berikutnya
        print("none <- rear")
q = QueueLL() #Membuat instance dari QueueLL
q.enqueue("A") #Menambahkan elemen "A" ke dalam queue
q.enqueue("B") #Menambahkan elemen "B" ke dalam queue
q.enqueue("C") #Menambahkan elemen "C" ke dalam queue
q.tampilkan() #Menampilkan isi queue (harus menampilkan "A")
q.dequeue() #Menghapus elemen pertama dari queue
q.tampilkan() #Menampilkan isi queue setelah dequeue (harus menampilkan "B")