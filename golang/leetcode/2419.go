package leetcode

func LongestSubarray(nums []int) int {
	l, max_num, max_len := 0, 0, 0

	for _, num := range nums {
		if num > max_num {
			l, max_num, max_len = 1, num, 1
		} else if num == max_num {
			l += 1
			max_len = max(l, max_len)
		} else {
			l = 0
		}
	}

	return max_len
}
