import unittest
from gilded_rose import GildedRose, Item


class GildedRoseTest(unittest.TestCase):

    # Règle: un item normal perd 1 quality et 1 sell_in par jour
    def test_normal_item_decreases_quality_and_sell_in(self):
        items = [Item("Elixir of the Mongoose", 5, 7)]
        GildedRose(items).update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(6, items[0].quality)

    # Règle: le nom ne change jamais
    def test_item_name_does_not_change(self):
        items = [Item("Elixir of the Mongoose", 5, 7)]
        GildedRose(items).update_quality()
        self.assertEqual("Elixir of the Mongoose", items[0].name)


if __name__ == "__main__":
    unittest.main()