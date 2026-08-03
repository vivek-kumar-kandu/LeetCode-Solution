class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        std::unordered_map<int,int>hash_map;
        for( int num : arr){
            hash_map[num]++;
        }
        std::unordered_set<int> seen;
        for(auto it : hash_map){
            if(seen.count(it.second)){
                return false ;
            }
            seen.insert(it.second);
        }
        return true;
    }
};