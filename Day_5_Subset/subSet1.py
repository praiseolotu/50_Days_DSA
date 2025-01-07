def powerSetDup(array): 
  result = []
  array.sort()
  def helper(i, subset): 
    if i == len(array):
      result.append(subset[:])
      return
    subset.append(array[i])
    helper(i+1, subset)
    subset.pop()
    while i<len(array)-1 and array[i]==array[i+1]:
      i+=1
    helper(i+1, subset)
  helper(0,[])
  return result

print(powerSetDup([1,3,7]))