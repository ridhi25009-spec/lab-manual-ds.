def fibonacci(n):
    if n <= 1:   # base case
        return n
    
    a = fibonacci(n-1)
    b = fibonacci(n-2)
    
    return a + b   # recursive case


n = int(input("Enter n: "))
ans = fibonacci(n)

print("Answer is:", ans)