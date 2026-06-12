# DeepSeek Reply Review

Use this as the final review gate for answer-first reply drafts.

Roles:

Run two separate passes:

1. Strict, nitpicky ordinary Reddit user.
2. Moderator-adjacent rules and self-promotion risk reviewer.

Primary standard:

The reply must be genuinely useful before it is safe. A safe but generic reply
does not pass.

## Review Criteria

DeepSeek should check:

1. Does the reply directly answer the original question?
2. Does it give concrete steps the poster can use immediately?
3. Is it adapted to the thread, not a reusable template pasted in?
4. If the link is removed, does the reply still have clear standalone value?
5. Is the link a minor supplement rather than the core of the reply?
6. Does the tone fit the subreddit: human, concise, non-corporate, and not like
   support-script text?
7. Does it contain or imply promotion, funneling, self-serving language,
   AI-template tone, paid/Gumroad/coupon/discount/Pro/upgrade/sales language, or
   likely self-promotion risk?

## Pass Gates

All must pass before a draft can be recommended:

- usefulness score >= 8
- subreddit tone score >= 7
- promotion risk score <= 3
- link dependency is `None` or `Minor`
- link decision is `keep`, `remove`, or `no_link_present`
- if DeepSeek says `remove`, remove the link before presenting the draft
- no banned words or paid CTA language
- no public posting without user approval

If a draft fails, revise and review again. The default fix order is:

1. Improve concrete usefulness.
2. Adapt more tightly to the original question.
3. Remove self-reference and optional links.
4. Re-run the strict review.

Keep iterating until the draft passes. If the only passing version would be too
generic or not useful, do not recommend a reply.

## Prompt

```text
You review Reddit replies in two separate passes.

First pass: strict, nitpicky ordinary Reddit user.
Second pass: moderator-adjacent rules and self-promotion risk reviewer.

Your most important question:
Is this reply genuinely useful to the original poster?

If the link is removed, the reply must still solve part of the problem.

Review the Reddit reply draft below.

Review in two passes.

Pass 1, ordinary Reddit user:
1. Does it directly answer the original question?
2. Does it give concrete, actionable steps?
3. Is it adapted to this exact thread instead of sounding like a generic template?
4. Does the tone fit the subreddit: human, concise, non-corporate, and not like support-script text?

Pass 2, moderator-adjacent risk:
5. Does the reply remain useful if every link is removed?
6. Are any links minor supplements rather than the core value?
7. Does it contain or imply promotion, funneling, self-serving language, AI-template tone, paid/Gumroad/coupon/discount/Pro/upgrade/sales language, or likely self-promotion risk?

Return strict JSON only:
{
  "usefulness_score": 0-10,
  "subreddit_tone_score": 0-10,
  "promotion_risk_score": 0-10,
  "recommendation": "Yes" | "No" | "Revise",
  "link_dependency": "None" | "Minor" | "High",
  "largest_usefulness_problem": "...",
  "largest_tone_problem": "...",
  "largest_promotion_or_rules_risk": "...",
  "sentence_to_delete_first": "...",
  "link_decision": "keep" | "remove" | "no_link_present",
  "revision_brief": "..."
}

Original thread:
[thread summary]

Draft reply:
[draft]
```
