# Write a for loop to add up all numbers between 0 and 100
s=0
for i in range(101):
  s+=i
print(s)




# ----------------------------- or
print(sum([i for i in range(101)]))