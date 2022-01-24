a = int(input("type ur no."))
b = a//2
c = a%2
d = 0
if c != 0:
 for i in range(3,b,1):
  if a%i == 0:
    print(a,'is not a prime no.')
    break
 if a%i != 0:
   print(a,'is a prime no.')
else:
  print(a,'is not a prime no.')
  