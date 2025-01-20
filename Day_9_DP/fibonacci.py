def fib(n):
  prev = 0
  curr = 1
  counter = 1
  while counter < n: 
    nextt = prev + curr
    prev = curr
    curr = nextt
    counter += 1
  return curr
print(fib(4))
    
# 0 1 1 2 3 5 