def winner(k, m, n):
  if k % (m+n) < m:
    print("Barb")
  else:
    print("Alex")

inp = input().split(" ")
winner(int(inp[0]),int(inp[1]),int(inp[2]))