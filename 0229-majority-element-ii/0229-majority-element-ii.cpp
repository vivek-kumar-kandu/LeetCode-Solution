class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int n = nums.size();
        map<int, int>freq;
        for(int i=0; i<n; i++){
            freq[nums[i]]++;
        }

        vector<int>ans;
        for(auto it: freq){
            if(it.second >(n/3)) ans.push_back(it.first);
        }
        return ans;


        // int ele1=0 , ele2=0 ,cnt1=0 ,cnt=0;
        // for(int i=0;i<n;i++){
            
        // }
    }
};