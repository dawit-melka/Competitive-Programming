class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        def insertVal(node, val):
                if val > node.val:
                    if not node.right:
                        node.right = TreeNode(val)
                        return
                    insertVal(node.right, val)
                else:
                    if not node.left:
                        node.left = TreeNode(val)
                        return
                    insertVal(node.left, val)
        
        for i in range(1, len(preorder)):
            insertVal(root, preorder[i])
        
        return root
