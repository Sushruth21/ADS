#1. Design data structure for Binary Search Tree. Write methods for adding node into BST.

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if root is None:
            return TreeNode(key)

        if key < root.key:
            root.left = self._insert_recursive(root.left, key)
        else:
            root.right = self._insert_recursive(root.right, key)

        return root

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, root, result):
        if root:
            self._inorder_recursive(root.left, result)
            result.append(root.key)
            self._inorder_recursive(root.right, result)

bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

assert bst.inorder_traversal() == [20, 30, 40, 50, 60, 70, 80]

bst.insert(45)
bst.insert(35)
bst.insert(65)
bst.insert(75)

assert bst.inorder_traversal() == [20, 30, 35, 40, 45, 50, 60, 65, 70, 75, 80]

print("All assertions passed!")

