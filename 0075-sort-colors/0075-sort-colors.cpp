class Solution {
public:
    void sortColors(vector<int>& nums) {
        int n = nums.size();
        int left = 0;
        int right = n - 1;
        int mid = 0;
        // while (left < right) {
        //     if (nums[left] == 0 && nums[right] == 2) {
        //         left++;
        //         right--;
        //     } else if (nums[left] == 2 && nums[right] == 0) {
        //         swap(nums[left], nums[right]);
        //         left++;
        //         right--;
        //     } else if (nums[left] == 2 && nums[right] == 2) {
        //         right--;
        //     } else if (nums[left] == 0 && nums[right] == 0) {
        //         left++;
        //     } else if (nums[left] == 0 && nums[right] == 1) {
        //         left++;

        //     } else if (nums[left] == 1 && nums[right] == 0) {
        //         swap(nums[left], nums[right]);
        //         left++;

        //     } else if (nums[left] == 1 && nums[right] == 1) {
        //         right--;

        //     } else if (nums[left] == 1 && nums[right] == 2) {
        //         right--;
        //     } else if (nums[left] == 2 && nums[right] == 1) {
        //         swap(nums[left], nums[right]);
        //         right--;
        //     }
        // }

        while (mid <= right) {
            if (nums[mid] == 0) {
                swap(nums[mid], nums[left]);
                left++;
                mid++;
            } else if (nums[mid] == 1) {
                mid++;
            } else if (nums[mid] == 2) {
                swap(nums[mid], nums[right]);
                right--;
            }
        }
    }
};