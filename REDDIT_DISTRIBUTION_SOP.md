# Reddit Distribution SOP

## Goal

Use Reddit and adjacent forums as a low-risk place to answer real developer
questions, learn what problems repeat, and maintain useful free resources.

This is not a Reddit -> GitHub -> Gumroad sales funnel. Do not optimize public
replies for monetization. Optimize for useful answers, clean moderation history,
and evidence about which problems are worth solving.

GitHub is the preferred free resource surface. Gumroad can exist downstream, but
it must not be used in subreddit replies or Reddit-linked landing pages unless a
specific community clearly allows it and the user explicitly approves that path.

## Default Behavior

When participating in Reddit or similar communities:

1. Answer the actual question first.
2. Give concrete steps that work without downloading anything.
3. Link at most one matching free resource only when it directly helps.
4. Use `FREE_RESOURCE_INDEX.md` to choose the resource and safe link line.
5. Do not mention paid products, Gumroad, discounts, or coupons in public replies.
6. Do not copy-paste the same reply across threads.
7. Stop immediately if a moderator warning, removal, or ban signal appears.

The working posture is: helpful answer first, optional free tool second.

If the user cannot manually review replies, do not publish public replies
automatically. Use `AUTO_HELP_POLICY.md`: draft, log, and improve owned resources
instead.

## Participation Tiers

### Tier 0: Do Not Touch

Do not post, comment, vote-brigade, or use another account in:

- Any subreddit where the account is currently banned.
- Any thread removed for self-promotion unless the user explicitly asks for a
  moderation-safe review.
- Any community where rules disallow the resource type being discussed.

### Tier 1: Answer Only

Use this for most communities.

Allowed:

- Direct answers.
- Checklists written inline.
- Clarifying questions.
- One free GitHub link only if it is directly relevant.

Not allowed:

- Paid links.
- Coupon codes.
- Multiple resource links.
- Repeated promotional phrasing.
- Replies whose main purpose is to place a link.

### Tier 2: Free Resource Link

Use only when the user question directly matches a resource in
`FREE_RESOURCE_INDEX.md`.

The reply must still be useful if the link is removed.

Safe structure:

1. Short direct answer.
2. Two to five concrete steps.
3. One sentence with one free GitHub link.
4. No paid CTA.

### Tier 3: New Resource Post

Use only after explicit user approval.

Before drafting:

1. Read the target community rules.
2. Pull 5-10 recent successful benchmark posts from that community.
3. Confirm the resource type is allowed.
4. Confirm the landing page is free-only.
5. Confirm there is no Gumroad, discount, paid upgrade, or Pro Preview CTA on
   the directly linked page.
6. Draft in the target community's normal style, not as a sales post.

## Resource Matching

Use `FREE_RESOURCE_INDEX.md` for common scenarios:

- Asset/source provenance before shipping.
- Font source-chain and mirror risk.
- Game-safe font/source starter rows.
- Pre-shipping asset-license traps.
- Actual free UI SFX in asset-specific communities.

If no resource matches, do not force a link. Answer the question only.

## Information Product Quality Gate

Information packs must be real audited material, not filler.

Minimum standard before linking or publishing:

- Verified rows have a direct source URL.
- Verified rows have a license evidence URL or exact evidence note.
- Verified rows have `last_checked`.
- Discovery rows are clearly marked and do not count toward the public verified
  claim.
- Public titles and claims match verified rows only.
- Practical columns exist where relevant: commercial use, attribution,
  redistribution risk, download friction, best use case, and risk notes.
- A README explains audit method, limitations, and what the pack is not.
- CSV is included when tabular data is central; Markdown/XLSX can be added when
  useful.
- Local consistency checks pass before release.

Do not publish or link a source directory that is mostly generic links,
unverified search results, or copied directory tags without page-level checks.

Use `INFO_PACK_BENCHMARK_PLUS_ONE.md` when upgrading a free information pack.

## Landing Page Rules

Every page linked directly from a subreddit must be free-only.

This includes:

- GitHub Release notes.
- Package README files.
- Repo README if it is the linked page.
- Any itch.io, Gumroad, or personal page used as the direct link.

Do not put these on direct subreddit landing pages:

- Gumroad links.
- Paid product CTAs.
- Launch discounts.
- Coupon codes.
- Pro Preview sections.
- "Upgrade" language.
- Email gates unless the community clearly allows them and the user approves.

## Subreddit Notes

### r/gamedev

Status as of 2026-06-05: do not post or comment in `r/gamedev`.

The account received a 7-day subreddit ban after moderators said there had been
multiple self-promotion warnings and that sneaking paid products into a free
resource is not allowed. Do not use another account to bypass the ban. Do not
repost removed resources, appeal aggressively, or automatically resume after the
ban expires.

Any future `r/gamedev` use requires:

1. Explicit user approval.
2. Fresh rule review.
3. No paid link or paid-adjacent landing page.
4. Answer-first participation, not resource-post funneling.

### r/gameassets

Use only for actual free game asset submissions.

Allowed when relevant:

- Original downloadable assets.
- Clear license notes.
- No-email GitHub or release download.
- Preview images or audio samples.

Not appropriate:

- Templates.
- Checklists.
- Questions or polls.
- Tutorials without an asset download.
- Paid links.
- Temporary freebies.
- Crypto, NFT, or generative-AI-related content.

## Reply Template

Use this shape when a link is justified:

```text
Short version: [direct answer].

I would:
- [step 1]
- [step 2]
- [step 3]

I also keep a free [resource type] for this exact workflow here: [GitHub link]
```

Use this shape when no link is needed:

```text
Short version: [direct answer].

The main thing I would check is [specific risk]. Record [source/evidence/recheck
detail] so you are not relying on memory at release time.
```

For legal/license-sensitive answers:

```text
Not legal advice, but I would not rely on [weak signal]. I would look for
[stronger evidence], record the source URL and license evidence, and replace it
if the source chain is unclear.
```

## Hard Rules

- Respect subreddit bans and cooldowns.
- Do not use another account to bypass a subreddit ban.
- Treat a moderator warning as a hard stop for that community path.
- Answer before linking.
- Link at most one matching free resource.
- Skip the link if the answer stands alone.
- Do not direct-link Gumroad first on Reddit.
- Do not mention paid products in public subreddit replies.
- Do not use Gumroad as a direct download surface for communities requiring no
  email or registration.
- Do not post a resource before quality/audit status is clear.
- For Gumroad products, cover and thumbnail are mandatory before publication,
  but Gumroad publication is separate from Reddit distribution.

## Tracking

Track participation only when it informs future decisions:

- community/platform
- question topic
- whether a link was included
- which free resource was linked
- reply score/reactions
- follow-up questions
- GitHub release downloads after the reply
- moderator warnings, removals, or bans

Success metric:

A good day is useful answers with zero moderation issues. Downloads and
follow-up questions are secondary signals. Revenue is not a public Reddit
participation metric.

## Related Files

- `FREE_RESOURCE_INDEX.md`: maps question types to safe free resources.
- `REPLY_DRAFTS.md`: reusable answer patterns.
- `ANSWER_LOG.md`: candidate/reply tracking.
- `AUTO_HELP_POLICY.md`: rules for unattended automation.
