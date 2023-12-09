def Binary_Search(arr,low,high,element):
    arr = sorted(arr)
    mid = low + (high - low)//2
    if element == arr[mid]:
        return mid
    elif element > arr[mid]:
        low = mid + 1
        return Binary_Search(arr,low,high,element)
    elif element < arr[mid]:
        high = mid - 1
        return Binary_Search(arr,low,high,element)

T = int(input())


while T>0:
    arr = list(map(int,input().split()))
    element = int(input())
    low  = 0
    high = len(arr) - 1
    ans = Binary_Search(arr,low,high,element)
    print(ans)
    T = T - 1




