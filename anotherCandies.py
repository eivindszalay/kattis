nCases = int(input())

for i in range(nCases):
  input()
  nKids = int(input())
  nCandies = 0
  for i in range(nKids):
    nCandies += int(input())
  if nCandies % nKids == 0:
    print("YES")
  else:
    print("NO")