class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        tovisit = [root]
        val=0
        path = {root.val:''}

        while tovisit:
            x = tovisit.pop(0)
            if x.left:
                path[x.left.val] = path[x.val]+'L'
                tovisit.append(x.left)
            if x.right:
                path[x.right.val] = path[x.val] + 'R'
                tovisit.append(x.right)

            if x.val!=startValue and x.val!=destValue:
                del path[x.val]
            else:
                if startValue in path and destValue in path:
                    break 
        
        a = path[startValue]
        b = path[destValue]
        i=0
        while(i<min(len(a),len(b))):
            if a[i]!=b[i]:
                break
            i=i+1

        a = a[i:]
        b = b[i:]
        s = 'U'*len(a)

        return s+b