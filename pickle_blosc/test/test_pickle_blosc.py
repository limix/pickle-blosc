from os.path import join

from pickle_blosc import pickle, unpickle


class A(object):
    def __init__(self, value):
        self.value = value


def test_pickle_blosc():
    def _test_it(folder):
        fp = join(folder, "a.pkl")
        pickle(A(10), fp)
        a = unpickle(fp)
        assert a.value == 10

    try:
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as folder:
            _test_it(folder)

    except ImportError:
        import tempfile

        folder = tempfile.mkdtemp()
        _test_it(folder)
