#include<algorithm>
class Solution {
public:
    string firstPalindrome(vector<string>& words) {
        for(auto x: words){
            string y=x;
            reverse(x.begin(),x.end());
            if(y==x){
                return y;
            }
        }
        return "";
    }
};