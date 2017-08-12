python testGenerator.py > test
g++ FLOWERPO.cpp -std=c++14
time ./a.out < test
time python FLOWERPO1.py < test
