def perm(array):
  n = len(array)
  result = []
  def helper(index): 
    if index == n - 1: 
      result.append(array[:])
      
    for j in range(index, n): 
      array[index], array[j] = array[j], array[index]
      helper(index + 1)
      array[index], array[j] = array[j], array[index]
  helper(0)
  return result

print(perm([1,4]))