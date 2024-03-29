class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort(reverse = True)
            if stones[0] == stones[1]:
                stones.remove(stones[1])
                stones.remove(stones[0])
            else:
                stones[0] -= stones[1]
                stones.remove(stones[1])

        if len(stones) == 1:
            return stones[0]
        else:
            return 0
