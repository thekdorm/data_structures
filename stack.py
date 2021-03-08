class Stack:

    def __init__(self):
        """Init method, just create an empty array
        """

        self.__items__ = []

    def push(self, item):
        """Push a new item on top of stack

        Args:
            item [type]: Item to push onto stack
        """

        self.__items__.append(item)

    def pop(self):
        """Remove and return item from top of stack

        Returns:
            [type]: Popped item
        """

        item = self.__items__.pop()
        return item

    def read(self):
        """Peek item on top of stack

        Returns:
            [type]: Peeked item
        """
        
        return self.__items__[-1]


if __name__ == '__main__':
    stack = Stack()
    
    stack.push("apples")
    stack.push("bananas")
    stack.push("watermelon")

    print(stack.read())
    print(stack.pop())

    print(stack.read())
