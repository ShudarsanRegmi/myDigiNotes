# Mysql Regex

Certainly! Here's a concise list of commonly used regular expression components:

### Basic Components

- `.`: Matches any single character except newline.
- `^`: Anchors the match at the start of a string.
- `$`: Anchors the match at the end of a string.
- `*`: Matches 0 or more occurrences of the preceding element.
- `+`: Matches 1 or more occurrences of the preceding element.
- `?`: Matches 0 or 1 occurrence of the preceding element.
- `|`: Acts as a logical OR between patterns.

### Character Classes

- `[abc]`: Matches any single character a, b, or c.
- `[^abc]`: Matches any single character except a, b, or c.
- `[a-z]`: Matches any single lowercase letter.
- `[A-Z]`: Matches any single uppercase letter.
- `[0-9]`: Matches any single digit.
- `\d`: Matches any single digit (equivalent to `[0-9]`).
- `\D`: Matches any non-digit character.
- `\w`: Matches any word character (alphanumeric + underscore).
- `\W`: Matches any non-word character.
- `\s`: Matches any whitespace character.
- `\S`: Matches any non-whitespace character.

### Quantifiers

- `{n}`: Matches exactly n occurrences of the preceding element.
- `{n,}`: Matches n or more occurrences of the preceding element.
- `{n,m}`: Matches between n and m occurrences of the preceding element.

### Anchors and Boundaries

- `\b`: Matches a word boundary.
- `\B`: Matches a non-word boundary.

### Groups and Alternation

- `()`: Groups multiple tokens together and remembers the matched text.
- `(?:)`: Groups multiple tokens together without remembering the matched text.
- `|`: Acts as a logical OR between patterns.

### Escaping Special Characters

- `\`: Escapes a special character (e.g., `\.` matches a literal period).

### Practical Examples

- Email Validation: `^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$`
- Phone Number: `^\+?[0-9]{1,3}?[-. ]?\(?[0-9]{1,4}?\)?[-. ]?[0-9]{1,4}[-. ]?[0-9]{1,9}$`
- URL: `^(https?|ftp)://[^\s/$.?#].[^\s]*$`
