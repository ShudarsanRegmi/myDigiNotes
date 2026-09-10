<img width="800" height="885" alt="image" src="https://github.com/user-attachments/assets/c4c738fa-8a8f-4d4b-885a-c5597ab4801b" />

## Ans

Before solving this problems, let's think about what actually happens after an IPO allotment is done.

60 lakh people applied.
Only 7.5 lakh got shares.

For everyone else, the money that was blocked in their bank account now needs to be released. For the people who got shares, the right amount needs to be debited.

And all of this is happening across 40+ banks that you do not control.

If I were designing this, I would think about it in 4 simple parts.

[1] First, separate allotment from money movement

The allotment result should be final before we start touching bank accounts.

For every application, I would store a clear state:
→ allotted
→ not allotted
→ debit pending
→ unblock pending
→ completed

Once that state is safely stored, the settlement process can run independently.

This matters because you do not want the IPO allocation logic sitting there waiting for SBI, HDFC, ICICI, or any other bank to respond.

Btw, if you're preparing for Senior to Principal-level system design interviews, I've put together 90+ fundamentals like this into a guide.

You can check it out here: puneetpatwari.in

[2] Give every bank its own lane

This is probably the most important design decision. I would not put all 60 lakh applications into one giant processing line.

I would split them by bank.

So conceptually:
→ HDFC applications go into one queue
→ SBI applications go into another
→ ICICI applications go into another

Now if SBI is slow, SBI's queue gets longer.
HDFC and ICICI keep processing.

Think of it like 40 toll booths instead of one toll booth for the entire highway.

[3] Retries must never move money twice

Now imagine we send: "Debit ₹15,000"

The bank processes it, but our request times out before we get the response.

Did the money move?
Maybe.

So blindly retrying is dangerous. Every debit or unblock request needs a unique idempotency key tied to that application.

If the same request is sent again, the bank integration should understand: "I've already processed this exact instruction."

Same request can arrive 5 times.
Money should still move once.

That one rule is what stops timeout handling from becoming a duplicate debit incident.

[4] Slow banks become delayed work. 

If one bank starts timing out, I would not keep hammering it every second.

I would:
→ retry with increasing delays
→ keep those applications marked pending
→ alert if the backlog gets too old
→ continue processing every other bank
→ reconcile later with the slow bank

Reconciliation is the boring part that saves you.

At the end, compare: "What did our system ask the bank to do?"

with: "What does the bank say actually happened?"

Anything that does not match goes into a repair or manual review flow. That is how I would think about this from first principles.
