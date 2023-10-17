#3. Write method to find the height of BST.

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_height(root):
    if root is None:
        return -1  

    left_height = find_height(root.left)
    right_height = find_height(root.right)

    return max(left_height, right_height) + 1

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)

assert find_height(root) == 2  

root2 = TreeNode(5)
root2.left = TreeNode(3)
root2.right = TreeNode(8)
root2.left.left = TreeNode(2)
root2.left.right = TreeNode(4)

assert find_height(root2) == 2 

print("All assertions passed!")
