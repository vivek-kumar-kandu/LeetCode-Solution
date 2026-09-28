class Solution {
public:
    int maxDepth(string s) {
        int depth = 0;
        int max_depth = 0;

        for (auto i : s) {
            if (i == '(') {
                depth++;
                max_depth = max(max_depth, depth);
            } else if (i == ')'){
                depth--;
            }
        }
        return max_depth;
    }
};