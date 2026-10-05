# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        #base case 1
        if subRoot is None:
            return True
        #base case 2
        if root==None and subRoot!=None:
            return False
        #check for current tree
        if self.isSameTree(root,subRoot):
            return True
        #recursively check left and right subtrees
        l_c = self.isSubtree(root.left,subRoot)
        r_c = self.isSubtree(root.right,subRoot)
        return l_c or r_c
        
    #isSameTree function for checking subTree present or not
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p == None and q == None:
            return True
        if p == None or q == None or p.val!=q.val:
            return False
        l_c = self.isSameTree(p.left,q.left)
        r_c = self.isSameTree(p.right,q.right)
        return l_c and r_c