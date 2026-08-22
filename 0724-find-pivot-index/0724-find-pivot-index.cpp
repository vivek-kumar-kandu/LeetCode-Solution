class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int left_sum = 0;
        int right_sum = 0;
        int total = 0;
        for (int i = 0; i <= nums.size() - 1; i++) {
            total = total + nums[i];
        }
        for (int j = 0; j <= nums.size() - 1; j++) {
            int curr = nums[j];
            right_sum = total - curr - left_sum;
            if (right_sum == left_sum) {
                return j;
            } else {
                left_sum = left_sum + curr;
                right_sum = total - left_sum - curr;
            }
        }
        return -1;
    }
};