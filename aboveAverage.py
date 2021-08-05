cases = int(input())

def calcsAvgScore(scores):
  totalScore = 0
  for score in scores:
    totalScore += int(score)
  return totalScore/len(scores)


for i in range(cases):
  case = input().split(" ")
  students = int(case[0])
  scores = case[1:]
  avgScore = calcsAvgScore(scores)
  betterThanAvg = 0
  for score in scores:
    if int(score) > avgScore:
      betterThanAvg += 1
  
  print('{:.3f}%'.format(round(betterThanAvg/len(scores)*100, 3)))