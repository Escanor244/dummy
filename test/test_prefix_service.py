import unittest
from app.service import PrefixService

class TestPrefixService(unittest.TestCase):
    def setUp(self):
        self.prefix_service = PrefixService(["bonfire", "bonsai", "cardio", "case"])

    def test_unique_prefix(self):
        result = self.prefix_service.get_prefixes(["bonfire"])
        self.assertEqual(result["bonfire"], "bonf")

    def test_shared_prefix(self):
        result = self.prefix_service.get_prefixes(["bonsai", "bonfire"])
        self.assertEqual(result["bonsai"], "bons")
        self.assertEqual(result["bonfire"], "bonf")

    def test_non_existent(self):
        result = self.prefix_service.get_prefixes(["unknown"])
        self.assertEqual(result["unknown"], "not_applicable")

if __name__ == '__main__':
    unittest.main()
