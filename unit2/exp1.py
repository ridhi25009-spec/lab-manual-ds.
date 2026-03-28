arr = [10, 20, 30]

# INSERT (with shifting)
pos = 1
val = 15

arr.append(0)   # space banayi
for i in range(len(arr)-1, pos, -1):
    arr[i] = arr[i-1]

arr[pos] = val
print("After insert:", arr)


# DELETE (with shifting)
pos = 2

for i in range(pos, len(arr)-1):
    arr[i] = arr[i+1]

arr.pop()
print("After delete:", arr)
