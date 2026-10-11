
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
            cont +=1
            if pointer.data == elem:
                print(f"valor encontrado no indice : {cont}")
                return True
                break
            pointer = pointer.next
            if pointer == None:
                print("valor não encontrado")
                return False
                break
        
    def transform(self,arr):
        for i in arr:
            self.append_node(i)
        return self


    def del_node(self, elem):
        pointer = self.head
        if elem == pointer.data:
            previous = pointer
            self.head = pointer.next
        else:
            while pointer:
                if pointer.data == elem:
                    previous.next = pointer.next
                    break
                previous = pointer
                pointer = pointer.next
        self.size -= 1


lista = LinkedList()

import array as arr

# 1. Array de números inteiros sequenciais simples (código 'i')
numeros_sequenciais = arr.array('i', [1, 2, 3, 4, 5,6,7,8,9,10])


lista.transform(numeros_sequenciais)
lista.del_node(10)
lista.see_list()