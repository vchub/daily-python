import os
from os.path import getsize, join


def printTree():
    for root, dirs, files in os.walk('.'):
        fsize = sum([getsize(join(root, f)) for f in files])
        fnum = len(files)
        print(
            root,
            f'consumes {fsize} in bytes in {fnum} non-directory files',
            end='\n')

        # print(f' filese {files}', end='\n')

        def ok(d):
            return not (d.startswith('.') or d.startswith('_'))

        # dirs = list([d for d in dirs if ok(d)])
        for d in dirs:
            if d.startswith('.') or d.startswith('_'):
                dirs.remove(d)
        # print(dirs)


def test0():
    printTree()
    assert 2 == 2
