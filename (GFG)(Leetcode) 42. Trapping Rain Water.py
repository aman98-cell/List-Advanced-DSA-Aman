"""42. Trapping Rain Water
Solved
Hard
Topics
Companies
Given n non-negative integers representing an
elevation map where the width of each bar is 1,
compute how much water it can trap after raining.


Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9


Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105"""


def trappingWater(arr):
    # Initialising leftmax and rightmax and length of
    # array
    n = len(arr)
    leftmax = [0] * n
    rightmax = [0] * n

    # Traversing for filling left max array
    leftmax[0] = arr[0]
    for i in range(1, n):
        leftmax[i] = max(arr[i], leftmax[i - 1])

    # Traversing for filling rightmax array
    rightmax[n - 1] = arr[n - 1]
    for j in range(n - 2, -1, -1):
        rightmax[j] = max(arr[j], rightmax[j + 1])

    res = 0
    for i in range(1, n - 1):
        res = res + (min(leftmax[i], rightmax[i]) - arr[i])

    return res
arr =  [3,0,0,2,0,4]
print(trappingWater(arr))
