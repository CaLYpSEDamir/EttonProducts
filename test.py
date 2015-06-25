# coding: utf-8

from products import ProductManager

p_m = ProductManager()
"""
    {
        'a': 150,
        'b': 200,
        'c': 100,
        'd': 100,
        'e': 250,
        'f': 100,
        'g': 150,
        'h': 125,
        'i': 50,
        'j': 150,
        'k': 100,
        'l': 75,
        'm': 500,
    }
"""
assert p_m.calculate(['a', 'a', 'a']) == 450  # 150*3

assert p_m.calculate(['a', 'a', 'b']) == 465  # (150+200)*0.9 + 150

assert p_m.calculate(['b', 'e', 'f', 'g']) == 675  # 200 + 0.95*(250+100+150)

assert p_m.calculate(['b', 'm', 'l', 'k']) == 787.5  # (200+500+75+100)*0.9
