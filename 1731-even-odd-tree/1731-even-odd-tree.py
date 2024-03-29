# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = deque([root])
        d=0
        while(q):
            for _ in range(len(q)):
                x = q.popleft()
                if (d%2==0 and x.val%2==0) or (d%2!=0 and x.val%2!=0):
                    return False

                if _==0:
                    prev = x.val
                else:
                    if(d%2==0 and x.val<=prev) or (d%2!=0 and x.val>=prev):
                        return False
                    prev = x.val

                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)

            d=d+1
        
        return True
