class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        root.root = True
        tovisit = [root]
        nodes = []

        while(tovisit):
            x = tovisit.pop()

            if x.val in to_delete:
                if x.right:
                    x.right.root = True
                    tovisit.append(x.right)
                
                if x.left:
                    x.left.root = True
                    tovisit.append(x.left)
                
                continue

            if x.root:
                nodes.append(x)
            
            if x.right:
                x.right.root = False
                tovisit.append(x.right)
                if x.right.val in to_delete:
                    x.right = None

            
            if x.left:
                x.left.root = False
                tovisit.append(x.left)
                if x.left.val in to_delete:
                    x.left = None
        
    
        return nodes

