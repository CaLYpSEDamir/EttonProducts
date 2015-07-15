# coding: utf-8

from collections import Counter


class Product(object):
    relations = {}
    price = 100

    @classmethod
    def get_price(cls):
        return cls.price

    @classmethod
    def get_relations(cls):
        return cls.relations

# наименование и цена продукта, если None, то цена приходит от родителя
main_list = {
    'a': 150, 'b': 200, 'c': None, 'd': None,
    'e': 250, 'f': None, 'g': 150, 'h': 125,
    'i': 50, 'j': 150, 'k': None, 'l': 75, 'm': 500,
}


# правила скидок, связи продуктов
rools = {
    'a': {'b': 10, 'k': 5, 'l': 5, 'm': 5},
    'd': {'e': 5},
    'e': {'many': {'list': ['f', 'g'], 'val': 5}},
}


# контейнер для классов продукции
products = {}


# создание классов продукций
for lett in main_list:
    if lett in rools:
        products[lett] = type(lett, (Product, ),
                              {'relations': rools[lett],
                               'price': main_list[lett] or Product.price})
    else:
        products[lett] = type(lett, (Product, ),
                              {'price': main_list[lett] or Product.price})


class ProductManager(object):

    def calculate(self, chosen):

        # для условий 5,6,7
        chosen_len = len(chosen)

        chosen.sort()

        # список результатов со скидками 1-4
        discount_1_4 = []

        # итоговая сумма
        total = 0

        # счетчик чего-сколько
        c = Counter(chosen)

        for key in sorted(c.keys()):

            relations = products[key].get_relations()

            for r_key in sorted(relations.keys()):

                if not r_key == 'many':
                    entry = min(c[key], c[r_key])
                    if entry:
                        discount_1_4.append([entry, relations[r_key], key, r_key])

                        # если 'a' несколько раз, то часть 'a' со скидкой, часть без
                        for k in [key, r_key]:
                            if c[k] > entry:
                                total += (c[k] - entry)*products[k].get_price()

                        try:
                            c.pop(key)
                            c.pop(r_key)
                        except IndexError:
                            break
                else:
                    many = relations['many']
                    entry = min(c[key], *[c[k] for k in many['list']])
                    if entry:
                        discount_1_4.append([entry, many['val'], key] + many['list'])

                        for k in [key, ] + many['list']:
                            if c[k] > entry:
                                total += (c[k] - entry)*products[k].get_price()

                        try:
                            for k in many['list']:
                                c.pop(k)
                            c.pop(key)
                        except IndexError:
                            break

        # сумма продуктов, не участвующих в скидках 1-4
        counter_total = sum([products[x].get_price()*y for (x, y) in c.items()])

        # если 1-4 скидки сработали, 5-7 скидки не действуют
        if discount_1_4:
            print 'Discounts 1-4 are applied'
            for res in discount_1_4:
                total += (
                    sum([products[x].get_price() for x in res[2:]]) *
                    (100-res[1]) / 100.0 * res[0]
                )
            total += counter_total
        # если 1-4 скидки не сработали и (а или с выбраны), то 5-7 скидки не действуют
        elif c.get('a') or c.get('c'):
            print 'No discounts are applied'
            total = counter_total
        # 5-7 скидки
        else:
            total = counter_total
            if chosen_len == 3:
                print 'Discounts 5 is applied'
                total *= 0.95
            elif chosen_len == 4:
                print 'Discounts 6 is applied'
                total *= 0.9
            elif chosen_len == 5:
                print 'Discounts 7 is applied'
                total *= 0.85

        return total


if __name__ == '__main__':

    input_ = input()
    input_ = input_.split(' ')

    p_m = ProductManager()
    total_sum = p_m.calculate(input_)

    print 'Total is: ', total_sum