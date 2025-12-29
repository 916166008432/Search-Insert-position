def searchInsert(nums):
    n=len(nums)
    low,high=0,n-1
    idx=len(nums)
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>=target:
            idx=mid
            high=mid-1
        else:
            low=mid+1
    return idx
target=54
nums=list(map(int,input().split()))
print(searchInsert(nums))
        