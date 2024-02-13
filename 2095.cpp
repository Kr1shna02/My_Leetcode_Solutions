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
    ListNode* deleteMiddle(ListNode* head) {
        int size=0;
        struct ListNode *i=head;
        while(i!=nullptr){
            i=i->next;
            size++;
        }
        if(size==1){
            head=nullptr;
            return head;
        }
        if(size%2 ==0){
            size=size/2-1;
            struct ListNode *i=head;
            while(size>0){
                i=i->next;
                size--;
            }
            if((i->next!=nullptr) && (i->next->next!=nullptr)){
               struct ListNode *temp=i->next->next;
               i->next=temp;
               return head; 
            }
            else{
                i->next=nullptr;
                return head;
            }
        }
        else{
            size=size/2-1;
            struct ListNode *i=head;
            while(size>0){
                i=i->next;
                size--;
            }
            if((i->next!=nullptr) &&(i->next->next!=nullptr)){
               struct ListNode *temp=i->next->next;
               i->next=temp;
               return head; 
            }
            else{
                i->next=nullptr;
                return head;
            }
        return head;
        
    }
    }
};