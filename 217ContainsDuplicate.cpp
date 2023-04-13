class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int> s;
        int size = 0;
        for (long unsigned int i = 0; i < nums.size(); ++i)
        {
            s.insert(nums[i]);
            if (s.size() == size)
            {
                return true;
            }
            size = s.size();
        } 
        return false;
    }
};
