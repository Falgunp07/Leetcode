class Solution:
    def __init__(self):
        self.ans = True
    def height(self, root) -> int:
        if root ==None:
            return 0

        leftHeight = self.height(root.left)
        RightHeight = self.height(root.right)

        if abs(leftHeight-RightHeight)>1:
            self.ans = False


        return max(leftHeight,RightHeight ) + 1
    def isBalanced(self, root) -> bool:
        self.height(root)
        return self.ans