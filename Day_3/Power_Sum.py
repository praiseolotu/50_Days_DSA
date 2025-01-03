def powerSum(arr, power = 1):
  sum = 0
  for each in arr: 
    if type(each) == list:
      sum += powerSum(each, power+1)
    else: 
      sum += each
  return sum**power 

print(powerSum([1,2,[3,4], [[2]]]))