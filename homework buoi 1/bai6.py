from math import sqrt
a, b, c = map(float, input().split())
if (a+b > c) and (b+c > a) and (a+c > b):
    p = (a+b+c)/2
    area = sqrt(p*(p-a)*(p-b)*(p-c))
    print(f"{area:.1f}")
else:
    print("Ko phải 3 cạnh của tam giác")