# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        h=[]
        def search(node,x,y,heap):
            heapq.heappush(heap,(x,y,node.val))
            if node.left:
                search(node.left,x-1,y+1,heap)
            if node.right:
                search(node.right,x+1,y+1,heap)
        if root:
            search(root,0,0,h)
        ans=[]
        x,y=float('-inf'),float('-inf')
        while h:
            cur=heapq.heappop(h)
            if cur[0]==x:
                ans[-1].append(cur[2])
            else:
                ans.append([cur[2]])
                x=cur[0]
        return ans