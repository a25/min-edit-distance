a='appropriate meaning'
b="approximate matching"
n=len(a)
m=len(b)
print(n,m)
T=[[0 for i in range(m)] for j in range(n)]


def edit(i,j):
  # print('g',i,j)
  if(T[i][j]):
    return T[i][j]
  if(i==0 and j==0):
    T[i][j]=0
    return 0
  if(i==0 or j==0):
    T[i][j]=1
    return T[i][j]
  diff=0 if a[i]==b[j] else 1
  T[i][j]=min(T[i][j-1]+1,T[i-1][j]+1,T[i-1][j-1]+diff)
  return T[i][j]
for i in range(n):
  for j in range(m):
    edit(i,j)
for row in range(n):
  print(T[row])

  
