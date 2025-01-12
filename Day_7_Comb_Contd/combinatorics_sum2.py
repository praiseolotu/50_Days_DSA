def comb2(array, target): 
  array.sort()
  result = []
  n = len(array)
  def helper(start, curr, sum_curr):
    if sum_curr == target:
      result.append(curr[:])
      return
    if sum_curr > target: 
      return
    if start > n-1: 
      return
    hash = {}
    for i in range(start, n):
      if array[i] not in hash: 
        # append the value into hash
        hash[array[i]] = True
        curr.append(array[i])
        helper(i+1, curr, sum_curr+array[i])
        curr.pop()
  helper(0, [], 0)
  return result
    
print(comb2([3,5,2,1,3], 7))