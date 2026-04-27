# Modal Performance Metrics
---

# :sd 1. Foundation → Confusion Matrix (anchor everything here)

|                 | Predicted Positive | Predicted Negative |
| --------------- | ------------------ | ------------------ |
| Actual Positive | TP = 8             | FN = 2             |
| Actual Negative | FP = 2             | TN = 8             |

Total = 20

---

# :sd 2. Running Examples (parallel understanding)

## Dog Example (intuitive)

* Dog detects thieves
* TP = 8 (correctly barked at thieves)
* FP = 2 (barked at innocent people)
* FN = 2 (missed thieves)
* TN = 8 (correctly ignored innocents)

---

## Professional Example (interview-ready)

**Credit Card Fraud Detection System**

* 20 transactions
* 10 are fraud, 10 are legitimate

Model results:

* TP = 8 → fraud correctly flagged
* FP = 2 → legit transactions wrongly blocked
* FN = 2 → fraud missed
* TN = 8 → legit correctly allowed

---

# :sd 3. Metrics (formal + intuition)

---

## 3.1 Precision

**Formula:**
[
Precision = \frac{TP}{TP + FP}
]

**Value:**
[
= \frac{8}{8 + 2} = 0.8
]

**Formal Definition:**
Proportion of predicted positives that are actually positive.

**Dog intuition:**
When dog barks, 80% chance it's actually a thief.

**Professional meaning:**
When system flags fraud, it's correct 80% of time.

**Key idea:**
👉 Reliability of positive prediction

---

## 3.2 Recall (Sensitivity)

**Formula:**
[
Recall = \frac{TP}{TP + FN}
]

**Value:**
[
= \frac{8}{8 + 2} = 0.8
]

**Formal Definition:**
Proportion of actual positives correctly identified.

**Dog intuition:**
Dog caught 80% of all thieves.

**Professional meaning:**
System detected 80% of all fraud cases.

**Key idea:**
👉 Coverage of actual positives

---

## 3.3 Accuracy

**Formula:**
[
Accuracy = \frac{TP + TN}{Total}
]

**Value:**
[
= \frac{8 + 8}{20} = 0.8
]

**Formal Definition:**
Proportion of total predictions that are correct.

**Dog intuition:**
Dog was right 80% overall.

**Professional meaning:**
System made correct decisions 80% of time.

**Key limitation:**
Fails in imbalanced datasets.

---

## 3.4 F1 Score

F1 = \frac{2 \cdot Precision \cdot Recall}{Precision + Recall}

**Value:**
= 0.8

**Formal Definition:**
Harmonic mean of precision and recall.

**Dog intuition:**
Dog is balanced: not over-barking, not missing much.

**Professional meaning:**
Model balances false alarms and missed frauds.

**Key idea:**
👉 Trade-off optimizer

---

## 3.5 ROC-AUC

Key components:

TPR = \frac{TP}{TP+FN}, \quad FPR = \frac{FP}{FP+TN}

* TPR = Recall = 0.8
* FPR = 2 / (2 + 8) = 0.2

**Formal Definition:**
ROC curve plots TPR vs FPR across thresholds.
AUC = probability model ranks a random positive higher than a random negative.

**Dog intuition:**
How well dog ranks “suspiciousness” before barking.

**Professional meaning:**
Model’s ability to separate fraud vs legitimate across thresholds.

**Key idea:**
👉 Ranking capability independent of threshold

---

# :sd 4. Compact Mental Summary (high retention)

* Precision → “When I say YES, am I correct?”
* Recall → “Did I miss anything important?”
* Accuracy → “How often am I right overall?”
* F1 → “Am I balanced?”
* ROC-AUC → “Can I rank properly?”

---

# :sd 5. Why each metric matters (critical insight)

No metric is “best”.
Each encodes a **different failure cost**.

---

## Case 1: Medical Diagnosis (Cancer Detection)

* Missing a patient (FN) is dangerous
  👉 prioritize **Recall**

Even if precision drops, it's acceptable.

---

## Case 2: Spam Detection

* False positives annoy users
  👉 prioritize **Precision**

Better to miss some spam than block real emails.

---

## Case 3: Fraud Detection (banking)

* Both FP (user inconvenience) and FN (money loss) matter
  👉 use **F1 Score**

---

## Case 4: Model Comparison / Research

* Want threshold-independent evaluation
  👉 use **ROC-AUC**

---

## Case 5: Balanced dataset (simple tasks)

👉 **Accuracy works fine**

---

# :sd 6. Final Conclusive Insight (this is interview gold)

Each performance metric is not just a number; it encodes a **philosophy of error tolerance**:

* Precision → cautious decision-making
* Recall → exhaustive detection
* F1 → equilibrium between caution and coverage
* ROC-AUC → intrinsic separability of classes
* Accuracy → general correctness (only when data is balanced)

👉 The choice of metric should always align with the **cost of mistakes in the real-world system**.

---

# :ol Final takeaway

👉 **Metrics are not formulas to memorize; they are lenses to evaluate different kinds of mistakes.**
