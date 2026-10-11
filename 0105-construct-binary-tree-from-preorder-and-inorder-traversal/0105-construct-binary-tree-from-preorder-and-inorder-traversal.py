# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        io_map = {val: i for i, val in enumerate(inorder)}

        def splitTree(root_index, left, right):
            if left > right:
                return None
            root = TreeNode(preorder[root_index])
            mid = io_map[preorder[root_index]]

            root.left = splitTree(root_index +1, left, mid - 1)
            root.right = splitTree(root_index + mid - left + 1, mid + 1, right)
            return root
        return splitTree(0, 0, len(inorder) - 1)