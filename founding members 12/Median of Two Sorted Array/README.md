## Median of Two Sorted Arrays

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

### Example 1:
Input: `nums1 = [1,3], nums2 = [2]`
Output: `2.00000`
**Explanation:** merged array = [1,2,3] and median is 2.

### Example 2:
Input: `nums1 = [1,2], nums2 = [3,4]`
Output: `2.50000`
**Explanation:** merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

### Constraints:
- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`

## Instruction
The `solution.py` file in this directory contains a buggy solution to this problem. Your task is to find and fix the bug in the solution. Please do not rewrite the entire solution. Create a new file named `solution_fixed.py`, copy the existing code from `solution.py` into it, and then apply your fix there.