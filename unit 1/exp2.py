# simple complexity demo

def single(n):
    c = 0
    for i in range(n):
        c += 1
    print("Single loop count:", c, "-> O(n)")


def nested(n):
    c = 0
    for i in range(n):
        for j in range(n):
            c += 1
    print("Nested loop count:", c, "-> O(n^2)")


def triangle(n):
    c = 0
    for i in range(n):
        for j in range(i):
            c += 1
    print("Triangular loop count:", c, "-> O(n^2)")


def half(n):
    c = 0
    while n > 0:
        n = n // 2
        c += 1
    print("Halving loop count:", c, "-> O(log n)")


# search cases (simple print)
def linear_search():
    print("\nLinear Search:")
    print("Best: O(1)")
    print("Worst: O(n)")


def binary_search():
    print("\nBinary Search:")
    print("Best: O(1)")
    print("Worst: O(log n)")


# main
n = int(input("Enter n: "))

single(n)
nested(n)
triangle(n)
half(n)

linear_search()
binary_search()