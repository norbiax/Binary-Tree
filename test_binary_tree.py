import unittest
from newNode_binary_tree import NewNode
import calc_binary_tree


class TestNewNode(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.root = NewNode(5)
        self.root.right = NewNode(7)
        self.root.right.right = NewNode(0)
        self.root.right.right.right = NewNode(8)
        self.root.right.right.right.right = NewNode(5)

    def tearDown(self):
        print('tearDown\n')

    def test_node_property(self):
        print('test_node_property')
        self.assertEqual(self.root.node_property, '5')
        self.assertEqual(self.root.right.node_property, '7')
        self.assertEqual(self.root.right.right.node_property, '0')
        self.assertEqual(self.root.right.right.right.node_property, '8')
        self.assertEqual(self.root.right.right.right.right.node_property, '5')


class TestCalc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.root = NewNode(5)
        self.root.right = NewNode(7)
        self.root.right.right = NewNode(0)
        self.root.right.right.right = NewNode(8)
        self.root.right.right.right.right = NewNode(5)

    def tearDown(self):
        print('tearDown\n')

    def test_sum_in_node(self):
        print('test_sum_in_node')
        result = calc_binary_tree.sum_in_node(self.root.right)
        self.assertEqual(result, 20)

    def test_avg(self):
        print('test_avg')
        result = calc_binary_tree.avg(self.root.right)
        self.assertEqual(result, 5)

    def test_med(self):
        print('test_med')
        result = calc_binary_tree.med(self.root.right)
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
