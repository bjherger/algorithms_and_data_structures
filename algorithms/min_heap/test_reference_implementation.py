import logging
import unittest

from algorithms.min_heap import reference_implementation

logging.getLogger().setLevel(logging.DEBUG)


class TestMinHeap(unittest.TestCase):

    def test_api(self):
        data_structure = reference_implementation.MinHeap()
        required_methods = ['add', 'peak', 'contains', 'size']
        for required_method in required_methods:
            logging.info(f'Testing for required_method: {required_method}')
            self.assertTrue(hasattr(data_structure, required_method))

    def test0(self):
        data_structure = reference_implementation.MinHeap()
        data_structure.add(12)
        data_structure.add(6)
        data_structure.add(18)
        removed = data_structure.remove()

        self.assertEqual(6, removed)

    def test1(self):
        data_structure = reference_implementation.MinHeap()
        data_structure.add(12)
        data_structure.add(12)
        removed = data_structure.remove()

        self.assertEqual(12, removed)

    def test2(self):
        data_structure = reference_implementation.MinHeap()
        data_structure.add(17)
        removed = data_structure.remove()
        self.assertEqual(17, removed)

    def test3(self):
        data_structure = reference_implementation.MinHeap()
        self.assertRaises(ValueError, data_structure.remove)

        data_structure.add(17)

        data_structure.add(19)
        data_structure.add(23)

        removed = data_structure.remove()
        self.assertEqual(17, removed)

    def test4(self):
        data_structure = reference_implementation.MinHeap()

        sample_data = [124, 123, 451351, -234, 351235, 51235, 51325, 3523512351235, -213512351]
        sample_data_sorted = sorted(sample_data)
        for sample_element in sample_data:
            data_structure.add(sample_element)

        for sample_element in sample_data_sorted:
            peaked = data_structure.peak()
            self.assertEqual(sample_element, peaked)
            self.assertTrue(data_structure.contains(peaked))

            removed = data_structure.remove()
            self.assertFalse(data_structure.contains(removed))
            self.assertEqual(peaked, removed)
            self.assertEqual(sample_element, removed)
