# import pytest
#
# import unittest
#
# class smoke(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(2+2,4)
#
#     def test_sub(self):
#         self.assertEqual(4-2,2)

import unittest

import pytest

@pytest.mark.unittest
class Smoke(unittest.TestCase):

    def test_add(self):
        self.assertEqual(2 + 2, 4)

    def test_sub(self):
        self.assertEqual(4 - 2, 2)

if __name__ == "__main__":
    unittest.main()

