import unittest
from solutions.medium.CompareVersionNumbers import CompareVersionNumbers

class TestCompareVersionNumbers(unittest.TestCase):

    def setUp(self):
        self.compareVersionNumbers = CompareVersionNumbers()

    def test_compareVersion_same_versions(self):
        version1 = "1.2"
        version2 = "1.2"
        expected_output = 0
        output = self.compareVersionNumbers.compareVersion(version1, version2)
        self.assertEqual(output, expected_output)

    def test_compareVersion_version1_greater(self):
        version1 = "1.2.1"
        version2 = "1.2"
        expected_output = 1
        output = self.compareVersionNumbers.compareVersion(version1, version2)
        self.assertEqual(output, expected_output)

    def test_compareVersion_version2_greater(self):
        version1 = "1.5"
        version2 = "1.7"
        expected_output = -1
        output = self.compareVersionNumbers.compareVersion(version1, version2)
        self.assertEqual(output, expected_output)

    def test_compareVersion_unfilled_zeros(self):
        version1 = "1.0"
        version2 = "1"
        expected_output = 0
        output = self.compareVersionNumbers.compareVersion(version1, version2)
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()