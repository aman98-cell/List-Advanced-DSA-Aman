"""Given an array arr[] of N integers, the task is to
find the maximum difference between any two elements of the array."""
# NAIVE Method
def maxdiff(arr,n):
    res = arr[1] - arr[0]
    for i in range(n-1):
        for j in range(i+1,n):
            res = max(res, arr[j] - arr[i])
    return res

arr = [2,3,10,6,4,8,1]
n = len(arr)
print(maxdiff(arr,n))
"""Time Complexity : O(n^2)
Auxiliary Space : O(1)"""

# Efficient Method

def effMaxxDiff(arr,n):
    res = arr[1] - arr[0]
    minval = arr[0]

    for j in range(1,n):
        res = max(res , arr[j] - minval)
        minval = min(minval,arr[j])
    return res

arr = [2, 1, 5, 3]
n = len(arr)
print(effMaxxDiff(arr,n))
"""Time Complexity : O(n)
Auxiliary Space : O(1)"""