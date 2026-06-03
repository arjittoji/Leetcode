class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> v;
        int sum = 0;
        for(int i = 0; i < nums.size(); i++)
        {
            sum+=nums[i];
            v.emplace_back(sum);
        }
        return v;
    }
};