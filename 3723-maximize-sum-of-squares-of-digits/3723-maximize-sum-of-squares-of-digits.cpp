class Solution {
public:
    string maxSumOfSquares(int num, int sum) {
        string ans;

        if (sum > num*9) {
            
            return "";
        }
        while (sum > 0 && num > 0) {
            int digit = min(sum, 9);
            ans+=char('0'+digit);
            sum = sum - digit;
            num = num - 1;
        }
        while (num > 0) {
            ans.push_back('0');
            num = num - 1;
        }
        return ans;
    }
};