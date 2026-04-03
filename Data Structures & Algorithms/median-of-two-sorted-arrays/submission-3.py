class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        A = nums1
        B = nums2
        total = m+n
        half = total//2


        if m > n:
            A,B = B,A
            m,n = n,m
        l = 0
        r = m-1
        
        while True:
            i = (l+r)//2
            j = half - i - 2

            Aleft = A[i] if i >=0 else float('-inf')
            Aright = A[i+1] if i+1 < m else float('inf')

            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j+1] if j+1 < n else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if total%2 == 0:
                    return ((max(Aleft,Bleft) + min(Aright,Bright))/2)
                else:
                    return min(Aright,Bright)
            elif Aleft > Bright:
                r = i-1
            else:
                l = i+1
        
                