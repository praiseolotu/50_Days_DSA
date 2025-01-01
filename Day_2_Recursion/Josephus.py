def josephus(n, k):
  winner = 0
  for person in range(2, n+1):
    winner = (winner + k) % person
  
  return winner + 1
  
print(josephus(5,3))