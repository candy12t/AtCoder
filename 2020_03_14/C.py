a, b, c = map(int, input().split())
print('Yes' if c-a-b > 0 and 4*a*b < (c-a-b) ** 2 else 'No' )

"""
√a+√b < √c
a+2√ab+b < c
2√ab < c-a-b
c-a-b > 0 Λ 4ab < (c-a-b)^2
"""