# matrix input
r = int(input("Enter rows: "))
c = int(input("Enter cols: "))

mat = []

print("Enter elements:")
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    mat.append(row)

# display
print("Matrix:")
for i in mat:
    print(i)

# sum of all elements
s = 0
for i in range(r):
    for j in range(c):
        s += mat[i][j]
print("Sum:", s)

# search element
x = int(input("Enter element to search: "))
found = False

for i in range(r):
    for j in range(c):
        if mat[i][j] == x:
            print("Found at:", i, j)
            found = True

if not found:
    print("Not found")