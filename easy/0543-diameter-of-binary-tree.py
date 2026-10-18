#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.max_diameter = 0
        self.dfs(root)

        return self.max_diameter
    
    def dfs(self, root):
        if root == None:
            return 0
        L = self.dfs(root.left)
        R = self.dfs(root.right)
        self.max_diameter = max(self.max_diameter, L + R)
        return 1 + max(L, R)