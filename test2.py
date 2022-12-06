class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplet = []
        nums.sort()

        for i in range(len(nums) - 2):
            # skip throug duplicate numbers
            if i > 0 and nums[1] == nums[i -1]:
                continue
            # dont check overlapping values
            j = i + 1
            k = len(nums) - 1 
            # move k pointer lower when too high
            while j < k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                    # skip throug duplicate numbers
                    while nums[k] == nums[k + 1] and k > j:
                        k -= 1
                # move j pointer when to low
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                    # skip throug duplicate numbers
                    while nums[j] == nums[j - 1] and j < k:
                        j +=1
                else:
                    triplet.append([nums[i], nums[j], nums[k]])
                    # then increment
                    j += 1; k -= 1
                    # skip throug duplicate numbers
                    while nums[k] == nums[k + 1] and k > j:
                        k -= 1
                    # skip throug duplicate numbers
                    while nums[j] == nums[j - 1] and j < k:
                        j +=1
        return triplet    