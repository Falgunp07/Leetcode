class Solution:
    def insertIntoBST(self, root, target):
        newNode = TreeNode(target)
        if root is None:
            return newNode


        curr = root
        while curr!=None:
            if target<curr.val:

                if curr.left!=None:
                    curr = curr.left
                else:
                    curr.left = newNode
                    break
            else:
                if curr.right!=None:
                    curr = curr.right
                else:
                    curr.right = newNode
                    break

        return root