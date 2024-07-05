# Linux Shell Scripting

## Things to keep in mind if you've came from another programming langages
- When transitioning from languages like C to Bash scripting, here are some key points to keep in mind to avoid common pitfalls and ensure smooth scripting:

1. **Whitespace Sensitivity:** In Bash scripting, spaces and quotes are crucial for correct syntax:
   - **`[[ ]]` and `[ ]`:** Ensure there are spaces around `[[ ]]` or `[ ]` when using conditional expressions. For example, `[[ -z "$var" ]]` is correct, while `[[ -z"$var" ]]` may not work as expected.
   - **`=` and `==`:** In conditional statements (`[[ ]]`), `=` and `==` are used for string comparison, and they should have spaces around them. For example, `[[ $var == "value" ]]` is correct, while `[[ $var=="value" ]]` may not work correctly.

2. **Quoting:** Bash is sensitive to quoting:
   - **Variable Expansion:** Always quote variables when expanding them to prevent word splitting and globbing issues. For example, use `"$var"` instead of `$var`.
   - **Single vs. Double Quotes:** Use double quotes for most string literals and variable expansions to prevent unintended word splitting and globbing. Single quotes should be used when you want to prevent all expansions inside the quotes.

3. **Command Substitution:** Use `$()` for command substitution instead of backticks (`), as `$()` is more readable and nests correctly.

4. **Arrays:** Bash supports arrays, but they are different from arrays in C. Array indexing starts from 0, and there are no explicit data types for elements.

5. **Variable Assignment:** No spaces around the assignment operator (`=`) when assigning values to variables (`var="value"`).

6. **Functions:** Functions in Bash are similar to functions in C, but there are differences in scope and variable handling. Variables are global by default unless explicitly declared local.

7. **Exit Status:** Pay attention to the exit status of commands (`$?`). In Bash, `0` usually indicates success, while non-zero values indicate failure.

8. **Comments:** Use `#` for comments in Bash scripts, similar to `//` in C++.

9. **Flow Control:** Bash supports `if...else`, `for`, `while`, and `until` constructs similar to other programming languages, but syntax and control flow may differ slightly.

10. **Error Handling:** Bash scripts can use `set -e` to exit immediately if any command fails (`errexit`), similar to checking return codes explicitly in C.



## Points
- [] has wider compatability
- [[ ]] supports more complex expression but compatibility is less and works mostly in modern shells
