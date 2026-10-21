import unittest
from validate_topology import validate

class TestTopology(unittest.TestCase):
    def test_expected(self):
        self.assertTrue(validate())
    def test_missing_link(self):
        self.assertFalse(validate(links=set()))

if __name__ == "__main__":
    unittest.main()
