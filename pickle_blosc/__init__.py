"""
Library for reading and writting Pickle files using Blosc compression.
"""

from ._core import pickle, unpickle
from ._testit import test

__version__ = "0.1.0"


__all__ = ["__version__", "test", "pickle", "unpickle"]
