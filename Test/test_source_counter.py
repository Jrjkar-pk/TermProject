import unittest

from score_counter import ScoreCounter

class MyTestCase(unittest.TestCase):

    def test_score_counter(self):
        self.assertEqual(ScoreCounter.increase_score(4))

    def test_draw(self):
        self.assertEqual(ScoreCounter.draw(2, 3))

    def test_get_circle(self):
        self.assertEqual(ScoreCounter.get_circles_eaten(3, 3))


if __name__ == '__main__':
    unittest.main()
