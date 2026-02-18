class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def delete_by_value(self, value):
        if not self.head:
            print("List kosong, tidak ada yang bisa dihapus.")
            return

        # Kasus 1: Node yang akan dihapus adalah Head
        if self.head.data == value:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            print(f"Node dengan nilai {value} berhasil dihapus.")
            return

        # Kasus 2: Mencari node di tengah atau di akhir
        current = self.head
        while current.next:
            if current.next.data == value:
                if current.next == self.tail:
                    self.tail = current
                
                current.next = current.next.next
                print(f"Node dengan nilai {value} berhasil dihapus.")
                return
            current = current.next

        print(f"Node dengan nilai {value} tidak ditemukan dalam list.")

    def display(self):
        if not self.head:
            print("Linked List: (Kosong)")
            return
        print("Linked List saat ini:", end=" ")
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# --- Program Utama ---
ll = LinkedList()

# Elemen yang sudah disediakan (Hardcoded)
elements = [10, 20, 30, 40, 50]
for item in elements:
    ll.insert_at_end(item)

# 1. Tampilkan List Awal
ll.display()

# 2. Minta input dari User
try:
    pilihan = int(input("Masukkan nilai elemen yang ingin Anda hapus: "))
    
    # 3. Jalankan fungsi hapus
    ll.delete_by_value(pilihan)
    
    # 4. Tampilkan List akhir
    ll.display()
except ValueError:
    print("Error: Harap masukkan angka yang valid!")