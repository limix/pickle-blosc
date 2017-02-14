#/bin/sh -f

wget https://github.com/Blosc/c-blosc/archive/v1.11.2.tar.gz
tar xzf v1.11.2.tar.gz

pushd c-blosc-1.11.2

mkdir build
cd build
cmake ..
cmake --build . --target install

popd
