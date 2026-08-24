class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int start = 0, end = 0;
        int max_lenght = 0;
        unordered_set<char> st;

        while (end < s.length()) {

            if (st.find(s[end]) == st.end()) {
                st.insert(s[end]);
                max_lenght = max(max_lenght, end - start + 1);
                end++;

            } else {

                st.erase(s[start]);
                start++;
            }
        }
        return max_lenght;
    }
};