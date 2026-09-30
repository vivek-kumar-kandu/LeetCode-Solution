class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int max_length = 0;
        int count = 0;
        for(int i= 0;i<nums.size();i++){
            if(nums[i]==1){
                count++;
                max_length=max(max_length,count);
            }
            else{
                count=0;
            }

        }
        return max_length;
    }
};