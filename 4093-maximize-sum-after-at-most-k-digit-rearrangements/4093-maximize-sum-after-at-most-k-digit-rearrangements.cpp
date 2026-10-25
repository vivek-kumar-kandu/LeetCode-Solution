class Solution {
public:
    long long maximizeSum(vector<int>& nums, int k) {
        vector<long long> gain;
        long long sum = 0;
        for (int num : nums) {
            sum += num;
        }
        vector<int> bremovilta = nums;
        
        for (int num : nums) {
            string s = to_string(num);
            sort(s.rbegin(), s.rend());
            long long re_arrange = stoi(s);
            long long benefit = re_arrange - num;
            gain.push_back(benefit);
        }
        sort(gain.rbegin(), gain.rend());
        for (int i = 0; i < k; i++) {
            sum += gain[i];
        }

        return sum;
    }
};