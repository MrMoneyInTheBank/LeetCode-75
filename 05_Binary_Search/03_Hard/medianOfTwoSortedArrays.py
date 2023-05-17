"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

The overall run time complexity should be O(log(m+n)).
"""

def findMedianSortedArrays(nums1, nums2):
    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2

    if len(B) < len(A):
        A, B = B, A

    l, r = 0, len(A) - 1

    while True:
        pa = (l + r) // 2  # A
        pb = half - pa - 2  # B

        Aleft = A[pa] if pa >= 0 else float("-inf")
        Aright = A[pa + 1] if pa + 1 < len(A) else float("inf")
        Bleft = B[pb] if pb >= 0 else float("-inf")
        Bright = B[pb + 1] if pb + 1 < len(B) else float("inf")

        if Aleft <= Bright and Bleft <= Aright:
            if total % 2 == 1:
                return min(Aright, Bright)
            else:
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bright:
            r = pa - 1
        else:
            l = pa + 1
            
# T | S : O(log(m + n)) | O(1)