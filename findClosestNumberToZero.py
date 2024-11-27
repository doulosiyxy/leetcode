nums = [-4,-2, 1,4,8]

#better answer, most efficient
closest = float('inf')
for num in nums:
    if abs(num) < abs(closest) or (abs(num) == abs(closest) and num > closest):
        closest = num
print(closest)

#long using for loops
distances = []
closestNums = []

for num in nums:
  distances.append(-num) if num < 0 else distances.append(num)

for i in range(len(distances)):
  if distances[i] == min(distances):
    closestNums.append(nums[i])

print(f"The closest number to zero is {max(closestNums)}.")

#short using list comprehension and ternary operator
distances = [-num if num < 0 else num for num in nums]
closestNums = [nums[i] for i in range(len(distances)) if distances[i] == min(distances)]
print(f"The closest number to zero is {max(closestNums)}.")
