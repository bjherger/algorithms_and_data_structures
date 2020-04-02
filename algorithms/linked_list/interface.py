import logging


class LinkedList(object):
    """
    A linked list implementation, with the following attributes
     - Singly linked
     - First in, first out
     - New elements added to end of list
     - Elements removed from beginning of list
    API roughly based on https://docs.oracle.com/javase/7/docs/api/java/util/LinkedList.html
    """

    def __init__(self, iterable_input=None):
        """
        Initialize and return an instance of the data structure.

        :param iterable_input: Add elements from iterable to the data structure. If iterable is ordered, elements will be in
        that order
        """
        self.head = None
        self.tail = None
        self.size = 0

        if iterable_input is not None:
            logging.info(f'Creating data structure from iteratble: {iterable_input}')

            for element in iterable_input:
                logging.info(f'Adding element {element} to data structure')
                self.add(element)

    def add(self, element):
        """
        Add the specified element to the end of the data structure
        :param element:
        :type element: object
        :return: None
        :rtype: None
        """
        logging.info(
            f'Adding element: {element} to data structure with head: {self.head}, tail: {self.tail} and size: {self.size}')

        # Reference variables
        new_node = LinkedListNode(element)

        # If no elements in data structure, initialize head and tail
        if self.tail is None:
            logging.info('')
            self.head = new_node
            self.tail = new_node

        # Else, if elements in data structure already, add to old tail set new element as tail
        else:
            self.tail.next = new_node
            self.tail = new_node

        # Increment size
        self.size += 1

        logging.info(f'Added element: {element} to data structure with head: {self.head}, tail: {self.tail} '
                     f'and size: {self.size}')
        pass

    def remove(self):
        """
        Remove the first element from the data structure, and return it. If the data structure is empty, then this will
        raise a ValueError.

        :raises: ValueError
        :return: The first object in the data structure, if there is one
        :rtype: object
        """
        # Reference variables
        element = None

        # If no elements in data structure, raise ValueError
        if self.tail is None:
            raise ValueError('No elements in data structure to remove')

        # Else remove element and update points
        else:
            # If element is head and tail
            if self.size == 1:
                element = self.head.data
                self.head = None
                self.tail = None
            # If element is head, but not tail
            else:
                element = self.head.data
                self.head = self.head.next

        # Decrement size
        self.size -= 1
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

    def size(self):
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


class LinkedListNode():
    """
    Helper class, representing a node in the LinkedList
    """

    def __init__(self, data):
        self.data = data
        self.next = None
