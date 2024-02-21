class Solution:
    def largestPerimeter(self, arr: List[int]) -> int:
        arr.sort()
        arrsum = sum(arr)

        for i in range(len(arr)-1,1,-1):
            arrsum = arrsum-arr[i]
            if arrsum>arr[i]:
                return arrsum+arr[i]

        return -1