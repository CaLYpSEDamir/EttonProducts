# coding: utf-8

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
        "a": info[ai],
        "b": info[bi],
    }


LISTS = []

with open(main_file) as f:

    def process_tree(prev_info):

        for_tree = list()
        for_tree.append(get_dict(prev_info))

        prev_x1 = prev_info[0]
        ALL_XS.append([prev_x1, None])

        next_info = f.readline().split()

        # print next_info

        if next_info:
            next_x1 = next_info[0]

            while prev_x1 == next_x1:
                for_tree.append(get_dict(next_info))

                next_info = f.readline().split()
                next_x1 = next_info[0]

            LISTS.append(for_tree)

            return next_info

        # добавляем последнюю строку
        LISTS.append(for_tree)

        return None


    prev_info = f.readline().split()
    next_info = process_tree(prev_info)

    i = 0

    while next_info:
        # print next_info
        next_info = process_tree(next_info)

for l in LISTS:
    print l

    # if not ALL_XS:
    #     prev_tree = None
    # else:
    #     prev_tree = ALL_XS[-1][1]




    #
    # for line in f:
    #     i += 1
    #
    #
    #     print line
    #     break


