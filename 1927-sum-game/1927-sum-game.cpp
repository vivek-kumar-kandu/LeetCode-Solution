class Solution {
public:
    bool sumGame(string num) {
        int n = num.length();
        int left_know_sum = 0;
        int right_know_sum = 0;
        int left_Qn_mark = 0;
        int right_Qn_mark = 0;
        int total_Qn_mark = 0;

        for (int i = 0; i < n; i++) {
            if (num[i] == '?') {
                if (i < n / 2) {
                    left_Qn_mark++;
                } else {
                    right_Qn_mark++;
                }
            } else {
                if (i < n / 2) {
                    left_know_sum += num[i] - '0';
                } else {
                    right_know_sum += num[i] - '0';
                }
            }
        }
        total_Qn_mark = left_Qn_mark + right_Qn_mark;
        if (total_Qn_mark % 2 == 1) {
            return true;
        }
        int Left = 2 * left_know_sum + 9 * left_Qn_mark;
        int Right = 2 * right_know_sum + 9 * right_Qn_mark;
        if (Left == Right) {
            return false;
        } else {
            return true;
        }
    }
};