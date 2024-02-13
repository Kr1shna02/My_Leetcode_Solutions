/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    vector<int> nextLargerNodes(ListNode* head) {
        vector<int> arr;
        struct ListNode *i=head;
        while(i->next!=nullptr){
            struct ListNode*j=i;
            int size=arr.size();
            while(j!=nullptr){
                if((j->val)>(i->val)){
                    arr.push_back(j->val);
                    break;
                }
                j=j->next;
            }
            if(size==arr.size()){
                arr.push_back(0);
            }
            i=i->next;
        }
        arr.push_back(0);
        
        return arr;
    }
};