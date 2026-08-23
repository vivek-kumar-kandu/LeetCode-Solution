class Solution {
public:
    long long int binarySearch(int n) {
        int s = 0;
        int e = n;
        long long int mid = s + (e - s) / 2;
        long long int ans=-1;

        while (s <= e) {
            long long int square = mid * mid;

            if (square == n) {
                return mid;
            }
            if (square < n) {
                ans = mid;
                s = mid + 1;
            } else {
                e = mid - 1;
            }
            mid = s + (e - s) / 2;
        }
        return ans;
    }

    int mySqrt(int x) {
        return binarySearch(x); 
    }
};

// class Solution {
// public:
//     int mySqrt(int x) {
//         if (x < 2) return x; // Handle 0 and 1

//         int left = 1, right = x / 2, ans;

//         while (left <= right) {
//             int mid = left + (right - left) / 2;

//             // Use division to prevent overflow: mid <= x / mid
//             if (mid <= x / mid) {
//                 ans = mid;     // Potential answer
//                 left = mid + 1; // Try larger values
//             } else {
//                 right = mid - 1; // Too big, go smaller
//             }
//         }
//         return ans;
//     }
// };