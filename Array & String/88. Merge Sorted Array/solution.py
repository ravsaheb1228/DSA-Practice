"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.

        """
        p1 = m-1;
        p2 = n-1;
        p3 = len(nums1) - 1;

        while p3 >= 0 :
            element1 = nums1[p1] if p1 >= 0 else -sys.maxsize - 1
            element2 = nums2[p2] if p2 >= 0 else -sys.maxsize - 1

            if(element1 > element2) :
                nums1[p3] = element1
                p3 -= 1
                p1 -= 1
            else:
                nums1[p3] = element2
                p3 -= 1
                p2 -= 1
            