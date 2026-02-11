class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        elems = []
        while temp:
            elems.append(str(temp.data))
            temp = temp.next
        if elems:
            print(" -> ".join(elems) + " -> None")
        else:
            print("None")

    # --- Latihan 4: Menggabungkan dua linked list ---
    def merge(self, other_list):
        # Jika list pertama kosong, maka hasilnya adalah list kedua
        if not self.head:
            self.head = other_list.head
            return

        # Jika list kedua kosong, tidak ada yang perlu dilakukan
        if not other_list.head:
            return

        # Cari node terakhir di list pertama
        temp = self.head
        while temp.next:
            temp = temp.next
        
        # Sambungkan node terakhir list pertama ke head list kedua
        temp.next = other_list.head


def _parse_elements(s: str):
    parts = [p.strip() for p in s.split(',') if p.strip()]
    vals = []
    for p in parts:
        try:
            vals.append(int(p))
        except ValueError:
            vals.append(p)
    return vals


def main():
    print("Latihan 4: Gabungkan dua Single Linked List")
    s1 = input("Masukkan elemen List A (pisahkan dengan koma): ").strip()
    if not s1:
        print("Tidak ada elemen untuk List A. Program dihentikan.")
        return
    s2 = input("Masukkan elemen List B (pisahkan dengan koma): ").strip()
    if not s2:
        print("Tidak ada elemen untuk List B. Program dihentikan.")
        return

    arr1 = _parse_elements(s1)
    arr2 = _parse_elements(s2)

    list1 = LinkedList()
    for v in arr1:
        list1.insert_at_end(v)

    list2 = LinkedList()
    for v in arr2:
        list2.insert_at_end(v)

    print("List A:", end=" ")
    list1.display()
    print("List B:", end=" ")
    list2.display()

    print("\nMenggabungkan List A dan List B...")
    list1.merge(list2)

    print("Hasil Penggabungan:", end=" ")
    list1.display()


if __name__ == "__main__":
    main()