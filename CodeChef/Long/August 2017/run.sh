python testGenerator.py > test
python CHEFFA.py < test > 1.out
python CHEFFAbrute.py < test > 2.out
diff 1.out 2.out
