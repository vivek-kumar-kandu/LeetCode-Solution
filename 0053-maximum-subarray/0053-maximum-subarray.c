int maxSubArray(int* nums, int numsSize) {
    int maxSum =INT_MIN ;
     int CurrentSum = 0 ;
    for (int i = 0; i < numsSize; i++) {
        
              CurrentSum = CurrentSum + nums[i];
              maxSum = fmax(CurrentSum, maxSum);
              if(CurrentSum < 0){
                CurrentSum=0;
              }
    }
    return maxSum;
}