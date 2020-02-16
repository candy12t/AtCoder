n = int(input())
As = list(map(int, input().split()))
flag = True

for a in As:
    if a%2 == 0:
        if a%3 == 0 or a%5 == 0:
            pass
        else:
            flag = False
if flag:
    print('APPROVED')
else:
    print('DENIED')