python testGenerator.py > test
g++ CAVECOIN.cpp -std=c++14
time ./a.out < test > 1.out
