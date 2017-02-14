from __future__ import absolute_import

import blosc

try:
    import cPickle as pkl
except ImportError:
    import pickle as pkl


def pickle(obj, filepath):
    arr = pkl.dumps(obj, -1)
    with open(filepath, 'wb') as f:
        s = 0
        while s < len(arr):
            e = min(s + blosc.MAX_BUFFERSIZE, len(arr))
            carr = blosc.compress(arr[s:e], typesize=8)
            f.write(carr)
            s = e


def unpickle(filepath):
    arr = []
    with open(filepath, 'rb') as f:
        while True:
            carr = f.read(blosc.MAX_BUFFERSIZE)
            if len(carr) == 0:
                break
            arr.append(blosc.decompress(carr))
    return pkl.loads(b"".join(arr))
