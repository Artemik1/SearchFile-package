import unittest
from SearchFile import search


class MyTestCase(unittest.TestCase):

    def test_first_function_search(self):
        self.assertEqual(search("D:\\Anaconda\\bin"), ["libLIEF.dll"])

    def test_second_function_search(self):
        self.assertEqual(len(search("D:\\Скачанные файлы", "t", ".txt")), 3)

    def test_third_function_search(self):
        self.assertEqual(len(search("D:\\Скачанные файлы", extension_parameter=".md")), 10)

    def test_fourth_function_search(self):
        self.assertEqual(len(search("D:\\draw io\\draw.io", "draw")), 1)


if __name__ == '__main__':
    unittest.main()