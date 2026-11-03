class Solution {
public:
    int minMoves2(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int mid = (n - 1) / 2;
        int step = 0;
        int target = nums[mid];
        for (int i = 0; i < n; i++) {
            step += abs(nums[i]-target);
        }
        return step;
    }
};