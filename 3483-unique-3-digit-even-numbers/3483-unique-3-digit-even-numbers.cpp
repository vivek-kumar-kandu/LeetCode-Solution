class Solution {
public:
    int totalNumbers(vector<int>& digits) {
        unordered_set<int>set;
        int n  = digits.size();

        for(int i =0;i<n;i++){
            for(int j = 0 ;j<n;j++){
                for(int k =0 ; k<n;k++){
                    if(i==j||j==k||k==i){
                        continue;
                    }
                    int num = digits[i]*100+digits[j]*10+digits[k]*1;
                    if(num >=100 && num %2==0){
                        set.insert(num);
                    }
                }
            }
        }
        vector<int> result(begin(set),end(set));
        sort(begin(result),end(result));
        return result.size();
    }
};