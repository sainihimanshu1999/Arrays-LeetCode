'''
Caution: when we are making tree from preorder and inorder, root.left comes firs
         when we are making tree from postorder and inorder, root.right comes first
'''

def buildTree(self,postorder,inorder):
    if inorder:
        index = inorder.index(postorder.pop())
        root = TreeNode(inorder[index])
        root.right = self.buildTree(inorder[index+1:],postorder)
        root.left = self.buildTree(inorder[:index],postorder)
        return root