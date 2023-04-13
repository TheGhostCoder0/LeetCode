class Solution {
public:
    int mySqrt(int x) {
        for (long unsigned int i = 0; i < x; i++)
        {
            if ((i + 1) * (i + 1) == x)
            {
                return i + 1;
            }
            if ((i + 1) * (i + 1) > x)
            {
                return i;
            }
        }
        return 0;
    }
};
