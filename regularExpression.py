import re

express = "True" if re.fullmatch(r'[^a-z]', 'A') else "False"
print(express)


sym = "Yes" if re.fullmatch(r'[*]', '*') else "No"

print(sym)


