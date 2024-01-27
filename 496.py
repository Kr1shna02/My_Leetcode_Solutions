class Solution(object):
    def check_next_greater(self,temp, subarray):
        for i in range(len(subarray)):
            if subarray[i]>temp:
                return subarray[i]
        return -1;

    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []

        for i in range(len(nums1)):
            temp = nums1[i]
            for j in range(len(nums2)):
                if j == len(nums2) - 1:
                    result.append(-1)
                    break
                else:
                    if temp == nums2[j]:
                        result.append(self.check_next_greater(temp, nums2[j + 1:]))
                        break
        return result
