def powerSet(array): 
  result = []
  def helper(array, i, subset):
    if i == len(array): 
      result.append(subset.copy())
      return
    helper(array, i+1, subset)
    subset.append(array[i])
    helper(array, i+1, subset)
    subset.pop()
  helper(array, 0, [])
  return result
  
print(powerSet([1,7,8]))