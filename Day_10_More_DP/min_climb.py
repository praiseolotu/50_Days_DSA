def min_climb(array): 
  n = len(array)
  mincost = [0]*(n+1)
  mincost[0] = 0
  mincost[1] = 0
  for i in range(2, n+1): 
    oneStep= array[i-1] + mincost[i-1]
    twoStep= array[i-2] + mincost[i-2]
    mincost[i] = min(oneStep, twoStep)
  return mincost[n]
  