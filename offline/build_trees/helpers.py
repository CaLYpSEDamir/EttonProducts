# -*- coding: utf-8 -*-

from itertools import groupby, izip_longest
from operator import itemgetter
from collections import Counter

__author__ = 'damir'


def replace_node_val(next_tree, del_val, new_info):
    node = next_tree.get_node(next_tree.root, del_val)
    if not node.updated:
        node.a = new_info['a']
        node.b = new_info['b']
        node.pid1 = new_info['pol_id']
        node.updated = True
    else:
        node.pid2 = new_info['pol_id']


def process_add_del(to_del, to_add, next_tree, prev_tree):

    # del/add pairs
    pairs = []

    del_dict = {}
    add_dict = {}

    for k, gr in groupby(sorted(to_del, key=itemgetter('val')), lambda x: x['y2']):
        del_dict[k] = list(gr)

    for k, gr in groupby(sorted(to_add, key=itemgetter('val')), lambda x: x['y1']):
        add_dict[k] = list(gr)

    for k in del_dict:
        pairs.append((del_dict[k], add_dict.get(k, [])))

        add_dict.pop(k, None)

    # finals
    f_del = []
    f_add = []

    for pair in pairs:
        d, a = pair

        for pair in izip_longest(d, a):
            first, second = pair
            if first and second:
                replace_node_val(next_tree, first['val'], second)
            else:
                f_del.append(first) if first else f_add.append(second)

    print f_del, f_add

    # удаляем сразу по 2 значения
    for v, gr in groupby(f_del, lambda x: x['val']):
        # pol_ids = [g['pol_id'] for g in gr]
        next_tree.delete(v)


def find_polygon(root, came_x, came_y):
    less, more = None, None
    if root is None:
        print 'No {0} element in Tree'.format(came_y)
    elif root.val is None:
        print 'Tree is empty!'
    else:
        child = root
        while child:
            r_v = child.calc_new_val(came_x)
            if r_v == came_y:
                return child, child
            elif r_v < came_y:
                less = child
                child = child.right
            elif r_v > came_y:
                more = child
                child = child.left
    print less, more
    if not less and not more:
        pass
    elif less and more:
        # fixme достаю 2 одинаковых
        ids = [less.pid1, less.pid2, more.pid1, more.pid2]
        print ids
        return max(Counter(ids))
    else:
        print 'Out of territory'
        return None