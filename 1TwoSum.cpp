class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> target_nums;

        for (int i = 0; i < nums.size(); ++i)
        {
            for (int j = 0; j < nums.size(); ++j)
            {
                if (i == j){
                    continue;
                }
                else if (nums[i] + nums[j] == target){
                    target_nums.push_back(i);
                    target_nums.push_back(j);
                    return target_nums;
                }
            } 
        }
        return target_nums;
    }
};
