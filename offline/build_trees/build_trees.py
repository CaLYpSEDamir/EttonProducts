# coding: utf-8

ALL_XS = list()

# main_file = 'c://python27/tree/EttonProducts/offline/Files/merged'
main_file = '/home/damir/Projects/EttonProducts/offline/Files/merged'

i = 1

with open(main_file) as f:

    l = f.readline()

    for line in f:
        i += 1


        print line
        break


