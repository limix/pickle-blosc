# pickle-blosc

[![PyPI-License](https://img.shields.io/pypi/l/pickle-blosc.svg?style=flat-square)](https://pypi.python.org/pypi/pickle-blosc/)
[![PyPI-Version](https://img.shields.io/pypi/v/pickle-blosc.svg?style=flat-square)](https://pypi.python.org/pypi/pickle-blosc/) [![Anaconda-Version](https://anaconda.org/conda-forge/pickle-blosc/badges/version.svg)](https://anaconda.org/conda-forge/pickle-blosc) [![Anaconda-Downloads](https://anaconda.org/conda-forge/pickle-blosc/badges/downloads.svg)](https://anaconda.org/conda-forge/pickle-blosc)

Read and write Pickle files using Blosc compression.

## Install

The recommended way of installing it is via
[conda](http://conda.pydata.org/docs/index.html)

```bash
conda install -c conda-forge pickle-blosc
```

An alternative way would be via pip

```
pip install pickle-blosc
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
