import os

# import stat


def dir_inode():
    """docstring for test_th0"""
    for f in os.listdir('.'):
        inode = os.stat(f)
        print(f"{f} : {inode}")


def test_th0():
    # dir_inode()
    assert 0 == 0
