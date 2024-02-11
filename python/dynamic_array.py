class DynamicArray:

    def __init__(self, capacity: int):
        self.array = None
        self.capacity = capacity

        if capacity > 0:
            self.array = [None for x in range(capacity)]

    def get(self, i: int) -> int:
        if (i < self.capacity):
            return self.array[i]

    def set(self, i: int, n: int) -> None:
        if i < self.capacity:
            self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.array[-1] is not None:
            self.resize()
        for i in range(self.capacity - 1, -1, -1):
            if self.getSize() == 0:
                self.set(0, n)
                break
            if self.array[i] is not None:
                self.set(i + 1, n)
                break

    def popback(self) -> int:
        for i in range(self.capacity - 1, -1, -1):
            if self.array[i] is not None:
                val = self.array[i]
                self.set(i, None)
                return val

    def resize(self) -> None:
        self.array.extend([None for x in range(self.capacity)])
        self.capacity *= 2

    def getSize(self) -> int:
        val = 0
        for i in range(self.capacity):
            if self.array[i] is not None:
                val += 1
        return val

    def getCapacity(self) -> int:
        return self.capacity


if __name__ == "__main__":
    # Test case 1
    da = DynamicArray(1)
    print(da.getSize())
    print(da.getCapacity())
    print(da.array)

    # Test case 2
    da = DynamicArray(5)
    print(da.getSize())
    print(da.getCapacity())
    print(da.array)

    # Test case 3
    da = DynamicArray(3)
    da.pushback(1)
    da.pushback(2)
    da.pushback(3)
    print(da.get(0))
    print(da.get(1))
    print(da.get(2))
    print(da.array)

    # Test case 4
    da = DynamicArray(4)
    da.pushback(1)
    da.set(0, 0)
    da.pushback(2)
    print(da.get(0))
    print(da.get(1))
    print(da.getCapacity())
    print(da.popback())
    print(da.array)

    # Test case 6
    # ["Array", 2, "pushback", 0, "pushback", 1, "pushback", 2, "getSize", "getCapacity"]
    da = DynamicArray(2)
    da.pushback(0)
    da.pushback(1)
    da.pushback(2)
    print(da.getSize())
    print(da.getCapacity())
    print(da.array)
