class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        def insertVal(node, val):
                if not node: return TreeNode(val)

                if val > node.val:
                    node.right = insertVal(node.right, val)
                else:
                    node.left = insertVal(node.left, val)
                
                return node
        
        for i in range(1, len(preorder)):
            insertVal(root, preorder[i])
        
        return root
