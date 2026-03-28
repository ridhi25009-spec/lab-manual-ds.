def sum_n(n):
    if n == 0:      # base case
        return 0
    else:
        return n + sum_n(n-1)   # recursive case


num = int(input("Enter number: "))
print("Sum is:", sum_n(num))