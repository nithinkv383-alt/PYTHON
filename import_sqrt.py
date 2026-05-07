from math import sqrt

myList = []
tot = 0
n = int(input("Enter the number of items: "))
print("Enter", n, "the items:")

# First loop: Get inputs and calculate total sum
for i in range(n):
    item = int(input())
    myList.append(item)
    tot += item

# Calculate mean AFTER the first loop
mean = tot / n

# Reset tot to 0 to calculate variance
tot = 0
for item in myList:
    tot += (item - mean)**2

# Final calculations after all loops
var = tot / n
std = sqrt(var)

print("Mean:", mean)
print("Variance:", var)
print("Standard Deviation:", std)