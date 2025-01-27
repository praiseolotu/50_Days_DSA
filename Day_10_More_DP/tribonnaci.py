def trib(number):
  zero = 0; one = 1; two = 1
  if number<= 1: return number
  if number== 2: return two
  for i in range(3, number+1): 
    nextNum = zero + one + two
    zero = one; one = two; two = nextNum
  return nextNum