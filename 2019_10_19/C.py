import re
N = int(input())
S = input()

x = re.sub("(.)\\1{1,}", "-", S)
print(len(x))