class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Edge case for empty input
        if not nums:
            return 0
        
        max_product = nums[0]
        current_max = nums[0]
        current_min = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            
            # If the number is negative, swap the max and min
            if num < 0:
                current_max, current_min = current_min, current_max
            
            # Update the current_max and current_min
            current_max = max(num, current_max * num)
            current_min = min(num, current_min * num)
            
            # Update the global max_product
            max_product = max(max_product, current_max)
        
        return max_product

# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProduct([2, 3, -2, 4]))  # Output: 6
    print(solution.maxProduct([-2, 0, -1]))     # Output: 0
