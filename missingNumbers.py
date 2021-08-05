
def missingNumbers():
  x = int(input())
  n = 1
  ret = ""
  for i in range(x):
    y = int(input())
    while (n<y):
      print(n)
      ret += " " + str(n)
      n+=1
    n+=1
  if ret == "":
    print("good job")
missingNumbers()
