# Reddit Distribution SOP

## Goal

Drive attention, downloads, comments, and eventually the first cash transaction through a Reddit -> GitHub -> Gumroad funnel.

Reddit is the trust and feedback surface. GitHub is the direct free download surface. Gumroad is downstream monetization.

The core product direction is curated information, not raw assets. The user's durable positioning is a materials curator / audit-sheet maker: source lists, checklists, trackers, templates, and reviewed directories. Audio or visual asset packs are traffic side experiments only when they help enter a subreddit or build trust.

## Default Rule

Before drafting or publishing a new Reddit post, analyze and imitate benchmark accounts/posts in the target subreddit.

Do not write from scratch based only on internal taste.

Default priority:

1. Build and improve information products that reduce research/audit time for indie developers.
2. Use free information resources on Reddit as the main attention engine.
3. Use actual game asset packs only as a secondary subreddit-entry tactic.
4. Keep the paid Gumroad product tied to curated information: Pro sheets, templates, trackers, and done-for-you audits.

## Benchmark-First Checklist

For every new Reddit post:

1. Pull 5-10 recent or top benchmark posts from the target subreddit.
2. Record for each benchmark:
   - title formula
   - score
   - comments
   - flair
   - media type: text, gallery, video, link
   - value promise
   - license wording
   - CTA style
   - whether the post links to GitHub, itch.io, Gumroad, or a personal site
3. Copy the successful packaging pattern, not the content.
4. Keep the Reddit post free-first and rule-compliant.
5. Put paid links downstream in GitHub/profile unless the subreddit clearly allows direct paid promotion.

## Current Benchmark Patterns

### Core Information Product Lane

This is the primary business lane.

Use this lane for:

- commercial-use source directories
- CC0/no-attribution filtered lists
- font/license checklists
- attribution trackers
- provenance logs
- shipping-risk checklists
- starter audit templates
- workflow kits

The working formula:

- exact count in the title, such as `50 sources`, `7 traps`, `4 templates`, or `100 rows`
- clear pain: asset licensing, attribution, font embedding, provenance, shipping risk
- free GitHub-first download
- visible audit method and limitations
- one specific feedback question
- downstream Gumroad CTA only in README/profile/product page

This lane should get most build time because it maps directly to the paid $9 template pack and future Pro sheets/services.

### Information Quality Gate

Information packs must be real audited material, not filler.

Minimum standard before publishing:

- Every verified row has a direct source URL.
- Every verified row has a license evidence URL or exact evidence note.
- Every verified row has `last_checked`.
- Discovery rows are clearly marked as discovery only and do not count toward the verified-row promise in the title.
- Claims in the Reddit title must match verified rows only. Example: do not say `50 verified font sources` if the file contains 35 verified rows plus 15 discovery rows.
- Include practical columns, not just names and links: commercial use, attribution, redistribution risk, download friction, best use case, and risk notes.
- Include a README explaining audit method, limitations, and what the pack is not.
- Include a machine-readable CSV and a human-readable Markdown/XLSX version when practical.
- Run a local consistency audit before release: required columns present, URLs non-empty, no duplicate URLs, no blank risk notes, verified-count matches title.

Do not publish a source directory if it is mostly generic links, unverified search results, or copied directory tags without page-level checks.

Use `INFO_PACK_BENCHMARK_PLUS_ONE.md` before upgrading a free information pack or making a paid Gumroad version. The standard is to copy benchmark packaging while beating benchmarks on verification, row-level evidence, risk fields, and practical workflow value.

### r/gameassets

Use this subreddit only for actual free game asset submissions.

The working formula from benchmark posts:

- Title includes: `[Free]`, asset type, exact count, format, sizes, commercial-use, no-attribution.
- Use gallery or strong preview images when possible.
- Body includes:
  - short use case
  - contents
  - license short version
  - creation/provenance method
  - download link with no email or signup
  - feedback question

Do not post templates, questions, polls, tutorials without download, paid links, temporary freebies, crypto, NFT, or generative-AI-related content.

### r/gamedev

Use this subreddit for resource posts, process posts, feedback requests, postmortems, and workflow/tooling discussions.

The working formula from benchmark posts:

- Lead with credible effort or concrete learning: "I spent X time curating/building..." or "I made X after feedback..."
- Explain the pain clearly before the link.
- Give a useful free resource.
- Include exact contents and limitations.
- Ask one specific feedback question.
- Avoid a hard Gumroad pitch.

## Title Template

Prefer titles that include:

- `free`
- exact artifact type
- exact contents or count
- target use case
- license/friction promise when relevant

Examples:

- `I made a free game-jam asset license workflow kit: CC0 starter sources, attribution tracker, font checklist, provenance log`
- `[Free] [2D] 20 transparent PNG UI icons | 3 sizes | commercial-use | no attribution`
- `I turned feedback on my asset audit sheet into a free game-jam workflow kit`

## Body Template

Use this structure:

1. Context: why the post exists.
2. Concrete contents.
3. Download link, preferably GitHub Release for no-email access.
4. License/provenance notes.
5. What it is not.
6. One specific feedback question.

## Hard Rules

- Do not direct-link Gumroad first on Reddit.
- Do not mention paid products unless clearly allowed and naturally relevant.
- Do not use Gumroad as the direct download surface for subreddits requiring no email or registration.
- Do not post a product before quality/audit status is clear.
- For Gumroad products, cover and thumbnail are mandatory before considering the publish complete.

## Current Follow-Up

Track these active posts:

- `1tnz9hk`: first r/gamedev asset audit sheet.
- `1tssd1i`: benchmark-style r/gamedev workflow kit post.
- `1ttc3tr`: r/gameassets UI SFX side experiment.

Measure:

- Reddit score, upvote ratio, comments, removed status.
- GitHub release downloads.
- GitHub views/clones.
- Gumroad product views/sales when available.
