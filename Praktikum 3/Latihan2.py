class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

    def search(self, key):
        if not self.head:
            print("Circular Linked List kosong. Tidak ada elemen yang bisa dicari.")
            return

        current = self.head
        while True:
            if current.data == key:
                print(f"Elemen {key} ditemukan dalam Circular Linked List.")
                return
            current = current.next
            # Kembali ke awal, artinya sudah satu putaran penuh
            if current == self.head:
                break
        
        print(f"Elemen {key} tidak ditemukan dalam Circular Linked List.")

def _parse_elements(input_str):
    parts = [p.strip() for p in input_str.split(',') if p.strip()]
    vals = []
    for p in parts:
        try:
            vals.append(int(p))
        except ValueError:
            vals.append(p)
    return vals


def main():
    s = input("Masukkan elemen untuk Circular Linked List (pisahkan dengan koma): ").strip()
    if not s:
        print("Tidak ada elemen yang dimasukkan. Program selesai.")
        return

    elements = _parse_elements(s)
    cll = CircularLinkedList()
    for e in elements:
        cll.insert_at_end(e)

    key_input = input("Masukkan elemen yang ingin dicari: ").strip()
    if not key_input:
        print("Tidak ada nilai yang dimasukkan untuk pencarian. Program selesai.")
        return
    try:
        key = int(key_input)
    except ValueError:
        key = key_input

    cll.search(key)


if __name__ == "__main__":
    main()