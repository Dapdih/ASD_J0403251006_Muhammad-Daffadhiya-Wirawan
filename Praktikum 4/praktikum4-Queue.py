#=======================================================
# PERTEMUAN 4 - LINKED LIST STACK QUEUE
#
# NAMA : MUHAMMAD DAFFADHIYA WIRAWAN
# NIM : J0403251006
# KELAS : TPL B1
#=======================================================

#=======================================================
# Implementasi Dasar : Queue pada Linked List
#=======================================================

class QueueLL:
    def __init__(self):
        self.front = None #Pointer ke elemen depan (front) dari queue
        self.rear = None  #Pointer ke elemen belakang (rear) dari queue
    
    def enqueue(self, data):
        nodeBaru = Node(data) #Membuat node baru dengan data yang diberikan
        if self.rear is None: #Jika queue kosong
            self.front = nodeBaru #Node baru menjadi front
            self.rear = nodeBaru  #Node baru juga menjadi rear
        else:
            self.rear.next = nodeBaru #Rear lama menunjuk ke node baru
            self.rear = nodeBaru      #Node baru menjadi rear