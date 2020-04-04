import logging


class Stack(object):
    """
    A Stack implementation, with the following attributes
     - Array implementation
     - First in, last out
     - New elements added to end of list
     - Elements removed from end of list
    API roughly based on https://docs.oracle.com/javase/7/docs/api/java/util/Queue.html
    """

    def __init__(self, iterable_input=None):
        """
        Initialize and return an instance of the data structure.

        :param iterable_input: Add elements from iterable to the data structure. If iterable is ordered, elements will be in
        that order
        """
        self.array = list()

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
        return len(self.array)

    def add(self, element):
        """
        Add the specified element to the end of the data structure
        :param element:
        :type element: object
        :return: None
        :rtype: None
        """
        logging.info(f'Adding element: {element} to data structure, with array: {self.array}')
        self.array.append(element)
        logging.info(f'Added element: {element} to data structure, with array: {self.array}')
        return None

    def remove(self):
        """
        Remove the first element from the data structure, and return it. If the data structure is empty, then this will
        raise a ValueError.

        :raises: ValueError
        :return: The first object in the data structure, if there is one
        :rtype: object
        """
        # Return ValueError if no elements
        if len(self.array) <= 0:
            raise ValueError('No elements in data structure to remove')

        # Pull and last element in array
        element = self.array.pop()

        # Return pulled element
        return element

    def remove_element(self, element=None):
        """
        Remove the specified element from the data structure. If the specified element is not in the data structure
        (or the data structure is empty), then this will raise a ValueError.

        :param element: The element to be removed
        :type element: object
        :raises: ValueError
        :return: None
        :rtype: None
        """
        # Return ValueError if no elements
        if len(self.array) <= 0:
            raise ValueError('No elements in data structure to remove')

        # Reverse array, so that last added copy of element is removed
        self.array = list(reversed(self.array))
        # Find index of element, and re-phrase error if not found
        try:
            element_index = self.array.index(element)
        except ValueError:
            raise ValueError('Element not in data structure')
        # Pull and remove element at found index
        self.array.pop(element_index)

        # Reverse array again, to reset natural order
        self.array = list(reversed(self.array))

        # Return None
        return None

    def peak(self):
        """
        Return the first item in the data structure, without removing it
        :return: The first item in the data structure
        :rtype: object
        :raises: ValueError
        """
        # Return ValueError if no elements
        if len(self.array) <= 0:
            raise ValueError('No elements in data structure to remove')

        return self.array[-1]

    def contains(self, element):
        """
        Determine if the element is in the data structure.
        :return: Whether the element is in the data structure.
        :rtype: bool
        """
        return element in self.array
