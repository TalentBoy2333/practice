'''
参考链接: https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-w-2/
'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)
        if l1 == 0 and l2 % 2 == 0:
            return (nums2[l2//2-1] + nums2[l2//2]) / 2
        elif l1 == 0 and l2 % 2 == 1:
            return nums2[l2//2]
        elif l1 % 2 == 0 and l2 == 0:
            return (nums1[l1//2-1] + nums1[l1//2]) / 2
        elif l1 % 2 == 1 and l2 == 0:
            return nums1[l1//2] 
        k = (l1 + l2) // 2
        ind1 = 0
        ind2 = 0
        while k > 1:
            # print('k:', k)
            if ind1 == l1:
                if (l1 + l2) % 2 == 0:
                    return (nums2[ind2+k-1] + nums2[ind2+k]) / 2
                else:
                    return nums2[ind2+k]
            if ind2 == l2:
                if (l1 + l2) % 2 == 0:
                    return (nums1[ind1+k-1] + nums1[ind1+k]) / 2
                else:
                    return nums1[ind1+k]

            k_d2 = k // 2
            end1 = ind1 + k_d2 - 1 if ind1 + k_d2 - 1 < l1 else l1 - 1
            end2 = ind2 + k_d2 - 1 if ind2 + k_d2 - 1 < l2 else l2 - 1
            if nums1[end1] < nums2[end2]:
                k -= (end1 - ind1 + 1)
                ind1 = end1 + 1
            else:
                k -= (end2 - ind2 + 1)
                ind2 = end2 + 1
            # print(ind1, ind2)

        if ind1 == l1:
            if (l1 + l2) % 2 == 0:
                return (nums2[ind2+k-1] + nums2[ind2+k]) / 2
            else:
                return nums2[ind2+k]
        if ind2 == l2:
            if (l1 + l2) % 2 == 0:
                return (nums1[ind1+k-1] + nums1[ind1+k]) / 2
            else:
                return nums1[ind1+k]

        if (l1 + l2) % 2 == 0:
            if ind1 + 1 == l1 and ind2 + 1 == l2:
                return (nums1[ind1] + nums2[ind2]) / 2
            elif ind1 + 1 == l1:
                return (min(nums1[ind1], nums2[ind2]) + \
                       min(max(nums1[ind1], nums2[ind2]), nums2[ind2+1])) / 2
            elif ind2 + 1 == l2:
                return (min(nums1[ind1], nums2[ind2]) + \
                       min(max(nums1[ind1], nums2[ind2]), nums1[ind1+1])) / 2
            else:
                return (min(nums1[ind1], nums2[ind2]) + \
                       min(max(nums1[ind1], nums2[ind2]), nums1[ind1+1], nums2[ind2+1])) / 2
        else:
            if ind1 + 1 == l1 and ind2 + 1 == l2:
                return max(nums1[ind1], nums2[ind2])
            elif ind1 + 1 == l1:
                return min(max(nums1[ind1], nums2[ind2]), nums2[ind2+1])
            elif ind2 + 1 == l2:
                return min(max(nums1[ind1], nums2[ind2]), nums1[ind1+1])
            else:
                return min(max(nums1[ind1], nums2[ind2]), nums1[ind1+1], nums2[ind2+1])


# if __name__ == '__main__':
#     so = Solution()
#     n1 = [1,2]
#     n2 = [3,4]
#     res = so.findMedianSortedArrays(n1, n2)
#     print(res)