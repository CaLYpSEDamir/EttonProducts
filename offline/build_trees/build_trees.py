# coding: utf-8

from copy import deepcopy
from operator import itemgetter

from avl_tree import AVLTree


ALL_XS = list()


# main_file = 'c://python27/tree/EttonProducts/offline/Files/merged'
# main_file = '/home/damir/Projects/EttonProducts/offline/Files/merged'
main_file = '/home/damir/Projects/EttonProducts/offline/Files/cut'


float_x1i, x1_preci, x1i, y1i, x2i, y2i, poli, ai, bi = range(9)


def get_dict(info):
    return {
        "x1": info[x1i],
        "y1": info[y1i],
        "x2": info[x2i],
        "y2": info[y2i],
        "pol_id": info[poli],
        "a": float(info[ai]),
        "b": float(info[bi]),
    }


def calc_Y(x, a, b):
    # x = float(x)
    # a = float(a)
    # b = float(b)
    return a*x+b


# списки на удаление, элемент состоит из val и y2
# будем группировать по y2
to_delete = []


def process_tree_nodes(nodes, x_middle, n_x):
    """
        Определяем val ноды, определяем ноды на удаление,
        сортируем по val
    """
    # обнуляем список на удаление
    global to_delete
    to_delete = []
    # если х2 совпадает с n_x, то на удаление
    for n in nodes:
        n['val'] = calc_Y(x_middle, n['a'], n['b'])

        if n['x2'] == n_x:
            # to_delete.append({
            #     'val': n['val'], 'y2': n['y2'], 'pol_id': n['pol_id'], })
            to_delete.append(n)

    return sorted(nodes, key=itemgetter('val'))


with open(main_file) as f:

    def process_tree(prev_info, build_first):

        for_tree_build = list()
        for_tree_build.append(get_dict(prev_info))

        prev_x1 = float(prev_info[x1i])
        ALL_XS.append([prev_x1, None])

        next_info = f.readline().split()

        if next_info:
            next_x1 = float(next_info[x1i])

            while prev_x1 == next_x1:
                for_tree_build.append(get_dict(next_info))

                next_info = f.readline().split()
                next_x1 = float(next_info[x1i])

            # середина между x(i) и x(i+1) для нахождений val-ов
            x_middle = (next_x1+prev_x1)/2

            prev_to_delete = to_delete

            # обрабатываем ноды будущего дерева
            to_add = process_tree_nodes(for_tree_build, x_middle, next_info[x1i])

            print '-'*80
            print to_add
            print prev_to_delete

            if build_first:
                tree = AVLTree()
                for n in to_add:
                    tree.add(tree.root, n['val'], n['a'], n['b'], n['pol_id'])
                tree.show()
                ref_to_tree = tree
            else:
                # если кривые координаты, идут вразброс с дырами,
                # то строим новое дерево
                #  __           __
                # /  \ пустота /  \
                # \__/         \__/

                if not prev_to_delete:
                    print 'Hole'
                    tree = AVLTree()
                    for n in to_add:
                        tree.add(tree.root, n['val'], n['a'], n['b'], n['pol_id'])

                    tree.show()
                    ref_to_tree = tree
                else:
                    prev_tree = ALL_XS[-2][1]
                    next_tree = deepcopy(prev_tree)

                    # пока грубое добавление/удаление
                    for n in to_add:
                        next_tree.add(next_tree.root, n['val'], n['a'], n['b'], n['pol_id'])
                    for n in prev_to_delete:
                        next_tree.delete(n['val'])

                    ref_to_tree = next_tree
                    next_tree.show()

            ALL_XS[-1][1] = ref_to_tree

            return next_info

        # TODO обработать последнюю строку(последний x),
        # TODO а то теряется последнее дерево

        return None


    prev_info = f.readline().split()
    next_info = process_tree(prev_info, True)

    while next_info:
        next_info = process_tree(next_info, False)


print ALL_XS
