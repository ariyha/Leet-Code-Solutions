class Solution:
    def searchRange(self, arr: List[int], target: int) -> List[int]:
        if target not in arr:
            return [-1,-1]
        
        def binarysearch_left(arr, low, high):
            while low < high:
                mid = (low + high) // 2
                if arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid
            return low if arr[low] == target else -1

        def binarysearch_right(arr, low, high):
            while low < high:
                mid = ((low + high) // 2 )+ 1 
                if arr[mid] > target:
                    high = mid - 1
                else:
                    low = mid
            return high if arr[high] == target else -1

        left = binarysearch_left(arr, 0, len(arr) - 1)
        right = binarysearch_right(arr, 0, len(arr) - 1)
        return [left, right]
