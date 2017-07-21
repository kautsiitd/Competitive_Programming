python testGenerator.py > test
python idealCode.py < test > 1.out
python SCHEDULE.py < test > 2.out
diff 1.out 2.out
