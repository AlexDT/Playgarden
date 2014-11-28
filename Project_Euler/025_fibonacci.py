a = 0
b = 1
c = 0
for i in range(0, 1000000):
  c = a + b
  a = b
  b = c
  if len(str(c)) >= 1000:
    print c
    break