#include<vector>
#include<algorithm>
class RecentCounter {
private:
    vector<int> v;
public:
    RecentCounter() {
    
    }
    
    int ping(int t) {
        v.push_back(t);
        int range[2]={t-3000,t};
        sort(range,range+2);
        int count=0;
        for(auto x:v){
            if (x<=range[1] && x>=range[0]){
                count+=1;
            }
        }
        return count;
    }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */