import logging


class MinHeap(object):
    """
    A MinHeap implementation, with the following attributes
     - Complete tree
     - Root is minimum of all values
     - Parents are always less than or equal to children
    API roughly based on https://docs.oracle.com/javase/7/docs/api/java/util/PriorityQueue.html
    """

    def __init__(self, iterable_input=None):
        """
        Initialize and return an instance of the data structure.

        :param iterable_input: Add elements from iterable to the data structure. If iterable is ordered, elements will be in
        that order
        """
        self.array = list()

        self._size_ = 0

        if iterable_input is not None:
            logging.info(f'Creating data structure from iteratble: {iterable_input}')

            for element in iterable_input:
                logging.info(f'Adding element {element} to data structure')
                self.add(element)

    def size(self):
        """
        Returns the number of elements in the data structure
        :return: Number of elements in the data structure
        :rtype: int
        """
        return self._size_

    def add(self, element):
        """
        Add the specified element to the end of the data structure
        :param element: Element to be added
        :type element: object
        :return: None
        :rtype: None
        """

        # Add new element to last leaf in array
        self.array.append(element)
        pointer_index = len(self.array) - 1
        parent_index = pointer_index // 2
        # TODO Sieve up until min heap quality satisfied
        while (parent_index >= 0) and (self.array[pointer_index] < self.array[parent_index]):
            tmp = self.array[parent_index]
            self.array[parent_index] = self.array[pointer_index]
            self.array[pointer_index] = tmp
            pointer_index = parent_index
            parent_index = pointer_index // 2

        # Increment size
        self._size_ += 1

    def remove(self):
        """
        Remove the first element from the data structure, and return it. If the data structure is empty, then this will
        raise a ValueError.

        :raises: ValueError
        :return: The first object in the data structure, if there is one
        :rtype: object
        """
        # If no elements in data structure, raise ValueError
        if self._size_ <= 0:
            raise ValueError('No elements in data structure to remove')

        elif self._size_ == 1:
            # Remove current 0th item
            return_value = self.array[0]

            # Reset to empty array
            self.array = list()
        else:
            # Remove current 0th item
            return_value = self.array[0]

            # Replace 0th item with replacement value (last value)
            self.array[0] = self.array.pop()

            # Sieve new 0th item until min heap quality satisfied
            pointer_index = 0
            pointer_child_left_index = pointer_index * 2
            pointer_child_right_index = pointer_index * 2 + 1
            while pointer_child_left_index <= len(self.array) - 1:

                # Determine smallest child
                if pointer_child_right_index <= len(self.array) - 1:
                    min_child_index = pointer_child_left_index if self.array[pointer_child_left_index] < self.array[
                        pointer_child_right_index] else pointer_child_right_index
                else:
                    min_child_index = pointer_child_left_index
                # If smallest child is smaller than pointer, switch pointer with smallest child
                if self.array[min_child_index] < self.array[pointer_index]:
                    tmp = self.array[min_child_index]
                    self.array[min_child_index] = self.array[pointer_index]
                    self.array[pointer_index] = tmp

                    # Update pointer and children
                    pointer_index = min_child_index
                    pointer_child_left_index = pointer_index * 2
                    pointer_child_right_index = pointer_index * 2 + 1

                else:
                    break

        # Decrement size
        self._size_ -= 1
        # Return old 0th item
        return return_value

    def peak(self):
        """
        Return the first item in the data structure, without removing it
        :return: The first item in the data structure
        :rtype: object
        :raises: ValueError
        """
        # If no elements in data structure, return ValueError
        if self._size_ <= 0:
            raise ValueError('No elements in data structure to peak')

        # Else return the data from the first node
        else:
            return self.array[0]

    def contains(self, element):
        """
        Determine if the element is in the data structure.
        :return: Whether the element is in the data structure.
        :rtype: bool
        """
        return element in self.array
