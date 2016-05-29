import re
print "."+('.'.join(i for i in raw_input().lower().translate(None, "aeiouy")))