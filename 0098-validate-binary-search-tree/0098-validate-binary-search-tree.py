# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        io_list = []
        self.helper(root, io_list)

        for i in range(1, len(io_list)):
            if io_list[i] <= io_list[i - 1]:
                return False
        return True

    def helper(self, tree_node, io_list):
        if tree_node is None:
            return
        self.helper(tree_node.left, io_list)
        io_list.append(tree_node.val)
        self.helper(tree_node.right, io_list)