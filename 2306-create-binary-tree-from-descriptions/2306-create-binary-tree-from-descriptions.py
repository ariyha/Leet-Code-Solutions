# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.ischild = False
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
            childnode.ischild = True
            
            if not node.ischild:
                root = node
            

            print(root.val)

            if i[2]:
                node.left=childnode
            else:
                node.right=childnode
        
        return created[38]
