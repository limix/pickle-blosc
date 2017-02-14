#/bin/sh -f

https://github.com/Blosc/python-blosc/archive/v1.5.0.tar.gz
tar xzf v1.5.0.tar.gz

pushd python-blosc-1.5.0

python setup.py build_ext --inplace --blosc=/usr/local

popd
