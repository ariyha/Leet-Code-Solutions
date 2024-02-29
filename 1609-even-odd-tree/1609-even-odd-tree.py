# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = [root]
        d=0
        
        while(q!=[]):
            prev = None
            k = len(q)
            for _ in range(k):
                x = q.pop(0)
                if d%2==0 and x.val%2==0:
                    return False
                if d%2!=0 and x.val%2!=0:
                    return False

                if prev ==None:
                    prev = x.val
                    if x.left!=None:
                        q.append(x.left)
                    if x.right!=None:
                        q.append(x.right)
                    continue
                
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

                if x.left!=None:
                    q.append(x.left)
                if x.right!=None:
                    q.append(x.right)

            d+=1
        
        return True
