class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = []
        for i in range(numRows):
            ret.append([])
            for j in range(i+1):
                ret[i].append([])
                if j == 0 or j == i:
                    ret[i][j] = 1
                else:
                    ret[i][j] = ret[i - 1][j - 1] + ret[i - 1][j]
        return ret
