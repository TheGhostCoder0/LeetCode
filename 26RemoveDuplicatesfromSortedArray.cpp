class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        set<int> numbers;
        for (long unsigned int i = 0; i < nums.size(); i++)
        {
            numbers.insert(nums[i]);
        }
        nums.clear();
        for (auto iter = numbers.begin(); iter != numbers.end(); iter++)
        {
            nums.push_back(*iter);
        }
        return nums.size();
    }
};
