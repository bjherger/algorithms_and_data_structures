class LinkedList(object):
    """
    A linked list implementation, with the following attributes
     - Singly linked
     - First in, first out
     - New elements added to end of list
     - Elements removed from beginning of list
    API roughly based on https://docs.oracle.com/javase/7/docs/api/java/util/LinkedList.html
    """

    def __init__(self, iterable=None):
        """
        Initialize and return an instance of the data structure.

        :param iterable: Add elements from iterable to the data structure. If iterable is ordered, elements will be in
        that order
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
        pass

    def remove(self):
        """
        Remove the first element from the data structure, and return it. If the data structure is empty, then this will
        raise a ValueError.

        :raises: ValueError
        :return: The first object in the data structure, if there is one
        :rtype: object
        """
        pass

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
        pass

    def get_size(self):
        """
        Return the number of elements currently in the data structure.
        :return: The number of elements currently in the data structure.
        :rtype: int
        """
        pass

    def peak(self):
        """
        Return the first item in the data structure, without removing it
        :return: The first item in the data structure
        :rtype: object
        """
        pass

    def find(self, element):
        """
        Find the element in the data structure, and return its index. If the element is not in the data structure,
        return None
        :param element: The element to search for
        :rtype: object
        :return: The index of the element, or None if it is not in the data structure
        :rtype: int
        """
        pass

    def contains(self, element):
        """
        Determine if the element is in the data structure.
        :return: Whether the element is in the data structure.
        :rtype: bool
        """
        pass
