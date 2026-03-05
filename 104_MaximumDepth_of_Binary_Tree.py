class Solution:
    def maxDepth(self, root):
        if root ==None:
            return 0

        leftHeight = self.maxDepth(root.left)
        RightHeight = self.maxDepth(root.right)


        return max(leftHeight,RightHeight ) + 1
