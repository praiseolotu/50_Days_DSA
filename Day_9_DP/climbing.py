def climbing(n):
  prev = 1
  curr = 1
  counter = 1
  while counter < n: 
    nextt = prev + curr
    prev = curr
    curr = nextt
    counter += 1
  return curr
print(climbing(3))