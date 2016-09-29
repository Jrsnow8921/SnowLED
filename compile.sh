#!/bin/bash

echo "Compiling snow.cpp into lib for python"

g++ -c -fPIC snow.cpp -o snow.o
g++ -shared -Wl,-soname,snowled.so -o snowled.so  snow.o
