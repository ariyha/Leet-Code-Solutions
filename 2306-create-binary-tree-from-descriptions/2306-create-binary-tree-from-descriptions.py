class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = None
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        created = {}
        for i,j,k in descriptions:
            if i not in created:
                node = TreeNode(i)
                created[i] = node
            else:
                node = created[i]

            if j in created:
                childnode = created[j]
            else:
                childnode = TreeNode(j)
                created[j] = childnode

            if k:
                node.left=childnode
            else:
                node.right=childnode
            childnode.parent = node
        
        x = created[descriptions[0][0]]

        while(x.parent):
            x = x.parent
        return x