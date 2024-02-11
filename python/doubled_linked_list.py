class List:
    def __init__(self, value, next=None, prev=None):
        self.val = value
        self.next = next
        self.prev = prev

    def __getitem__(self, index):
        return self.val


class LinkedList:

    def __init__(self):
        self.root = None
        self.tail = None

    def search(self, index: int) -> int:
        count = 0
        node = self.root
        print(node, index)

        while True:
            if node is None:
                return None
            else:
                if count == index:
                    return node
            count += 1
            node = node.next

    def get(self, index: int) -> int:
        node = self.search(index)

        if node is None:
            return None
        else:
            return node.val

    def insertHead(self, val: int) -> None:
        newnode = List(val)

        if self.root is None:
            self.root = newnode
            self.tail = newnode
        else:
            newnode.next = self.root
            self.root.prev = newnode
            self.root = newnode

    def insertTail(self, val: int) -> None:
        newnode = List(val)

        # Empty list
        if self.tail is None:
            self.root = newnode
            self.tail = newnode
        else:
            newnode.prev = self.tail
            self.tail.next = newnode
            self.tail = newnode

    def remove(self, index: int) -> bool:
        node = self.search(index) #4

        if node is None:
            return False

        before = node.prev #3
        after = node.next #5

        if before is not None:
            before.next = after
        else:
            self.root = after
        if after is not None:
            after.prev = before
        else:
            self.tail = before

        return True

    def getValues(self) -> [int]:
        # Return array of List values
        result = []
        node = self.root

        while True:
            if node is None:
                return result
            else:
                result.append(node.val)
                node = node.next
        return result

    def getValuesI(self) -> [int]:
        # Return array of List values
        result = []
        node = self.tail

        while True:
            if node is None:
                return result
            else:
                result.append(node.val)
                node = node.prev
        return result



L = LinkedList()

L.insertHead(3)
L.insertHead(2)
L.insertHead(4)
L.insertHead(5)
L.insertHead(1)
L.insertTail(6)

# 1 5 4 2 3 6
print(L.get(2))
# Returns 6
print(L.getValues())
print(L.getValuesI())

L.remove(2)
# 1 5 2 3 6

print(L.root.val)
print(L.tail.val)
print(L.getValues())
print(L.getValuesI())
