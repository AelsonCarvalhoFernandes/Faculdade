from .Nodes.NodeTree import Node

class Tree:
    def __init__(self) -> None:
        self.root = None

    def append(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.recurssive_append(self.root, value)

    def recurssive_append(self, root, value):
        if root.value < value:
            if root.right == None:
                root.right = Node(value)
                print(root.value)
            else:
                self.recurssive_append(root.right, value)
        
        elif root.value > value:
            if root.left == None:
                root.left = Node(value)
                print(root.value)
            else:
                self.recurssive_append(root.left, value)

        
    def recursive_delete(self, root, value):
        if root.value < value:
            if root.right is not None:
                self.recursive_delete(root.right, value)
        elif root.value > value:
            if root.left is not None:
                self.recursive_delete(root.left, value)
        else:
            if root.right.left is not None:
                

