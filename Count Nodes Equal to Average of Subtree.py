class Solution:    
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        count = 0
        def countNodes(node):
            if not node:
                return [0, 0]
            nonlocal count
            L_Nodes, L_Sum = countNodes(node.left)
            R_Nodes, R_Sum = countNodes(node.right)
            
            currNodes = L_Nodes + R_Nodes + 1
            currSum = L_Sum + R_Sum + node.val

            if node.val == currSum // currNodes:
                count += 1
            return [currNodes, currSum]

        countNodes(root)
        
        return count
