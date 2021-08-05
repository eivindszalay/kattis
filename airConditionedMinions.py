nMinions = int(input())
minions = []

size = lambda interval : interval[1]
for i in range(nMinions):
  x = lambda a : (int(a.split(" ")[0]), int(a.split(" ")[1]))
  minions.append(x(input()))
  

minions.sort(key=size)


rooms = []
rooms.append(minions[0][1])


for minion in minions:
  if minion[0] > rooms[-1]:
    rooms.append(minion[1])

print(len(rooms))