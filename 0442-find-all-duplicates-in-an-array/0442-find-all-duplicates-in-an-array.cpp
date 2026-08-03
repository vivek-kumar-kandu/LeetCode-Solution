// 1st approach
// class Solution {
// public:
//     vector<int> findDuplicates(vector<int>& nums) {
//     std::unordered_map<int,int>hash_map;
//     vector<int>ans;
//     for(int num:nums ){
//         hash_map[num]++;
//     }
//     for(auto it :hash_map){
//         if(it.second!=1) ans.push_back(it.first);
//     }
//     return ans;
//     }
// };

// 2nd approach
//  class Solution {
//  public:
//      vector<int> findDuplicates(vector<int>& nums) {
//      sort(nums.begin(), nums.end());
//      vector<int>ans;
//      for (int i=0; i<nums.size()-1;i++){
//          if(nums[i]==nums[i+1]){
//              ans.push_back(nums[i]);
//          }
//      }
//      return ans;
//      }
//  };

// 3 =rd approach

class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> ans;
        for (int i = 0; i < nums.size(); i++) {
            int index = abs(nums[i]) - 1;
            if (nums[index] < 0) {
                ans.push_back(abs(nums[i]));
            } else {
                nums[index] = -nums[index];
            }
        }
        return ans;
    }
};
