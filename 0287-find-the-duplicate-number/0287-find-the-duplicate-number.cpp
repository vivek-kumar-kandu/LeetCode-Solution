class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int n = nums.size();
        vector<bool> ans(n, false);

        int i = 0;

        while (true) {
            if (ans[i] == true) {
                return i;
            } else {
                ans[i] = true;
                i = nums[i];
            }
        }
    }
};