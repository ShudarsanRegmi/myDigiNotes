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

## Infix to prefix
```cpp
#include <iostream>
#include <stack>
#include <string>
#include <algorithm>

using namespace std;

int prec(char c) {
    if (c == '^') {
        return 3;
    } else if (c == '/' || c == '*') {
        return 2;
    } else if (c == '+' || c == '-') {
        return 1;
    } else {
        return -1;
    }
}

string infToPost(string inp) {
    string result;
    stack<char> st;

    for (char c : inp) {
        // if the char is an operand, append to result
        if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9')) {
            result += c;
        }
        // if it is '(', push it to stack
        else if (c == '(') {
            st.push(c);
        }
        // if it is ')', pop and append until '(' is found
        else if (c == ')') {
            while (!st.empty() && st.top() != '(') {
                result += st.top();
                st.pop();
            }
            st.pop(); // pop the '('
        }
        else { // it must be an operator
            // pop operators from the stack with higher or equal precedence
            while (!st.empty() && prec(c) <= prec(st.top())) {
                result += st.top();
                st.pop();
            }
            st.push(c);
        }
    }

    // Pop all the remaining operators from the stack
    while (!st.empty()) {
        result += st.top();
        st.pop();
    }
    return result;
}

string infixToPrefix(string inp) {
    // Reverse the input expression
    reverse(inp.begin(), inp.end());

    // Change '(' to ')' and ')' to '('
    for (int i = 0; i < inp.size(); i++) {
        if (inp[i] == '(') inp[i] = ')';
        else if (inp[i] == ')') inp[i] = '(';
    }

    // Call infixToPost to convert the reversed infix expression to postfix
    string prefix = infToPost(inp);

    // Reverse the resulting postfix expression to get the prefix expression
    reverse(prefix.begin(), prefix.end());

    return prefix;
}

int main() {
    string inp = "(a-b/c)*(a/k-l)";
    string prefix = infixToPrefix(inp);
    cout << prefix << endl;
}
//  workong on gdb, giving sigsegv in clion
```

## Postfix to infix

**Algorithm**
```
Algorithm 
1.While there are input symbol left 
…1.1 Read the next symbol from the input. 
2.If the symbol is an operand 
…2.1 Push it onto the stack. 
3.Otherwise, 
…3.1 the symbol is an operator. 
…3.2 Pop the top 2 values from the stack. 
…3.3 Put the operator, with the values as arguments and form a string. 
…3.4 Push the resulted string back to stack. 
4.If there is only one value in the stack 
…4.1 That value in the stack is the desired infix string. 
Below is the implementation of above approach:
```

```cpp
#include <iostream>
#include <stack>
#include <string>

using namespace std;

bool isOperand(char c) {return ((c >= 'a' && c<='z') || (c >= 'A' && c<='Z') || (c >= '0' && c<='9'));}

string postfixToInfix(string inp) {
    stack<string> st;
    for (char c : inp) {
        if (isOperand(c)) {
            st.push(string(1, c));
        }else {
            // it is an operator
            string op1 = st.top();
            st.pop();
            string op2 = st.top();
            st.pop();
            st.push("(" + op2 + c + op1 + ")");
        }
    }
    return st.top();
}

int main() {
    string postfix = "ab*c+";
    string infix = postfixToInfix(postfix);
    cout << infix << endl;
}
```

## Prefix to infix

**almost similar to above except**
```
need to read from right to left
op1 operator op2
```

```cpp
#include <iostream>
#include <stack>
#include <string>

using namespace std;

bool isOperand(char c) {return ((c >= 'a' && c<='z') || (c >= 'A' && c<='Z') || (c >= '0' && c<='9'));}

string prefixToInfix(string inp) {
    stack<string> st;
    char c;
    for (int i=inp.size()-1; i>=0; i--) {
        c = inp[i];
        if (isOperand(c)) {
            st.push(string(1, c));
        }else {
            // it is an operator
            string op1 = st.top();
            st.pop();
            string op2 = st.top();
            st.pop();
            st.push("(" + op1 + c + op2 + ")");
        }
    }
    return st.top();
}

int main() {
    string prefix = "*+AB-CD";
    string infix = prefixToInfix(prefix);
    cout << infix << endl;
}
```

## Prefix to Postfix
```
Read the Prefix expression in reverse order (from right to left)
If the symbol is an operand, then push it onto the Stack
If the symbol is an operator, then pop two operands from the Stack 
Create a string by concatenating the two operands and the operator after them. 
string = operand1 + operand2 + operator 
And push the resultant string back to Stack
Repeat the above steps until end of Prefix expression.
```

```cpp
#include <iostream>
#include <stack>

using namespace std;

// Function to check if a character is an operator
bool isOperator(char ch) {
    return (ch == '+' || ch == '-' || ch == '*' || ch == '/');
}

// Function to convert a prefix expression to a postfix expression
string prefixToPostfix(const string& prefix) {
    stack<string> st;
    int length = prefix.size();

    // Traverse the prefix expression from right to left
    for (int i = length - 1; i >= 0; i--) {
        char ch = prefix[i];

        // If the current character is an operator
        if (isOperator(ch)) {
            if (st.size() < 2) {
                cerr << "Error: Invalid prefix expression!" << endl;
                return "";
            }
            // Pop two operands from the stack
            string op1 = st.top(); st.pop();
            string op2 = st.top(); st.pop();

            // Concatenate in the order: operand1 operand2 operator
            string postfix = op1 + op2 + ch;

            // Push the resulting string back onto the stack
            st.push(postfix);
        } 
        // If the current character is an operand
        else {
            // Push the operand as a string onto the stack
            st.push(string(1, ch));
        }
    }

    // If stack does not contain exactly one element, the expression was invalid
    if (st.size() != 1) {
        cerr << "Error: Invalid prefix expression!" << endl;
        return "";
    }

    // Return the final postfix expression
    return st.top();
}

// Driver function
int main() {
    string prefixExpr = "*-A/BC-/AKL";

    cout << "Prefix Expression  : " << prefixExpr << endl;
    cout << "Converted Postfix  : " << prefixToPostfix(prefixExpr) << endl;

    return 0;
}
```

## Postfix to Prefix

```cpp
Read the Postfix expression from left to right
If the symbol is an operand, then push it onto the Stack
If the symbol is an operator, then pop two operands from the Stack 
Create a string by concatenating the two operands and the operator before them. 
string = operator + operand2 + operand1 
And push the resultant string back to Stack
Repeat the above steps until end of Postfix expression.
```

```cpp
#include <iostream>
#include <stack>

using namespace std;

// Function to check if a character is an operator
bool isOperator(char ch) {
    return (ch == '+' || ch == '-' || ch == '*' || ch == '/');
}

// Function to convert a postfix expression to a prefix expression
string postfixToPrefix(const string& postfix) {
    stack<string> st;
    int length = postfix.size();

    // Traverse the postfix expression from left to right
    for (int i = 0; i < length; i++) {
        char ch = postfix[i];

        // If the current character is an operator
        if (isOperator(ch)) {
            if (st.size() < 2) {
                cerr << "Error: Invalid postfix expression!" << endl;
                return "";
            }
            // Pop two operands from the stack
            string op2 = st.top(); st.pop();
            string op1 = st.top(); st.pop();

            // Concatenate in the order: operator operand1 operand2
            string prefix = ch + op1 + op2;

            // Push the resulting string back onto the stack
            st.push(prefix);
        } 
        // If the current character is an operand
        else {
            // Push the operand as a string onto the stack
            st.push(string(1, ch));
        }
    }

    // If the stack does not contain exactly one element, the expression was invalid
    if (st.size() != 1) {
        cerr << "Error: Invalid postfix expression!" << endl;
        return "";
    }

    // Return the final prefix expression
    return st.top();
}

// Driver function
int main() {
    string postfixExpr = "ABC/-AK/L-*";

    cout << "Postfix Expression  : " << postfixExpr << endl;
    cout << "Converted Prefix    : " << postfixToPrefix(postfixExpr) << endl;

    return 0;
}

```

