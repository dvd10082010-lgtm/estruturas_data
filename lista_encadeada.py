
from node import Node 

class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def append_node(self,elem):
        if self.head:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
           self.head = Node(elem)       
        self.size +=1

    def see_list(self):
        pointer = self.head
        while  pointer:
            print(pointer.data)
            pointer = pointer.next
           
    def search(self,elem):
        pointer = self.head
        cont = 0
        while  pointer:
            if pointer.data == elem:
                print(f"valor '{elem}' encontrado no indice : {cont}\n")
                return cont
            pointer = pointer.next
            cont += 1
        print(" valor não encontrado !")

    def get(self,index):
        pointer = self.head
        cont = -1
        try:
            while cont != index:
                cont +=1
                if index == cont:
                    print(f"valor encontrado no indice {index} é '{pointer.data}'")
                    return True
                    break
                else:
                    pointer = pointer.next
        except AttributeError:
            print("indice não encontrado nos nodes..")

    def transform(self,arr):
        for i in arr:
            self.append_node(i)
    

            
    def del_node(self, elem):
            pointer = self.head
            previous = None
            if elem == pointer.data:
                self.head = pointer.next
            else:
                while pointer:
                    if pointer.data == elem:
                        previous.next = pointer.next
                        break
                    previous = pointer
                    pointer = pointer.next
            self.size -= 1


    def  __len__(self):
        return self.size

list = LinkedList()


