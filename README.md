# PolishNotation
This code finds the correct result when adding, subtracting, multiplying, and dividing the divisor polish notation.

# Explanation
The expression for adding the numbers 1 and 2 is, in Polish notation, written + 1 2 rather than 1 + 2. In more complex expressions, the operators still precede their operands, but the operands may themselves be nontrivial expressions including operators of their own. For instance, the expression that would be written in conventional infix notation as

(5 − 6) × 7
can be written in Polish notation as

× (− 5 6) 7
Since the simple arithmetic operators are all binary (at least, in arithmetic contexts), any prefix representation thereof is unambiguous, and bracketing the prefix expression is unnecessary. As such, the previous expression can be further simplified to

× − 5 6 7
The processing of the product is deferred until its two operands are available (i.e., 5 minus 6, and 7). As with any notation, the innermost expressions are evaluated first, but in Polish notation this "innermost-ness" can be conveyed by order rather than bracketing.

In the classical notation, the parentheses in the infix version were required, since moving them

5 − (6 × 7)
or simply removing them

5 − 6 × 7
would change the meaning and result of the overall expression, due to the precedence rule.

Similarly

5 − (6 × 7)
can be written in Polish notation as

− 5 × 6 7
One thing to keep in mind is that when executing an operation, the operation is applied to the first operand by the second operand. This is not an issue with operations that commute, but for non-commutative operations like division or subtraction, this fact is crucial to the analysis of a statement. For example, ÷ 10 5 is read as "divide 10 by 5", not "divide 5 by 10".
