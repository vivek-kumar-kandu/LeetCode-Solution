class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n=nums.size();
        k=k%n;
        // int first_part=n-k;
        // int second_part=k;
        // int left=0;
        // int right=n-1;
        // while(left<right){
        //     swap(nums[left],nums[right]);
        //     left++;
        //     right--;
        // }
        vector<int>ans(n);
        for(int i=0;i<n;i++){
            ans[(i+k)%n]=nums[i];
        }
        nums=ans;
        // reverse(nums.begin(),nums.end());
        // reverse(nums.begin(),nums.begin()+k);
        // reverse(nums.begin()+k,nums.end());
        // vector<int>ans(n);
        // for(int i=n-k;i<n;i++){
        //     ans[i-n+k]=nums[i];
        // }
        // for(int i=0;i<n-k;i++){
        //     ans[i+k]=nums[i];
        // }
        // for(int i=0;i<n;i++){
        //     nums[i]=ans[i];
        // }
    }
};