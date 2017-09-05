python testGenerator.py > test
g++ WEASELTX.cpp -std=c++14 -Wl,-stack_size,0x10000000,-stack_addr,0xc0000000
time ./a.out < test > 1.out
g++ WEASELTXOLD.cpp -std=c++14 -Wl,-stack_size,0x10000000,-stack_addr,0xc0000000
time ./a.out < test > 2.out
diff 1.out 2.out
