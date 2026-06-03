# AI Operations Level Model

This document adapts the five-level AI usage model into an operating system for
the Reddit -> GitHub -> Gumroad export project.

The goal is not to "use AI more." The goal is to use AI at the highest level that
is still observable, reversible, and tied to the first cash transaction.

## North Star

Get one real cash transaction within 30 days.

Primary path:

Reddit attention -> GitHub free download -> trusted information product -> Gumroad
paid workflow pack.

Current paid product:

- Gumroad: `Game Asset Audit Template Pack for Indie Developers`
- URL: https://3813941972097.gumroad.com/l/isavr
- Price: USD 9
- Offer code: `REDDIT40`, 40% off, first 10 uses

## Level 1: AI As Search

Use AI to find ideas, subreddits, competitor posts, pain points, and possible
product angles.

Allowed:

- Search for benchmark posts.
- Summarize subreddit rules.
- Collect possible product ideas.
- Find pain-point language from comments and posts.

Not enough for publishing:

- Do not build or post from Level 1 research alone.
- Do not trust broad "blue ocean" claims without real post/comment/download
  evidence.

Output:

- Candidate ideas only.

## Level 2: AI As Material Processor

Use AI to turn raw material into structured working files.

Inputs:

- Reddit comments.
- Benchmark post titles and bodies.
- GitHub release metrics.
- Gumroad product fields.
- Source URLs for information packs.

Allowed:

- Convert raw comments into pain-point notes.
- Turn benchmark posts into title/body templates.
- Convert source URLs into CSV/XLSX draft rows.
- Draft Gumroad page copy from existing product files.

Not enough for publishing:

- Any generated rows are drafts until audited.
- Any marketing copy is draft until it matches real product contents.

Output:

- Draft rows, draft copy, draft release notes, draft Reddit posts.

## Level 3: AI With Quality Gates

Use AI and scripts to check whether a product, post, or CTA is truthful and safe
enough to publish.

Required gates for information packs:

- Verified row count matches public claim.
- Every verified row has source URL.
- Every verified row has evidence URL or exact evidence note.
- Every verified row has `last_checked`.
- Discovery rows are not counted in title claims.
- Risk notes are not blank.
- Audit report passes.

Required gates for Reddit/Gumroad copy:

- No hard legal-safety claims.
- No "guaranteed commercial use" language.
- No direct paid-first Reddit link unless subreddit rules clearly allow it.
- Product page matches the actual uploaded ZIP.
- Cover/thumbnail exist for Gumroad products.

Current examples:

- `game-font-license-pack-v0.2.0` passed with 47 verified rows and 0 discovery
  rows counted.
- `$19` service idea is blocked for now because Gumroad service/commission
  products are disabled until account age reaches 30 days.

Output:

- `publish_ready`, `conditional_pass`, `technical_pass_only`, or `blocked`.

## Level 4: AI In A Repeatable Workflow

This is the current operating baseline.

The project should run through the same loop instead of improvising:

1. Collect metrics.
2. Read comments and benchmark signals.
3. Judge whether cash path is closer.
4. Choose one action:
   - observe
   - strengthen CTA
   - update release notes
   - reply to a relevant comment
   - build an adjacent audited information pack
   - improve Gumroad page
   - stop a weak branch
5. Save the decision to memory.

Daily metric checklist:

- Reddit score, upvote ratio, comments, removed status.
- GitHub stars, forks, watchers.
- GitHub release ZIP downloads.
- Gumroad sales, revenue, product status.
- `REDDIT40` offer-code usage.

Current active watch items:

- `1tnz9hk`: original asset audit sheet.
- `1ttesqj`: font license starter pack.
- `1ttc3tr`: UI SFX side experiment.
- `1tssd1i`: workflow kit post.
- `game-font-license-pack-v0.2.0`: main free trust-builder.
- `Game Asset Audit Template Pack for Indie Developers`: main paid product.

Output:

- One decision per cycle, backed by data.

## Level 5: AI Runs Low-Risk Operations

Level 5 is allowed only for low-risk, observable, reversible work.

Allowed autonomous actions:

- Collect Reddit/GitHub/Gumroad metrics.
- Check offer-code usage.
- Update local memory.
- Draft posts, comments, product copy, and release notes.
- Update low-risk GitHub README or Release notes when the change only clarifies
  an existing public offer.
- Create local audit reports.
- Run local consistency scripts.

Requires extra caution:

- Posting new Reddit threads.
- Commenting repeatedly on Reddit.
- Publishing new Gumroad products.
- Changing price.
- Creating paid offers.
- Replacing Gumroad files.

Blocked without a clear reason:

- Any action that bypasses platform restrictions.
- Any claim that legal use is guaranteed.
- Any paid service workaround while Gumroad service products are disabled.
- Any post that exists only to bump visibility.

Human-level decisions remain:

- Whether to pivot the whole business lane.
- Whether to increase price.
- Whether to post in a new subreddit with unclear rules.
- Whether to accept legal/identity/payment risk.

## Current Level Assessment

The project is at Level 4 with limited Level 5 automation.

Evidence:

- Metrics are collected via CLI.
- Products are built with scripts.
- Information packs have audit gates.
- GitHub Release notes and README can be updated safely.
- Gumroad CLI is connected.
- Daily heartbeat monitors the funnel.

Gap to stronger Level 5:

- Need a compact metrics log.
- Need explicit action thresholds.
- Need safer Reddit posting cadence rules.
- Need a product backlog ranked by cash-transaction likelihood.

## Action Thresholds

Use these thresholds for the next decision:

### Strengthen CTA

Do this when:

- Free release downloads increase, but Gumroad sales remain 0.
- `REDDIT40` times_used stays 0.
- Reddit post scores rise but comments do not ask for a new product.

Safe actions:

- Improve README paid section.
- Improve GitHub Release notes.
- Improve Gumroad summary/description.
- Add one clearer Gumroad link downstream.

### Build Adjacent Information Pack

Do this when:

- A comment names a concrete pain.
- A free pack gets downloads or upvotes but no paid conversion.
- The adjacent pack can connect directly to the paid workflow pack.

Good candidates:

- SFX licensing/source tracker.
- UI/HUD source tracker.
- "7 asset license traps before shipping" checklist.
- Attribution text generator/checklist.

### Avoid Action

Do nothing when:

- No new downloads.
- No new comments.
- No offer-code usage.
- No removal/risk event.

Silence is better than weak posting.

### Escalate To User

Notify when:

- A sale happens.
- A Reddit post is removed or locked.
- A buyer asks a question.
- A strong comment reveals a new product pain.
- Gumroad offer code is used.
- A platform restriction blocks the intended path.

## Operating Principle

AI can run the machine, but the machine must have brakes.

For this project, that means:

- Free-first on Reddit.
- GitHub-first for downloads.
- Gumroad downstream for paid workflow.
- Evidence before claims.
- Audit before promotion.
- Low-frequency, high-signal Reddit actions.
- Cash goal over vanity metrics.
