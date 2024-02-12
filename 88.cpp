class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int k=0;
        for(auto i:nums1){
            if(k>=m){
                nums1.pop_back();
            }
            else{
                ++k;
            }
        }
        for(auto j: nums2){
            nums1.push_back(j);
        }
        sort(nums1.begin(),nums1.end());
    }
};