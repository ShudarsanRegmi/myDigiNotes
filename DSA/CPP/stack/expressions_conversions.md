# Expressions Conversions


## Infix to Postfix
```cpp
class Solution {
  public:
  
  int prec(char c) {
    if (c == '^') return 3;
    else if (c == '/' || c == '*') return 2;
    else if (c == '+' || c == '-') return 1;
    return -1;
}
    // Function to convert an infix expression to a postfix expression.
    string infixToPostfix(string& s) {
        string result;
        char c;
        stack<char> st;
        
        for (int i=0; i<s.length(); i++) {
            c = s[i];
            
            // if it is operand append to result
            if((c>='a'&& c<= 'z') || (c>='A' && c<= 'Z') || (c >= '0' && c<= '9')) {
                result += c;
            }
            
            // if it is ( push
            else if (c== '(') st.push(c);

            // if it is ) pop and append until ) (pop ) too)
            else if (c == ')') {
                while(st.top() != '(') {
                    result += st.top();
                    st.pop();
                }
                st.pop();
            }
            // this should be a valid operand, if c has less precedence then pop and append until current char has the highest precedence
            else {
                while(!st.empty() && prec(c) <= prec(st.top())) {
                    result += st.top();
                    st.pop();
                }
                st.push(c);
            }
        }
        
        while(!st.empty()) {
            result += st.top();
            st.pop();
        }
        return result;
    }
};
 // geeksforgeeks submission
```
**Practice Before lab Exam**

```cpp
#include <iostream>
#include <stack>

using namespace std;

int prec(char c) {
    if (c == '^') {
        return 3;
    }else if (c == '/' || c == '*') {
        return 2;
    }else if (c == '+' || c == '-') {
        return 1;
    }else {
        return -1;
    }
}

string infToPost(string inp) {
    string result;
    stack<char> st;

    for (char c : inp) {
        // if the char is opearand append to result
        if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9')) {
            result += c;
        }

        // if it is ( push it to stack
        else if (c == '(') {
            st.push(c);
        }

        // if it is ) pop and append until ( is found
        else if (c == ')') {
            while (st.top() != '(') {
                result += st.top();
                st.pop();
            }
            st.pop(); // pop the (
        }

        else {
            // it must be an operator : rule: precedence , pop until current char has high precedence
            while (!st.empty() && prec(c) <= prec(st.top())) {
                result += st.top();
                st.pop();
            }
            st.push(c);
        }

    }

    while (!st.empty()) {
        result += st.top();
        st.pop();
    }
    return result;
}

int main() {
    string inp = "a+b*(c^d-e)^(f+g*h)-i";
    string postfix = infToPost(inp);
    cout << postfix << endl;
}
```

