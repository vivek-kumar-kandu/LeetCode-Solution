class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> ans;
        int m = matrix.size();    // row
        int n = matrix[0].size(); // col
        int total = m * n;
        int firstrow = 0;
        int firstcol = 0;
        int lastrow = m - 1;
        int lastcol = n - 1;
        int count = 0;
        while (count < total) {
            // first row
            for (int i = firstcol; i <= lastcol && count < total; i++) {
                ans.push_back(matrix[firstrow][i]);
                count++;
            }
            firstrow++;
            // last col
            for (int i = firstrow; i <= lastrow && count < total; i++) {
                ans.push_back(matrix[i][lastcol]);
                count++;
            }
            lastcol--;
            // lastrow
            for (int i = lastcol; i >= firstcol && count < total; i--) {
                ans.push_back(matrix[lastrow][i]);
                count++;
            }
            lastrow--;
            // first col
            for (int i = lastrow; i >= firstrow && count < total; i--) {
                ans.push_back(matrix[i][firstcol]);
                count++;
            }
            firstcol++;
        }
        return ans;
    }
};