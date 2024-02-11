class List:
    def __init__(self, value, node=None):
        self.val = value
        self.next = node

class LinkedList:

    def __init__(self):
        self.head = List(0)
        self.tail = None

    def search(self, index: int) -> int:
        count = 0
        node = self.head.next

        while node and count < index:
            node = node.next
            count += 1

        return node

    def get(self, index: int) -> int:
        node = self.search(index)

        if node is None:
            return -1
        else:
            return node.val

    def insertHead(self, val: int) -> None:
        newnode = List(val)

        if self.head.next is None:
            self.head.next = newnode
            self.tail = newnode
        else:
            newnode.next = self.head.next
            self.head.next = newnode

    def insertTail(self, val: int) -> None:
        newnode = List(val)

        if self.head.next:
            self.tail.next = newnode
            self.tail = newnode
        else:
            self.head.next = newnode
            self.tail = newnode


    def remove(self, index: int) -> bool:
        count = 0
        node = self.head

        while node and count < index:
            node = node.next
            count += 1

        if node and node.next:
            if node.next == self.tail:
                self.tail = node
            node.next = node.next.next

            return True

        return False

    def getValues(self) -> [int]:
        # Return array of List values
        result = []
        node = self.head.next

        while node:
            result.append(node.val)
            node = node.next
        return result


L = LinkedList()

L.insertHead(3)
L.insertHead(2)
L.insertHead(4)
L.insertHead(5)
L.insertHead(1)
L.insertTail(6)

# 1 5 4 2 3 6
#print(L.get(2))
# Returns 6
print(L.getValues())

print(L.remove(0))
print("remove index 0")
# 1 5 2 3 6

#print(L.head.val)
#print(L.tail.val)
print(L.getValues())

print(L.remove(4))
# 1 5 2 3 6

print("remove index 4")
#print(L.head.val)
#print(L.tail.val)
print(L.getValues())

print('remove index 20')

print(L.remove(20))
