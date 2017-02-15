from __future__ import absolute_import

import blosc

try:
    import cPickle as pkl
except ImportError:
    import pickle as pkl


def pickle(obj, filepath):
    """Pickle and compress."""
    arr = pkl.dumps(obj, -1)
    with open(filepath, 'wb') as f:
        s = 0
        while s < len(arr):
            e = min(s + blosc.MAX_BUFFERSIZE, len(arr))
            carr = blosc.compress(arr[s:e], typesize=8)
            f.write(carr)
            s = e


def unpickle(filepath):
    """Decompress and unpickle."""
    arr = []
    with open(filepath, 'rb') as f:
        carr = f.read(blosc.MAX_BUFFERSIZE)
        while len(carr) > 0:
            arr.append(blosc.decompress(carr))
            carr = f.read(blosc.MAX_BUFFERSIZE)
    return pkl.loads(b"".join(arr))
