class Solution {
public:
    int numberOfBeams(vector<string>& bank) {
        int res[bank.size()];
        int l=bank.size();
        int i=0;
        for(auto x:bank){
            int count=0;
            for(int i=0;i<x.size();i++){
                if (x[i]=='1'){
                    count++;
                }
            }
            res[i]=count;
            ++i;
        }
        int result=0;
        int temp=res[0];
        for(int i=1;i<l;i++){
            if(res[i]!=0){
                result+=temp*res[i];
                temp=res[i];
            }
        }
        return result;
    }
};