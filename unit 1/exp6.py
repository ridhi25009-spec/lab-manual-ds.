def binary(arr, low, high, key):
    if low > high:    # base case
        return -1
    
    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary(arr, low, mid-1, key)
    else:
        return binary(arr, mid+1, high, key)


# main
arr = [10, 20, 30, 40, 50, 60]
key = int(input("Enter element to search: "))

res = binary(arr, 0, len(arr)-1, key)

if res != -1:
    print("Element found at index:", res)
else:
    print("Not found")