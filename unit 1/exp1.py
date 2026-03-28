class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack += [element]

    def pop(self):
        if len(self.stack) == 0:
            print("Underflow!")
        else:
            print("Removed:", self.stack[-1])
            self.stack = self.stack[:-1]

    def peek(self):
        if len(self.stack) == 0:
            print("Stack empty!")
        else:
            print("Top element:", self.stack[-1])

    def display(self):
        print("Stack elements:", self.stack)

    def count(self):
        print("Total elements:", len(self.stack))


# driver code
obj = MyStack()

while True:
    print("\n--- Stack Menu ---")
    print("1.Push 2.Pop 3.Peek 4.Display 5.Count 6.Exit")

    choice = input("Choose: ")

    if choice == "1":
        x = input("Enter element: ")
        obj.push(x)

    elif choice == "2":
        obj.pop()

    elif choice == "3":
        obj.peek()

    elif choice == "4":
        obj.display()

    elif choice == "5":
        obj.count()

    elif choice == "6":
        print("Program Ended")
        break

    else:
        print("Invalid option")
