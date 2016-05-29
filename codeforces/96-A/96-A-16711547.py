a = raw_input()
print ["NO", "YES"][any(x in a for x in ["0000000", "1111111"])]