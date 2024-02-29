# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        d=0
        
        while(q!=[]):
            prev = None
            k = len(q)
            for _ in range(k):
                x = q.popleft(0)
                if (d%2==0 and x.val%2==0) or (d%2!=0 and x.val%2!=0):
                    return False

                if _==0:
                    prev = x.val
                else:
                    if d%2==0:
                        if x.val<=prev:
                            return False
                        else:
                            prev = x.val
                    else:
                        if x.val>=prev:
                            return False
                        else:
                            prev = x.val

                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)

            d+=1
        
        return True
