class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> result;
        int l,r;
        l=0;
        r=numbers.size()-1;
        while(1){
            if ((numbers[l]+numbers[r])>target){
                r-=1;
            }
            else if((numbers[l]+numbers[r])<target){
                l+=1;
            }
            else{
                result.push_back(l+1);
                result.push_back(r+1);
                return result;
            }
        }
        return result;
    }
};
