class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int n=nums.size();
        int freq=floor(n/2);
        sort(nums.begin(),nums.end());
        int ans;
        int count = 1;
        for (int i = 0; i < n - 1; i++) {

            if (nums[i] == nums[i + 1]) {
                count++;

            } else {
                if (count > freq) {
                    ans=nums[i];
                }
                count = 1;
            }
        }
        if (count > freq) {
            ans=nums[n - 1];
        }
        return ans;
    }
};