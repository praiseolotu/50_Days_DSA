def combinatorics_sum(array, target): 
  result =[]
  def helper(start, curr, summ): 
    if summ > target:
      return
    if summ == target:
      result.append(curr[:])
      return
    for j in range(start, len(array)): 
      curr.append(array[j])
      helper(j, curr, summ+array[j])
      curr.pop()
  helper(0, [], 0)
  return result
print(combinatorics_sum([2,3,4,7], 7))