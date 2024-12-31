def sorted_squared(array):
  new_array = [0] * len(array)
  i = 0
  j = len(array) - 1
  for k in reversed(range(len(array))):
    sqr_i = array[i] ** 2 
    sqr_j = array[j] ** 2
    if sqr_i > sqr_j: 
      new_array[k] = sqr_i
      i += 1
    else: 
      new_array[k] = sqr_j
      j -= 1
  return new_array
  
print(sorted_squared([-3,-2,-5]))