from tempfile import TemporaryDirectory
from os.path import join
from pickle_blosc import pickle, unpickle


class A(object):
    def __init__(self, value):
        self.value = value


def test_pickle_blosc():
    with TemporaryDirectory() as folder:
        fp = join(folder, 'a.pkl')
        pickle(A(10), fp)
        a = unpickle(fp)
    assert a.value == 10
