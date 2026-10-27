class Solution {
public:
    vector<string> createGrid(int m, int n) {
        vector<string> result;
        for (int i = 0; i < m; i++) {
            if (i == 0) {
                string temp = "";
                for (int j = 0; j < n; j++) {
                    temp += ".";
                }
                result.push_back(temp);
            } else {
                string temp = "";
                for (int j = 0; j < n - 1; j++) {
                    temp += "#";
                }
                temp += ".";
                result.push_back(temp);
            }
        }
        return result;
    }
};