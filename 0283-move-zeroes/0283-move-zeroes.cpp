class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        // int p=0;
        // int q=nums.size()-1;
        // while(p<q){
        //     if(nums[p]==0&&nums[q]!=0){
        //         swap(nums[p],nums[q]);
        //         p++;
        //         q--;
        //     }
        //     else if(nums[p]!=0&&nums[q]==0){
        //         p++;
        //         q--;
        //     }
        //     else if(nums[p]==0&&nums[q]==0){
        //         q--;
        //     }
            
        //     else if(nums[p]!=0&&nums[q]!=0){
        //         p++;
        //     }
        // }

                int p = 0;

        for (int q = 0; q < nums.size(); q++) {
            if (nums[q] != 0) {
                swap(nums[p], nums[q]);
                p++;
            }
        }

    }
};