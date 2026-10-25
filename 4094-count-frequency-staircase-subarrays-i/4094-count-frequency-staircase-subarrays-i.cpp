class Solution {
public:
    int countStaircase(vector<int>& nums) {
        int ans = 0;  // valid subarray count
        for (int i = 0; i < nums.size(); i++) {
            unordered_map<int, int> freq;
            vector<int> order;
            for (int j = i; j < nums.size(); j++) {
                if (freq[nums[j]] == 0) {
                    order.push_back(nums[j]);
                }
                freq[nums[j]]++;
                bool valid = true;
                for (int z = 0; z < order.size(); z++) {
                    if (freq[order[z]] != z + 1) {
                        valid = false;
                        break;
                    }
                }
                if (valid) {
                    ans++;
                }
            }
        }
        return ans;
    }
};