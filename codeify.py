A = [4,0, -5, 1, 2, 3]
if sorted(A) [0] < 0:
    print(sorted(A)[-3])
else:
    print("Two")

""" nums = [4, -3,  -1, 2, 3, 5]
i = 1
nums.sort()
nums = [0] + nums
for i in range(len(nums)):
    while nums[i]>0 and nums[i]<len(nums) and nums[nums[i]]!=nums[i]:
        nums[nums[i]],nums[i] = nums[i],nums[nums[i]]
    num = 1
    for i in range(0,len(nums)):
        if num == nums[i]:
            num+=1
    #return(num)
print(num) """

nums = [5, 1, 0, -4, 2, 4, 3]
num = 1
nums.sort()

for i in range(len(nums)):
    if nums[i] >= 1:
        while num == nums[i]:
            num+=1
print(num)