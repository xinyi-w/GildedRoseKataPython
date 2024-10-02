# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)
    
    def test_vest_item_should_decrease_after_one_day(self):
        vest = "+5 Dexterity Vest"
        items = [Item(vest, 1, 2), Item(vest, 9, 19), Item(vest, 4, 6)]
        gr = GildedRose(items)

        gr.update_quality()

        self.assertEqual(gr.get_items_by_name(vest), [Item(vest, 0, 1), Item(vest, 8, 18), Item(vest, 3, 5)])

    def test_normal_item_quality_should_decrease(self):
        normal_item = "Normal Item"
        items = [Item(normal_item, 5, 10), Item(normal_item, 3, 7)]
        gr = GildedRose(items)

        gr.update_quality()

        self.assertEqual(gr.get_items_by_name(normal_item), [Item(normal_item, 4, 9), Item(normal_item, 2, 6)])

    def test_legendary_item_quality_should_never_decrease(self):
        legendary_item = "Sulfuras, Hand of Ragnaros"
        items = [Item(legendary_item, 0, 80)]
        gr = GildedRose(items)

        gr.update_quality()
        self.assertEqual(gr.get_items_by_name(legendary_item), [Item(legendary_item, 0, 80)])


if __name__ == '__main__':
    unittest.main()
