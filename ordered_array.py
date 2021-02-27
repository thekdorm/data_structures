class OrderedArray:
    
    def __init__(self, data: list=None):
        """Init method, take a list and automatically sort it with __sort

        Args:
            data (list): Array to sort
        """

        self.array = []  # type: list

        if data:
            self.__sort__(data)

    def binary_search(self, value: int, return_steps: bool=False) -> int:
        """Binary search implementation for OrderedArray class

        Args:
            value (int): The value to search for.
            return_steps (bool, optional): If True, return the number of steps. 

        Returns:
            int: If not found, -1. Otherwise, index of value or steps taken depending on return_steps.
        """

        upper_bound = len(self.array) - 1
        lower_bound = 0
        steps = 0
        
        while True:
            steps += 1
            
            """
            Need a special case here for when we run into the last 2 values to check
            Just check them both one at a time here
            """
            if upper_bound - lower_bound == 1:
                if self.array[lower_bound] == value:
                    steps += 1
                    found = lower_bound
                    break
                elif self.array[upper_bound] == value:
                    steps += 1
                    found = upper_bound
                    break
                else:  # if the value doesn't exist, return -1
                    return -1

            else:
                """
                Take a midpoint and compare it to the value we are looking for
                If the midpoint is higher than our value:
                    Define the new upper_bound as the midpoint and search again
                If the midpoint is lower than our value:
                    Define the new lower_bound as the midpoint and search again
                """
                midpoint = lower_bound + (upper_bound - lower_bound) // 2
                if self.array[midpoint] == value:
                    found = midpoint
                    break
                elif self.array[midpoint] > value:
                    upper_bound = midpoint
                elif self.array[midpoint] < value:
                    lower_bound = midpoint
            # print(f'Step {steps}: lower_bound={lower_bound}, upper_bound={upper_bound}')  # for debug

        if return_steps:
            return steps
        else:
            return found

    def __sort__(self, data: list):
        """Perform some sort magic to make it an ordered array

        Search through entire array to find the lowest number
        Once we go through entire array, store the lowest number in self.array
        Then delete number from this array, reset lowest, continue until array is empty

        Args:
            data (list): Array to sort
        """

        while len(data) > 0:
            lowest = data[0]  # initialize lowest to first element on each iteration
            for number in data:
                if number < lowest:  # if we found a lower number, that's the new lowest
                    lowest = number
            self.array.append(lowest)
            data.remove(lowest)

    def __bubble_sort__(self, data: list) -> None:
        """Bubble Sort implementation

        Pass through entire array, comparing each number to the number next to it
        If the current number is greater than the next number, switch them
        Continue until we have a pass through where we don't switch anything

        Args:
            data (list): Array to sort
        """
 
        unsorted_until = len(data) - 1
        finished = False

        while not finished:
            finished = True  # set to True here since we assume we're done until we make a switch
            for i in range(unsorted_until):
                if data[i] > data[i+1]:  # if we find two values out of order, switch them
                    data[i], data[i+1] = data[i+1], data[i]
                    finished = False
            unsorted_until -= 1  # each run will bubble the largest to the top so ignore that last index

        self.array = data
    
    def __selection_sort__(self, data: list) -> None:
        """Selection Sort implementation

        Pass through entire array to find lowest number on each pass
        Switch lowest number with the number at start_index at end of pass
        Increment start_index by 1 each time, end when start_index = len(data) - 1

        Args:
            data (list): [description]
        """

        start_index = 0

        while True:
            if start_index == len(data) - 1:
                break
            
            # Define lowest, lowest_index for tracking here
            lowest = data[start_index]
            lowest_index = start_index

            # Scan through remaining values in data starting from start_index
            for i in range(start_index, len(data)):
                if data[i] < lowest:  # if we find a lower value, update lowest, lowest_index
                    lowest = data[i]
                    lowest_index = i
            
            # Switch the found lowest value with the value at start_index, increment start_index
            data[start_index], data[lowest_index] = data[lowest_index], data[start_index]
            start_index += 1
        
        self.array = data


if __name__ == '__main__':
    array = [4, 6, 1, 4, 8, 88, 168, 3, 53, 10, 12, 78, 29, 30, 89, 100]
    ordered = OrderedArray(array)
    print(ordered.binary_search(168))
