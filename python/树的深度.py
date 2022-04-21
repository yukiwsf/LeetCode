def Depth(self, root):
    if not root:
        return 0
    left = Depth(root.left)
    right = Depth(root.right)
    return (left if left >= right else right) + 1