time python testGenerator.py > test
g++ WEASELTX.cpp -std=c++14
time ./a.out < test > 1.out
