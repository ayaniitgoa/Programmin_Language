## Creating A basic Programming Language

### Currently working on/completed:

1. Lexer : A lexer takes an input and converts it into tokens (symbols, string, parentheses, brackets, commas, etc.).
   - For eg.
     ```bash
      command >> 1 + 2
      [INT: 1, PLUS, INT: 2]
     ```
     ```bash
      command >> 3/4
      [INT: 3, DIV, INT: 4]
     ```
     ```bash
      command >> 2.5 * 2.5
      [FLOAT: 2.5, MUL, FLOAT: 2.5]
     ```
     ```bash
      command >> 8 - $
      Invalid Character found: '$'
      File <stdin>, line 1
     ```

#### Licensed under [MIT License](License).
