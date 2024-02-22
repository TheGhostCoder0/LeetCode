func findMaxConsecutiveOnes(nums []int) int {
    count := 0
    cur := 0
    for _, num := range nums {
        if num == 1 {
            cur += 1
        } else {
            cur = 0
        }
        if cur > count {
            count = cur
        } 
    }
    return count
}
