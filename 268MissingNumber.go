func missingNumber(nums []int) int {
    sum := 0
    max := len(nums)
    for _, val := range nums {
        sum += val
    }
    newSum := 0
    for i := 0; i <= max; i++ { 
        newSum += i
    }
    return newSum - sum
}
