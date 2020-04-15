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
        pass

    def size(self):
        """
        Returns the number of elements in the data structure
        :return: Number of elements in the data structure
        :rtype: int
        """
        pass

    def add(self, element):
        """
        Add the specified element to the end of the data structure
        :param element:
        :type element: object
        :return: None
        :rtype: None
        """
        return None

    def remove(self):
        """
        Remove the first element from the data structure, and return it. If the data structure is empty, then this will
        raise a ValueError.

        :raises: ValueError
        :return: The first object in the data structure, if there is one
        :rtype: object
        """
        pass

    def peak(self):
        """
        Return the first item in the data structure, without removing it
        :return: The first item in the data structure
        :rtype: object
        :raises: ValueError
        """
        pass

    def contains(self, element):
        """
        Determine if the element is in the data structure.
        :return: Whether the element is in the data structure.
        :rtype: bool
        """
        pass
