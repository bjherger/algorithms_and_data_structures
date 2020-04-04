import logging
import unittest

from algorithms.stack import reference_implementation

logging.getLogger().setLevel(logging.INFO)


class StackTest(unittest.TestCase):

    def test_api(self):
        data_structure = reference_implementation.Stack()
        required_methods = ['add', 'remove', 'remove_element', 'peak', 'contains', 'size']
        for required_method in required_methods:
            logging.info(f'Testing for required_method: {required_method}')
            self.assertTrue(hasattr(data_structure, required_method))

    def test0(self):
        data_structure = reference_implementation.Stack()
        data_structure.add(12)
        data_structure.add(6)
        data_structure.add(18)

        peaked = data_structure.peak()
        removed = data_structure.remove()

        self.assertTrue(data_structure.contains(6))
        self.assertTrue(data_structure.contains(12))
        self.assertFalse(data_structure.contains(18))
        self.assertEqual(18, peaked)
        self.assertEqual(18, removed)

    def test1(self):
        data_structure = reference_implementation.Stack()
        data_structure.add(12)
        data_structure.add(12)
        removed = data_structure.remove()

        self.assertTrue(data_structure.contains(12))
        self.assertEqual(12, removed)

    def test2(self):
        data_structure = reference_implementation.Stack()
        data_structure.add(17)
        self.assertTrue(data_structure.contains(17))

    def test3(self):
        data_structure = reference_implementation.Stack()
        self.assertFalse(data_structure.contains(17))
        data_structure.add(17)
        self.assertTrue(data_structure.contains(17))

        data_structure.add(19)
        data_structure.add(23)
        self.assertTrue(data_structure.contains(17))
        self.assertTrue(data_structure.contains(19))
        self.assertTrue(data_structure.contains(23))

        removed = data_structure.remove()
        self.assertEqual(23, removed)
        self.assertTrue(data_structure.contains(19))
        self.assertTrue(data_structure.contains(17))
        self.assertFalse(data_structure.contains(23))

    def test4(self):
        data_structure = reference_implementation.Stack()

        sample_data = [124, 123, 451351, -234, 124, 351235, 51235, 51325, 3523512351235, -213512351]
        sample_data_sorted = sorted(sample_data)
        for sample_element in sample_data:
            data_structure.add(sample_element)

        self.assertEqual(len(sample_data), data_structure.size())

        for sample_element in sample_data_sorted:
            self.assertTrue(data_structure.contains(sample_element))

        for sample_element in reversed(sample_data):
            self.assertTrue(data_structure.contains(sample_element))

            removed = data_structure.remove()
            self.assertEqual(sample_element, removed)

    def test5(self):

        sample_data = [124, 123, 451351, -234, 124, 351235, 51235, 51325, 3523512351235, -213512351]

        data_structure = reference_implementation.Stack(sample_data)
        data_structure.remove_element(451351)

        self.assertEqual(len(sample_data) - 1, data_structure.size())
        self.assertFalse(data_structure.contains(451351))
        pass

    def test6(self):
        data_structure = reference_implementation.Stack()
        data_structure.add(12)
        data_structure.add(6)
        data_structure.add(18)

        peaked = data_structure.peak()
        data_structure.remove_element(6)

        self.assertFalse(data_structure.contains(6))
        self.assertTrue(data_structure.contains(18))
        self.assertTrue(data_structure.contains(12))
        self.assertEqual(18, peaked)
