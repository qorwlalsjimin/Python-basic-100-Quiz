n1, n2 = map(int, input().split())
print(bool(n1) and bool(n2) or (not bool(n1)) and (not bool(n2)))
#print(bool(n1) == bool(n2))