# pickle-blosc

[![Travis](https://img.shields.io/travis/com/limix/pickle-blosc.svg?style=flat-square&label=linux%20%2F%20macos%20build)](https://travis-ci.com/limix/pickle-blosc) [![AppVeyor](https://img.shields.io/appveyor/ci/Horta/pickle-blosc.svg?style=flat-square&label=windows%20build)](https://ci.appveyor.com/project/Horta/pickle-blosc)

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
