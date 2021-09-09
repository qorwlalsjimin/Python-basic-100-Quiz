n1, n2, n3 = map(int, input().split())
min = (n1 if(n1<n2) else n2) if((n1 if(n1<n2) else n2)<n3) else n3
print(min)