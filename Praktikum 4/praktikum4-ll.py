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

#Membuat class Node (Merupakan unit dasar dari Linked List)
class Node:
    def __init__ (self, data):
        self.data = data #menyimpan nilai pada node
        self.next = None #pointer ke node berikutnya

# 1) Membuat node satu per satu
nodeA = Node("A")
nodeB = Node("B") 
nodeC = Node("C") 

# 2) Menghubungkan node-node tersebut
nodeA.next = nodeB #Node A menunjuk ke Node B   
nodeB.next = nodeC #Node B menunjuk ke Node C

# 3) menentukan node pertama (head)
head = nodeA #Node A adalah head (awal dari linked list)

# 4) Traversal (menelusuri linked list)
current = head #Mulai dari head
while current is not None: #Selama masih ada node yang bisa ditelusuri
    print(current.data) #Cetak data pada node saat ini
    current = current.next #Pindah ke node berikutnya


#=======================================================
# Implementasi Dasar : Linked List + Insert Awal
#=======================================================

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_awal(self, data):
        # 1) buat node baru
        nodeBaru = Node(data) #Membuat node baru dengan data yang diberikan
        
        # 2) node baru menunjuk ke head lama
        nodeBaru.next = self.head #Node baru menunjuk ke head saat ini
        
        # 3) update head untuk menunjuk ke node baru
        self.head = nodeBaru #Node baru menjadi head (awal dari linked list)

    def tampilkan(self): #implementasi traversal
        current = self.head #Mulai dari head
        while current is not None: #Selama masih ada node yang bisa ditelusuri
            print(current.data) #Cetak data pada node saat ini
            current = current.next #Pindah ke node berikutnya

    def hapus_awal(self):
        data_terhapus = self.head.data
        #menggeser head
        self.head = self.head.next
        print("Node yang dihapus adalah :", data_terhapus)

print("=== Linked List dengan Insert Awal ===")
ll = LinkedList() # instantiasi objek ke class LinkedList
ll.insert_awal("X") # Menambahkan node dengan data "X" di awal linked list
ll.insert_awal("Y") # Menambahkan node dengan data "Y" di awal linked list
ll.insert_awal("Z") # Menambahkan node dengan data "Z" di awal linked list
ll.hapus_awal() # Menghapus node di awal linked list
ll.tampilkan() # Menampilkan isi linked list setelah penghapusan