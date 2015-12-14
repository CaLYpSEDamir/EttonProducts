# coding: utf-8

ALL_XS = list()

main_file = 'c://python27/tree/EttonProducts/offline/' \
            'Files/file0file1file2file3file4file5file6file7'

with open(main_file) as f:
    l = f.readline()

    for line in f:
        print line
        break


