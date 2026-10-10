# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        inorder_list = []
        self.helper(root,inorder_list)  
        return inorder_list[k-1]
    
    def helper(self, tree_node, inorder_list):
        if tree_node is None:
            return 
        
        self.helper(tree_node.left, inorder_list)
        inorder_list.append(tree_node.val)
        self.helper(tree_node.right, inorder_list)