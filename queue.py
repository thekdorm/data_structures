class Queue:

    def __init__(self):
        """Init method, just create an empty array
        """

        self.__items__ = []
    
    def enqueue(self, item):
        """Add item to end of array

        Args:
            item ([type]): Item to queue
        """

        self.__items__.append(item)
    
    def dequeue(self):
        """Remove and return first item

        Returns:
            [type]: Item removed from front of queue
        """

        item = self.__items__.pop(0)
        return item
    
    def read(self):
        """Read first item in queue

        Returns:
            [type]: First item in queue
        """

        return self.__items__[0]
    

if __name__ == '__main__':
    queue = Queue()

    queue.enqueue("apples")
    queue.enqueue("oranges")

    print(queue.dequeue())
    print(queue.__items__)
