class Solution(object):
    def twoSum(self, nums, target):
        num_index = [(i,num) for i,num in enumerate(nums)]
        num_index.sort(key=lambda x:x[1])
        left,right=0,len(nums)-1
        while left<right:
            s=num_index[left][1]+num_index[right][1]
            if s==target:
                return [num_index[left][0],num_index[right][0]]
            elif s<target:
                left += 1
            else:
                right -= 1
        return []
    # nums=list(map(int,input()))
    # target=int(input())
    # twoSum(nums,target)