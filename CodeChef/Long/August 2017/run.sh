python testGenerator.py > test
time python CHEFFA.py < test > 1.out
g++ CHEFFA.cpp
time ./a.out < test > 2.out
diff 1.out 2.out
