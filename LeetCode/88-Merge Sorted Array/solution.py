class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        length = m + n 
        ind = length - 1
        ind1 = m - 1 
        ind2 = n - 1
        while ind1 >= 0 and ind2 >= 0:
            if nums1[ind1] > nums2[ind2]:
                nums1[ind] = nums1[ind1]
                ind1 -= 1
            else:
                nums1[ind] = nums2[ind2]
                ind2 -= 1
            ind -= 1

        while ind2 >= 0:
            nums1[ind] = nums2[ind2]
            ind2 -= 1
            ind -= 1
            
