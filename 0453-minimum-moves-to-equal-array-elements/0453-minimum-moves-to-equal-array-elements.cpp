class Solution {
public:
    int minMoves(vector<int>& nums) {
        int step = 0;
        int sum = 0;
        int mini = nums[0];
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            sum += nums[i];
            mini = min(mini, nums[i]);
        }
        step = sum - n * mini;
        return step;
    }
};