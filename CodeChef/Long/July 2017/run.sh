python testGenerator.py > test
python APRPS.py < test > 1.out
python APRPS1.py < test > 2.out
diff 1.out 2.out
