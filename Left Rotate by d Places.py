def reverse(arr, beginning, end):
    while beginning < end:
        arr[beginning],arr[end] = arr[end],arr[beginning]
        beginning += 1
        end -= 1

    return arr

def leftRotate(arr,d):
    n=len(arr)
    reverse(arr,0,d-1)
    reverse(arr,d,n-1)
    reverse(arr,0,n-1)

arr=[10,20,30,40,50]
d=3
leftRotate(arr, d)
print(arr)
