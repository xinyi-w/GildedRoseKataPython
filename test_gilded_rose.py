# -*- coding: utf-8 -*-
import unittest

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    # Implement equality for Item objects to enable comparison in tests
    def __eq__(self, other):
        return self.name == other.name and self.sell_in == other.sell_in and self.quality == other.quality


class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Sulfuras, Hand of Ragnaros":
                if item.quality > 0:
                    item.quality -= 1

                item.sell_in -= 1

                if item.sell_in < 0 and item.quality > 0:
                    item.quality -= 1

    # Helper function to get items by name
    def get_items_by_name(self, name):
        return [item for item in self.items if item.name == name]


class GildedRoseTest(unittest.TestCase):

    # Test if the item name remains unchanged
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)  # Check if name remains the same

    # Test if vest item decreases in sell_in and quality after one day
    def test_vest_item_should_decrease_after_one_day(self):
        vest = "+5 Dexterity Vest"
        items = [Item(vest, 1, 2), Item(vest, 9, 19), Item(vest, 4, 6)]
        gr = GildedRose(items)

        gr.update_quality()

        # Expected values after one day of update
        expected_items = [Item(vest, 0, 1), Item(vest, 8, 18), Item(vest, 3, 5)]
        self.assertEqual(gr.get_items_by_name(vest), expected_items)

    # Test if normal item's quality decreases properly
    def test_normal_item_quality_should_decrease(self):
        normal_item = "Normal Item"
        items = [Item(normal_item, 5, 10), Item(normal_item, 3, 7)]
        gr = GildedRose(items)

        gr.update_quality()

        # Expected values after one day of update
        expected_items = [Item(normal_item, 4, 9), Item(normal_item, 2, 6)]
        self.assertEqual(gr.get_items_by_name(normal_item), expected_items)

    # Test if legendary item's quality never decreases
    def test_legendary_item_quality_should_never_decrease(self):
        legendary_item = "Sulfuras, Hand of Ragnaros"
        items = [Item(legendary_item, 0, 80)]
        gr = GildedRose(items)

        gr.update_quality()

        # Legendary item "Sulfuras" should retain its quality
        expected_items = [Item(legendary_item, 0, 80)]
        self.assertEqual(gr.get_items_by_name(legendary_item), expected_items)


if __name__ == '__main__':
    unittest.main()
