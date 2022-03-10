nums = [-2,1,-3,4,-1,2,1,-5,4]
dp = []
dp.append(nums[0])
for i in range(1,len(nums)):
    if dp[i-1] < 0:
        dp.append(nums[i])
    else:
        dp.append(nums[i]+dp[i-1])
print(max(dp))