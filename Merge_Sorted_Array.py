class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        final_length = m + n - 1

        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[final_length] = nums1[m-1]
                m -= 1
                final_length -= 1
            else:
                nums1[final_length] = nums2[n-1]
                n -= 1
                final_length -= 1

        while n > 0:
            nums1[final_length] = nums2[n-1]
            n -= 1
            final_length -= 1
