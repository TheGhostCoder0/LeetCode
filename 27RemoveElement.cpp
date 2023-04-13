class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        vector<int> temp;
        for (long unsigned int i = 0; i < nums.size(); i++)
        {
            if (nums[i] != val)
            {
                temp.push_back(nums[i]);
            }
        }
        nums.clear();
        for (long unsigned int i = 0; i < temp.size(); i++)
        {
            nums.push_back(temp[i]);
        }
        return nums.size();
    }
};
