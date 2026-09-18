class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n=nums.size();
        // int first_part=n-k;
        // int second_part=k;
        // int left=0;
        // int right=n-1;
        // while(left<right){
        //     int temp=nums[left];
        //     nums[left]=nums[right];
        //     nums[right]=temp;
        //     left++;
        //     right--;
        // }
        k=k%n;
        reverse(nums.begin(),nums.end());
        reverse(nums.begin(),nums.begin()+k);
        reverse(nums.begin()+k,nums.end());
    }
};