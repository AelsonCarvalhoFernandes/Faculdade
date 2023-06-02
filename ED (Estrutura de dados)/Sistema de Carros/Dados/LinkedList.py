from .Nodes.NodeList import Node


class LinkedList:
    def __init__(self) -> None:
        self.root : Node = None

    # Adicionar --------

    def append(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.recursive_append(self.root, value)

    
    def recursive_append(self, root, value):
        if root.next == None:
            root.next = Node(value)
            root.next.prev = root
        else:
            self.recursive_append(root.next, value)

    # Consultar --------

    def show(self, value=None):
        self.head = self.root

        if value == None:
            while self.head is not None:
                print(self.head.value)
                self.head = self.head.next
        else:
            while self.head is not None:
                if self.head.value == value:
                    print(f'O valor foi encontrado: {self.head.value}')
                    return True
                elif self.head.next is not None:
                    self.head = self.head.next
                else:
                    print('O valor procurado não está na lista')
                    return False
                
    # Alterar
    
    def change(self, value, new_value):
        self.head = self.root

        while self.head is not None:
            if self.head.value == value:
                self.head.value =new_value
                print('O valor foi alterado com sucesso')
                return True
            elif self.head.next is not None:
                self.head = self.head.next
            else:
                print('O valor procurado não está na lista')
                return False
            
    def delete(self, value):
        self.head = self.root

        while self.head is not None:
            if self.head.next.value == value:
                self.head.next = self.head.next.next
                return True
            
            elif self.head.next is not None:
                self.head = self.head.next

            else:
                print('O valor não foi encontrado')


            
