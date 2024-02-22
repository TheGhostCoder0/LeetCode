func fib(n int) int {
    nums := []int{0, 1}


    for i := 2; i < n + 1; i += 1 {
        nums = append(nums, nums[i - 1] + nums[i - 2]) 
    }
    return nums[n]
}
