python testGenerator.py > test
g++ PSHTTR.cpp -std=c++11
time ./a.out < test > 1.out
