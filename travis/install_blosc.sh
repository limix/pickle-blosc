#/bin/sh -f

if ( test "`uname -s`" = "Darwin" )
then
  echo
else
  sudo add-apt-repository --yes ppa:kalakris/cmake
  sudo apt-get update -qq
  sudo apt-get install cmake
fi

wget https://github.com/Blosc/c-blosc/archive/v1.11.2.tar.gz
tar xzf v1.11.2.tar.gz

pushd c-blosc-1.11.2

mkdir build
cd build
cmake ..
cmake --build . --config Release
ctest

popd
