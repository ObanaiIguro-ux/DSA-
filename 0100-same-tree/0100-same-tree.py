# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p == None and q == None:
            return True
        if p == None or q == None or p.val!=q.val:
            return False
        l_c = self.isSameTree(p.left,q.left)
        r_c = self.isSameTree(p.right,q.right)
        return l_c and r_c