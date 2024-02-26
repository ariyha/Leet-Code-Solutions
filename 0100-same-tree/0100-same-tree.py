# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack1 =[p]
        stack2 = [q]
        visited = []

        while(stack1!=[]):
            x = stack1.pop(0)
            y = stack2.pop(0)

            if type(x)!=type(y):
                return False

            if x==None and y==None:
                return True

            if x.val!=y.val:
                return False
            
            if type(x.right)!=type(y.right) or type(x.left)!=type(y.left):
                return False
                        
            if x.right not in visited and x.right!=None:
                stack1.append(x.right)
                stack2.append(y.right)
                visited.append(x.right)
            
            if x.left not in visited and x.left!=None:
                stack1.append(x.left)
                stack2.append(y.left)
                visited.append(x.left)
        
        return True

