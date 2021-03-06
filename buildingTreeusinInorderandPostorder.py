'''
In this question we make use of recursive calls and slicing of the array
'''

def buildTree(self,preorder,inorder):
    if inorder:
        index = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[index])
        root.left = self.buildTree(preorder,inorder[:index])
        root.right = self.buildTree(preorder,inorder[index+1:])

        return root