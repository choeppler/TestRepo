import hello

import unittest

class TestHello(unittest.TestCase):

    def test_default(self):
        actual = hello.create_greeting()
        self.assertEqual(actual, 'Hello world!')

    def test_one_arg(self):
        actual = hello.create_greeting('YOU')
        self.assertEqual(actual, 'Hello YOU!')

    def test_two_args(self):
        actual = hello.create_greeting('you', 'guys')
        self.assertEqual(actual, 'Hello you guys!')

if __name__ == '__main__':
    unittest.main()
