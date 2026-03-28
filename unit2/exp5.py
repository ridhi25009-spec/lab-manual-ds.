class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # enqueue (insert)
    def enqueue(self, val):
        new = Node(val)
        if self.rear is None:
            self.front = self.rear = new
        else:
            self.rear.next = new
            self.rear = new
        print("Inserted:", val)

    # dequeue (delete)
    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print("Removed:", self.front.data)
            self.front = self.front.next
            if self.front is None:
                self.rear = None

    # display
    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" <- ")
            temp = temp.next
        print("None")


# main
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

q.dequeue()

q.display()