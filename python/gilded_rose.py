# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        def clamp_quality(x):
            if x < 0:
                return 0
            elif x > 50:
                return 50
            else:
                return x

        for item in self.items:

            is_aged_brie = item.name == "Aged Brie"
            is_backstage = item.name == "Backstage passes to a TAFKAL80ETC concert"
            is_sulfuras = item.name == "Sulfuras, Hand of Ragnaros"

            is_conjured = item.name.startswith("Conjured")
            degrade = 2 if is_conjured else 1

            if not is_aged_brie and not is_backstage:
                item.quality = clamp_quality(item.quality - degrade)
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if is_backstage:
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if not is_sulfuras:
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if not is_aged_brie:
                    if not is_backstage:
                            item.quality = clamp_quality(item.quality - degrade)
                    else:
                        item.quality = 0
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
