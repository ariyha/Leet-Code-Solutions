class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(arr):
            if len(arr) <= 1:
                return arr

            n = len(arr) // 2

            a = arr[:n]
            b = arr[n:]

            a = mergesort(a)
            b = mergesort(b)

            return merge(a, b)

        def merge(a, b):
            m = len(a)
            n = len(b)
            out = []
            i, j = 0, 0

            while i < m and j < n:
                if a[i] <= b[j]:
                    out.append(a[i])
                    i += 1
                else:
                    out.append(b[j])
                    j += 1
            while i < m:
                out.append(a[i])
                i += 1 

            while j < n:
                out.append(b[j])
                j += 1 

            return out
        
        return mergesort(nums)
