def combinatorics(n, k):
  result =[]
  def helper(start, curr): 
    if k == len(curr): 
      result.append(curr[:])
      return
    need = k - len(curr)
    for j in range(start, n-(need-1)+1):
      curr.append(j)
      helper(j+1, curr)
      curr.pop()
  helper(1, [])
  return result
print(combinatorics(4,2))