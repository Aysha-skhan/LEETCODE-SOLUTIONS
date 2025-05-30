    def largestNumber(nums)r:
        nums_str = list(map(str, nums))
        n = len(nums_str)
        
        # Nested loop for custom sorting
        for i in range(n):
            for j in range(i + 1, n):
                if nums_str[i] + nums_str[j] < nums_str[j] + nums_str[i]:
                    nums_str[i], nums_str[j] = nums_str[j], nums_str[i]
        
        # Join all numbers
        largest_num = ''.join(nums_str)
        
        # Handle case where the result is multiple zeros, e.g. "000"
        if largest_num[0] == '0':
            return '0'
        
        return largest_num
