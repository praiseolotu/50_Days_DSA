def comb3(k, n): 
  '''
  k -> size of array (type : int)
  n -> targert (type: int)
  '''
  result = []
  def helper(start, curr, sumCur):
    if sumCur == n and len(curr) == k: 
      result.append(curr[:])
      return
    if sumCur > n or len(curr) == k:
      return
    for i in range(start, 10):
      curr.append(i)
      helper(i+1, curr, sumCur+i)
      curr.pop()
  helper(1, [], 0)
  return result
print(comb3(3,6))