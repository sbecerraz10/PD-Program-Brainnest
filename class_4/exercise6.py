def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True
res = [i for i in range(100) if is_prime(i)]
print(res)