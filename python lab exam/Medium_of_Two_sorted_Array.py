"""Medium of Two sorted Array
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
 
Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 
Constraints:
•	nums1.length == m
•	nums2.length == n
•	0 <= m <= 1000
•	0 <= n <= 1000
•	1 <= m + n <= 2000
•	-106 <= nums1[i], nums2[i] <= 106
"""
def findMedianSortedArrays(nums1, nums2):
        num3 = sorted(nums1 + nums2)
        x = len(num3)
        n = x // 2
        if x % 2 == 0:
            return (num3[n] + num3[n - 1]) / 2
        else:
            return num3[n]

nums1 = [1,3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))