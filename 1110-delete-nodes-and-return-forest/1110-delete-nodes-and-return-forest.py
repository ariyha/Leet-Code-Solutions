class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.root = False
        self.parent = None
        self.lr  =0

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        root.root = True
        root.lr = 100
        print(root)
        tovisit = [root]
        nodes = []

        while(tovisit):
            x = tovisit.pop()
            print(x)
            print(x.val,end=' ')
            print(x.root)

            if x.val in to_delete:
                if x.lr ==1:
                    x.parent.right = None
                elif x.lr==2:
                    x.parent.left = None
                elif x.lr ==100:
                    pass
        
                if x.right:
                    print('right',x.right.val)
                    x.right.root = True
                    x.right.parent = x
                    x.right.lr = 1
                    tovisit.append(x.right)
                
                if x.left:
                    print('left',x.left.val)
                    x.left.root = True
                    x.left.parent = x
                    x.left.lr = 2
                    tovisit.append(x.left)
            else:
                if x.root:
                    nodes.append(x)
                
                if x.right:
                    x.right.root = False
                    x.right.parent = x
                    x.right.lr = 1
                    tovisit.append(x.right)
                
                if x.left:
                    x.left.parent = x
                    x.left.root = False
                    x.left.lr=2
                    tovisit.append(x.left)
        
        return nodes

