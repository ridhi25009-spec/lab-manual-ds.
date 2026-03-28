def hanoi(n, source, helper, dest):
    if n == 1:   # base case
        print("Move disk 1 from", source, "to", dest)
        return
    
    hanoi(n-1, source, dest, helper)   # step 1
    print("Move disk", n, "from", source, "to", dest)   # step 2
    hanoi(n-1, helper, source, dest)   # step 3


n = 3
hanoi(n, "A", "B", "C")