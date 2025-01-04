'''
Time Complexity: O(n*n!)
Space Complexity: O(n)
where n is the recursive depth
'''

def perm_dupli(array):
  result = []
  n = len(array)
  def helper(index):
    if index == n - 1: 
      result.append(array[:])
      return
    hashmap ={}
    for j in range(index, n):
      if array[j] not in hashmap:
        hashmap[array[j]] = True
        array[index], array[j] = array[j], array[index]
        helper(index + 1)
        array[index], array[j] = array[j], array[index]
        
  helper(0)
  return result
print(perm_dupli([3,3,2]))