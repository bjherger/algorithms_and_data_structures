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
        if self.size <= 0:
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
        return None

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
        # If no elements in data structure, raise ValueError
        if self.tail is None:
            raise ValueError('No elements in data structure to remove')

        # Else iterate through elements until we find the right one
        else:
            cursor = self.head
            cursor_next = self.head.next
            while cursor is not None:
                # Check cursor for element. Can only happen when cursor is head.
                if cursor.data == element:
                    # Remove the current head
                    self.head = cursor_next
                    self.size -= 1
                    return None
                # Check cursor_next for element
                if cursor_next is not None and cursor_next.data == element:
                    # Remove cursor_next
                    new_next = cursor_next.next
                    cursor.next = new_next
                    self.size -= 1
                    return None

                # If element not found, update cursor and cursor_next
                cursor = cursor_next
                cursor_next = cursor.next

        # If we reach the end without finding the element, it is not in the data structure. Return ValueError
        raise ValueError('Element not in data structure')

        return None

    def peak(self):
        """
        Return the first item in the data structure, without removing it
        :return: The first item in the data structure
        :rtype: object
        :raises: ValueError
        """
        # If no elements in data structure, return ValueError
        if self.size <= 0:
            raise ValueError('No elements in data structure to peak')

        # Else return the data from the first node
        else:
            return self.head.data

    def contains(self, element):
        """
        Determine if the element is in the data structure.
        :return: Whether the element is in the data structure.
        :rtype: bool
        """
        # If no elements in data structure, return False
        if self.size <= 0:
            return False
        # TODO Else check every element of the data structure sequentially, and return when we find a match
        print(self.head, type(self.head))
        cursor = self.head
        while cursor is not None:
            logging.info(f'Checking cursor: {cursor} for element: {element}')
            if cursor.data == element:
                return True
            cursor = cursor.next

        # TODO If we've gone through the whole data structure and not found a match, then item is not in data structure
        return False


class LinkedListNode():
    """
    Helper class, representing a node in the LinkedList
    """

    def __init__(self, data):
        self.data = data
        self.next = None
