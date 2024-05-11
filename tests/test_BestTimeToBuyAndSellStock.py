import unittest
from solutions.easy.BestTimeToBuyAndSellStock import BestTimeToBuyAndSellStock

class TestBestTimeToBuyAndSellStock(unittest.TestCase):

    def setUp(self):
        self.solution = BestTimeToBuyAndSellStock()

    def test_maxProfit_no_profit(self):
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(self.solution.maxProfit(prices), 0)

    def test_maxProfit_max_profit(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(self.solution.maxProfit(prices), 5)

    def test_maxProfit_multiple_max_profits(self):
        prices = [2, 1, 2, 0, 1]
        self.assertEqual(self.solution.maxProfit(prices), 1)

    def test_maxProfit_empty_prices_list(self):
        prices = []
        self.assertEqual(self.solution.maxProfit(prices), 0)

    def test_maxProfit_single_price_in_list(self):
        prices = [2]
        self.assertEqual(self.solution.maxProfit(prices), 0)

    def test_case1(self):
        prices = [7,1,5,3,6,4]
        self.assertEqual(self.solution.maxProfit(prices), 5)



if __name__ == '__main__':
    unittest.main()