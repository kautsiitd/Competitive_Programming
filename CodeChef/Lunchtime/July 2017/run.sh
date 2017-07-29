python testGenerator.py > test
python 1.py < test > 1.out
g++ 1.cpp
./a.out < test > 2.out
diff 1.out 2.out
