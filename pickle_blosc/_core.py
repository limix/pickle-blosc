import pickle as pkl

import blosc


def pickle(obj, filepath):
    """
    Pickle, compress, and save it to a file.

    Parameters
    ----------
    obj : object
        Any python object to be pickled.
    filepath : str
        File path destination.
    """
    arr = pkl.dumps(obj, -1)
    with open(filepath, "wb") as f:
        s = 0
        while s < len(arr):
            e = min(s + blosc.MAX_BUFFERSIZE, len(arr))
            carr = blosc.compress(arr[s:e], typesize=8)
            f.write(carr)
            s = e


def unpickle(filepath):
    """
    Read, decompress, and unpickle a python object.

    Parameters
    ----------
    filepath : str
        File path to a pickled file.

    Returns
    -------
    obj : object
        Unpickled object.
    """
    arr = []
    buffsize = blosc.MAX_BUFFERSIZE
    with open(filepath, "rb") as f:
        while buffsize > 0:
            try:
                carr = f.read(buffsize)
            except (OverflowError, MemoryError):
                buffsize = buffsize // 2
                continue

            if len(carr) == 0:
                break
            arr.append(blosc.decompress(carr))

    if buffsize == 0:
        raise RuntimeError("Could not determine a buffer size.")

    return pkl.loads(b"".join(arr))
