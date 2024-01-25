class Solution {
public:
    int climbStairs(int n) {
        vector<int> fibs;
        fibs.push_back(1);
        fibs.push_back(1);
        for (long unsigned int i = 2; i <= n; ++i)
        {
            fibs.push_back(fibs[i-1] + fibs[i-2]);
        }
        return fibs[n];
    }
};
