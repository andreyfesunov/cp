package leetcode

func countSubsets(
	memo map[int]map[int]int,
	nums []int,
	index int,
	current_or int,
	target_or int,
) int {
	if index == len(nums) {
		if current_or == target_or {
			return 1
		}

		return 0
	}

	if _, exists := memo[index]; !exists {
		memo[index] = make(map[int]int)
	} else if val, exists := memo[index][current_or]; exists {
		return val
	}

	result := countSubsets(memo, nums, index+1, current_or, target_or) + countSubsets(memo, nums, index+1, current_or|nums[index], target_or)

	memo[index][current_or] = result

	return result
}

func CountMaxOrSubsets(nums []int) int {
	memo := make(map[int]map[int]int)
	max_v := 0

	for _, v := range nums {
		max_v |= v
	}

	return countSubsets(memo, nums, 0, 0, max_v)
}
