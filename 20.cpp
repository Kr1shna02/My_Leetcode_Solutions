#include <stack>
#include <iostream>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> check;
        for (int i = 0; i < size(s); i++) {
            if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
                check.push(s[i]);
                cout << s[i] << endl;
            } else {
                if (check.empty()) {
                    return false;  
                }
                switch (s[i]) {
                    case ')':
                        if (check.top() == '(') {
                            check.pop();
                        } else {
                            return false;  
                        }
                        break;
                    case '}':
                        if (check.top() == '{') {
                            check.pop();
                        } else {
                            return false;  
                        }
                        break;
                    case ']':
                        if (check.top() == '[') {
                            check.pop();
                        } else {
                            return false; 
                        }
                        break;
                }
            }
        }
        return check.empty();
    }
};
