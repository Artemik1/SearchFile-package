import unittest
from SearchFile import search


class MyTestCase(unittest.TestCase):

    def test_first_function_search(self):
        self.assertEqual(search("D:\\Anaconda\\bin"), ["libLIEF.dll"])

    def test_second_function_search(self):
        self.assertEqual(len(search("D:\\Anaconda\\condabin")), 7)

    def test_third_function_search(self):
        self.assertEqual(len(search("D:\\Anaconda\\bin")), 1)


if __name__ == '__main__':
    unittest.main()