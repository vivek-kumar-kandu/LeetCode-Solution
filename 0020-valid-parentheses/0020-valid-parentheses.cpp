class Solution {
public:
    bool isValid(string s) {
        stack<char> st;

        for (char c : s) {

            // Opening bracket
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);
            }

            // Closing bracket
            else {
                if (st.empty()) {
                    return false;
                }

                if ((c == ')' && st.top() == '(') ||
                    (c == '}' && st.top() == '{') ||
                    (c == ']' && st.top() == '[')) {
                    st.pop();
                }
                else {
                    return false;
                }
            }
        }

        return st.empty();
    }
};