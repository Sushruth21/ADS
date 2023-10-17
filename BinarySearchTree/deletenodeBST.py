#5. Write method to delete specified node from BST.

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def delete_node(root, key):
    if root is None:
        return root  

    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        root.key = find_min(root.right).key

        root.right = delete_node(root.right, root.key)

    return root

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def inorder_traversal(root):
    result = []
    if root:
        result += inorder_traversal(root.left)
        result.append(root.key)
        result += inorder_traversal(root.right)
    return result

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)

root = delete_node(root, 5)
assert inorder_traversal(root) == [3, 7, 10, 15, 18]

print("Deleted")
