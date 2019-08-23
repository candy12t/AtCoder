N = int(input())
aList = list(map(int, input().split()))

aList.sort(reverse=True)
Alice = sum(aList[::2])
Bob = sum(aList[1::2])
print(Alice - Bob)