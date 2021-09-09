n1, n2, n3 = map(int, input().split())
min = n1 if(n1<n2) else n2
min = n3 if(n3<min) else min
print(min)