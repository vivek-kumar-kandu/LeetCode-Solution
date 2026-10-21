class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        // int m = matrix.size();
        // int n = matrix[0].size();
        // vector<vector<int>> temp = matrix;
        // // O((m*n)*(n+m))
        // for (int i = 0; i < m; i++) {
        //     for (int j = 0; j < n; j++) {
        //         if (matrix[i][j] == 0) {
        //             for (int k = 0; k < n; k++) {
        //                 temp[i][k] = 0; // putting 0 on ith row
        //             }
        //             for (int k = 0; k < m; k++) {
        //                 temp[k][j] = 0; // putting 0 on jth column
        //             }
        //         }
        //     }
        // }
        // matrix = temp;

        // 2nd app
        int m = matrix.size();
        int n = matrix[0].size();

        vector<bool> row(m, false);
        vector<bool> col(n, false);

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0) {
                    row[i] = true;
                    col[j] = true;
                }
            }
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (row[i] == true || col[j] == true) {
                    matrix[i][j] = 0;
                }
            }
        }
    }
};
