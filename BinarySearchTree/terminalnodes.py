#4. Write method to count number of terminal nodes.

class Treenode:
    def __init__(self,key):
        self.key = key
        self.right = None
        self.left = None

def countTerminal(root):
    if root is None:
        return 0
    if root.right is None and root.left is None:
        return 1
    left_count = countTerminal(root.left)
    right_count = countTerminal(root.right)
    return left_count + right_count
    
#testing
root = Treenode(15)
root.left = Treenode(5)
root.right = Treenode(7)
root.left.left = Treenode(8)
root.left.right = Treenode(9)
root.right.right = Treenode(10)

assert countTerminal(root) == 3

print("all assertions passed!")
