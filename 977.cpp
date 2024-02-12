class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> result;
        for(auto i:nums){
            result.push_back(i*i);
        }
        sort(result.begin(),result.end());
        return result;
    }
};