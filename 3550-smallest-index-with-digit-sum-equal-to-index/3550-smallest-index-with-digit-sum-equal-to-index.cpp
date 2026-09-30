class Solution {
public:
    int smallestIndex(vector<int>& nums) {
        for (int i = 0; i <= nums.size() - 1; i++) {
            int res = 0;
            int x = nums[i];
            while (x > 0) {
                res = res + x % 10;
                x = x / 10;
            }
            if (res == i) {
                return i;
            }
        }
        return -1;
    }
};