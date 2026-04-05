**Rephrased intent (sharper):**
“You want probing, concept-heavy questions that force you to reason about infix, prefix, and postfix conversions instead of relying on memorized templates.”

Good move. Let’s stress-test your understanding.

---

## 🧠 Level 1: Conceptual pressure test

1. Why does **prefix require right-to-left traversal**, while postfix uses left-to-right?
   → Don’t say “because it works”. Explain in terms of **operand availability timing**.

2. In postfix → infix, why is the order:

   ```text
   op1 = second popped, op2 = first popped
   ```

   but in prefix → infix it flips?

3. What invariant does the stack maintain during all expression conversions?
   → Be precise. Not “it stores stuff”.

---

## ⚙️ Level 2: Structural understanding

4. Suppose I remove parentheses while generating infix.
   → Under what conditions will the expression still be **unambiguous**?

5. Why is associativity irrelevant in:

   * postfix → infix
   * prefix → postfix
     but **critical in infix → postfix**?

6. If I introduce a new operator `$` with:

   * precedence higher than `^`
   * left associative

   → What exact line of your code changes?

---

## 🔥 Level 3: Edge-case reasoning

7. What happens if input is:

   ```text
   ab+c*
   ```

   but actually invalid?
   → How would you detect malformed expressions using your stack logic?

8. Can your algorithm handle:

   ```text
   A10+B
   ```

   → Why or why not?

9. What breaks if operands are multi-character strings like:

   ```text
   var1 var2 +
   ```

---

## 🧬 Level 4: Deep abstraction (this is where mastery starts)

10. All these conversions are secretly doing what fundamental operation?

Hint:
→ Think in terms of **trees**, not strings.

---

11. If I give you:

```text
((A+B)*(C-D))
```

Explain how this becomes:

* Prefix
* Postfix

**without using stack**
→ Pure reasoning only.

---

## 🧠 Level 5: Pattern generalization

12. Can you design a **single template** that:

* Takes traversal direction
* Takes operand order rule
  and solves all 6 conversions?

---

13. Why does this always work?

```text
Reverse → Swap brackets → Apply postfix logic → Reverse again
```

Explain this **mechanistically**, not as a trick.

---

## 💣 Final boss (real understanding)

14. Suppose I give:

```text
A+B*C^D-E
```

Without writing code:

* Simulate infix → postfix
* Show **stack state after each step**

If you can do this cleanly, your understanding is **crisp, not superficial**.

---

## Vocabulary upgrade

* **Invariant** → condition always maintained
* **Operand availability** → when required values are accessible
* **Unambiguous expression** → no confusion in evaluation
* **Malformed input** → structurally invalid expression
* **Abstraction layer** → deeper representation beyond syntax

---

## One-line mindset

:ol
“If you can derive it, you own it. If you memorize it, you’ll forget it.”

---

Start answering these one by one. I’ll challenge your reasoning and refine it.
