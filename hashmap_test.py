import unittest
from hashmap import HashMap

class TestHashmap(unittest.TestCase):

    def test_assign(self):
        hash_map = HashMap(20)
        hash_map.assign('Anne', 53)
        hash_map.assign('Bob', 50)
        hash_map.assign('Colin', 17)
        self.assertEqual(hash_map.retrieve('Bob'), 50)
        self.assertIsNone(hash_map.retrieve('Dave'))

    def test_retrieve(self):
        hash_map = HashMap(20)
        self.assertIsNone(hash_map.retrieve('Anne'))       
