# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @lru_cache
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        tovisit = [root]
        path = {root.val:''}

        while tovisit:
            x = tovisit.pop()
            if x.left:
                path[x.left.val] = path[x.val]+'L'
                tovisit.append(x.left)
            if x.right:
                path[x.right.val] = path[x.val] + 'R'
                tovisit.append(x.right)

            if x.val!=startValue and x.val!=destValue:
                del path[x.val]        
        
        a = path[startValue]
        b = path[destValue]
        i=0
        while(i<min(len(a),len(b))):
            if a[i]!=b[i]:
                break
            i=i+1

        a = a[i:]
        b = b[i:]
        a = a[::-1]
        s=''
        for i in a:
            s = s+'U'

        return s+b