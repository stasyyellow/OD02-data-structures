#бинарное дерево

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

root = Node(45)
root = insert(root, 30)
root = insert(root, 56)
root = insert(root, 20)
root = insert(root, 35)
