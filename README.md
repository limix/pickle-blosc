# pickle-blosc

[![Travis](https://img.shields.io/travis/com/limix/pickle-blosc.svg?style=flat-square&label=linux%20%2F%20macos%20build)](https://travis-ci.com/limix/pickle-blosc) [![AppVeyor](https://img.shields.io/appveyor/ci/Horta/pickle-blosc.svg?style=flat-square&label=windows%20build)](https://ci.appveyor.com/project/Horta/pickle-blosc)

Read and write Pickle files using Blosc compression.

## Install

From terminal, enter

```
pip install pickle-blosc
```

## Usage

```python
>>> from pickle_blosc import pickle, unpickle
>>>
>>> class A(object):
>>>    def __init__(self, value):
>>>        self.value = value
>>>
>>> pickle(A(10), "filename.pkl")
>>> a = unpickle("filename.pkl")
>>> print(a.value)
10
```

## Running the tests

After installation, you can test it
```
python -c "import pickle_blosc; pickle_blosc.test()"
```
as long as you have [pytest](http://docs.pytest.org/en/latest/).

## Authors

* **Danilo Horta** - [https://github.com/Horta](https://github.com/Horta)

## License

This project is licensed under the MIT License - see the
[LICENSE](LICENSE) file for details
