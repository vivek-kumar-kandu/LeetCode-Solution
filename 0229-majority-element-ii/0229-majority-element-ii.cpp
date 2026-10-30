class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int n = nums.size();
        int freq = floor(n / 3);
        sort(nums.begin(), nums.end());
        vector<int> ans;
        int count = 1;
        for (int i = 0; i < n - 1; i++) {

            if (nums[i] == nums[i + 1]) {
                count++;

            } else {
                if (count > freq) {
                    ans.push_back(nums[i]);
                }
                count = 1;
            }
        }
        if (count > freq) {
            ans.push_back(nums[n - 1]);
        }
        return ans;
    }
};