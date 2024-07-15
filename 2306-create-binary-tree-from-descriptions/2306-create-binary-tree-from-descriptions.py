# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = None
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        created = {}
        root = None
        for i in descriptions:
            if i[0] not in created:
                node = TreeNode(i[0])
                created[i[0]] = node
            else:
                node = created[i[0]]

            if i[1] in created:
                childnode = created[i[1]]
            else:
                childnode = TreeNode(i[1])
                created[i[1]] = childnode
                     
            if i[2]:
                node.left=childnode
            else:
                node.right=childnode
            childnode.parent = node
        
        x = descriptions[0][0]

        x = created[x]

        while(x.parent):
            x = x.parent
        
        return x
