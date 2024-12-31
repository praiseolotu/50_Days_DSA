def kth_gram(n, k): 
  if n == 1: return 0
  length = 2**(n-1)
  mid_point = length//2
  if k <= mid_point:
    return kth_gram(n-1, k)
  else: 
    return int(not(kth_gram(n-1, k - mid_point)))

#print(kth_gram(2,2))
print(kth_gram(4,6))