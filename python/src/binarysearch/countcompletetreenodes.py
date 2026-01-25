class CountCompleteTreeNodes:
    """
    Given the root of a complete binary tree, return the number of the nodes in the tree.

    According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree,
    and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes
    inclusive at the last level h.

    Design an algorithm that runs in less than O(n) time complexity.
    """

    def get_left_depth(self, node):
        depth = 0
        while node:
            depth += 1
            node = node.left
        return depth

    def get_right_depth(self, node):
        depth = 0
        while node:
            depth += 1
            node = node.right
        return depth

    def countNodes(self, root):
        if not root:
            return 0

        left_depth = self.get_left_depth(root)
        right_depth = self.get_right_depth(root)

        if left_depth == right_depth:
            return (2 ** left_depth) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
