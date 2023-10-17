#6. Write method to traverse the BST in descending order.

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def reverse_inorder_traversal(root):
    result = []
    if root:
        result += reverse_inorder_traversal(root.right)
        result.append(root.key)
        result += reverse_inorder_traversal(root.left)
    return result

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)

assert reverse_inorder_traversal(root) == [18, 15, 10, 7, 5, 3]

print("Reverse Inorder Traversal done!")
