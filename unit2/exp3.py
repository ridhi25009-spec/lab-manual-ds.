class DynamicArray:
    def __init__(self):
        self.arr = [0] * 2   # initial size
        self.n = 0           # number of elements
        self.cap = 2         # capacity

    def add(self, x):
        if self.n == self.cap:   # resize if full
            self.resize()
        self.arr[self.n] = x
        self.n += 1

    def resize(self):
        new = [0] * (2 * self.cap)
        for i in range(self.n):
            new[i] = self.arr[i]
        self.arr = new
        self.cap *= 2
        print("Resized to", self.cap)

    def pop(self):
        if self.n == 0:
            print("Empty")
        else:
            self.n -= 1
            print("Removed:", self.arr[self.n])

    def show(self):
        print("Array:", self.arr[:self.n])


# main
d = DynamicArray()

d.add(10)
d.add(20)
d.add(30)   # resize hoga yaha
d.show()

d.pop()
d.show()