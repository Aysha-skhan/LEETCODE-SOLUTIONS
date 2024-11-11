#minimum-difference-between-largest-and-smallest-value-in-three-moves
def minDifference(nums):
    if len(nums)==3 or len(nums)==3:
        return 0
    M = max(nums)
    count_array = [0] * (M + 1)
    for num in nums:
        count_array[num] += 1
    for i in range(1, M + 1):
        count_array[i] += count_array[i - 1]
    output_array = [0] * len(nums)

    for i in range(len(nums) - 1, -1, -1):
        output_array[count_array[nums[i]] - 1] = nums[i]
        count_array[nums[i]] -= 1
    print(output_array)
    if output_array[0]<0:
        output_array.pop(0)
    else:
        output_array.pop()
    if output_array[0]<0:
        output_array.pop(0)
    else:
        output_array.pop()
    if output_array[0]<0:
        output_array.pop(0)
    else:
        output_array.pop()
    maxx=max(output_array)
    minn=min(output_array)
    # print(maxx,minn)
    return maxx-minn
print(minDifference([1,5,0,10,14]))
