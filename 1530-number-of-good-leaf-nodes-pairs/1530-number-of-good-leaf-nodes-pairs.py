# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        tovisit = [[root,'']]
        nodes = []

        while(tovisit):
            x,route = tovisit.pop(0)

            if x.right==None and x.left==None:
                nodes.append([x.val,route])
                continue

            if x.right:
                tovisit.append([x.right,route+'R'])
            
            if x.left:
                tovisit.append([x.left,route+'L'])

        count = 0
        for k in range(len(nodes)):
            for j in range(k+1,len(nodes)):
                x1,r1 = nodes[k]
                x2,r2 = nodes[j]
                i=0

                while(i<min(len(r1),len(r2))):
                    if r1[i]!=r2[i]:
                        break
                    i=i+1
                
                x = len(r1[i:]+r2[i:])
                if x<=distance:
                    count+=1

        return count