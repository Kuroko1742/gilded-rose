import unittest

from gilded_rose import GildedRose, Item


class GildedRoseTest(unittest.TestCase):

    def test_normal_item_decreases_quality_and_sell_in(self):
        items = [Item("Elixir of the Mongoose", 5, 7)]
        app = GildedRose(items)

        app.update_quality()

        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(6, items[0].quality)


if __name__ == "__main__":
    unittest.main()
