class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int s = 0;
        int e = nums.size() - 1;
        int mid = s + (e - s) / 2;
        int start = 0;
        int end = nums.size() - 1;
        int middle = start + (end - start) / 2;
        vector<int>result={-1,-1};
        while (s <= e) {
            if (nums[mid] == target) {
                result[0] = mid;
                e = mid - 1;
            } else if (nums[mid] < target) {
                s = mid + 1;

            } else {
                e = mid - 1;
            }
            mid = s + (e - s) / 2;
        }
        while (start <= end) {
            if (nums[middle] == target) {
                result[1] = middle;
                start = middle + 1;
            } else if (nums[middle] < target) {
                start = middle + 1;

            } else {
                end = middle - 1;
            }
            middle = start + (end - start) / 2;
        }
        return result;
    }
};