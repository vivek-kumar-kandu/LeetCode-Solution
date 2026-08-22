class Solution {
public:
    bool checkDivisibility(int n) {
        int add = 0;
        int multi = 1;
        int sum = 0;
        int new_n = n;
        while (n != 0) {
            int digit = n % 10;
            add = add + digit;
            multi = multi * digit;
            n = n / 10;
        }
        sum = add + multi;
        if (new_n % sum == 0) {
            return true;
        }
        return false ;
    }
};