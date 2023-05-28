def max_product(a):
  h1 = max(a)
  a.remove(h1)
  h2 = max(a)
  return h1* h2