class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    # insert at end
    def insert(self, val):
        new = Node(val)
        if self.head is None:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new

    # delete value
    def delete(self, val):
        temp = self.head

        if temp and temp.data == val:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != val:
            prev = temp
            temp = temp.next

        if temp:
            prev.next = temp.next
        else:
            print("Not found")

    # display
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# main
l = SLL()

l.insert(10)
l.insert(20)
l.insert(30)

l.display()

l.delete(20)

l.display()