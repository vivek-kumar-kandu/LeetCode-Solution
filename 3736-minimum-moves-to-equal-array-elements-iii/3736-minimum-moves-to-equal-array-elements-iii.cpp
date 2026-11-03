class Solution {
public:
    int minMoves(vector<int>& nums) {
        int step = 0;
        int n = nums.size();
        int maxi = 0;
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += nums[i];
            maxi = max(maxi, nums[i]);
        }
        step = maxi * n - sum;
        return step;
    }
};