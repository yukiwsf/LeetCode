def InvertTree(self, root):
    if not root:
        return
    tmp = root.left
    root.left = InvertTree(self, root.right)
    root.right = InvertTree(self, tmp)
    return root

