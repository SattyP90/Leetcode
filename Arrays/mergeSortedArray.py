class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        #2 pointer strategy as index position for each list
        p1 = m - 1
        p2 = n - 1
        #final position of the p in nums1 
        p = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]  #replace the currenct number in nums1 with numberi n nums 2
                p1 -= 1 #move left 1 on the list
            else:
                nums1[p] = nums2[p2]  
                p2 -= 1
            p -= 1


        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

        