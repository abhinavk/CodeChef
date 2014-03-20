def maxDS(a):
if a%2 is 0:
return a
else:
return a-1
 
i = int(input())
if __name__ == '__main__':
for _ in range(i):
print(maxDS(int(input())))
