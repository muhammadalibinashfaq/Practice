nums = []

for i in range(5):
    nums.append(int(input("Add number 5 times: ")))

print(nums)

highest = 0
sec_highest = 0

for i in nums:
    if i > highest:
        sec_highest = highest
        highest = i
    elif i > sec_highest:
        sec_highest = i

print(sec_highest)