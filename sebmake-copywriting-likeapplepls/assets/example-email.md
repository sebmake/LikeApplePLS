# Example: an email, before and after

Fictional product: **Fern**, an app that waters house plants on a schedule. Every figure below is fictional and was given in the brief. This shows the level of detail expected at delivery (SKILL.md, step 5).

## Before (as received)

> **Subject:** Important update regarding your Fern account!
>
> Dear valued customer,
>
> We are thrilled to announce that our innovative new watering solution has been designed to leverage smart sensors in order to optimize your plant care experience. We believe it is probably the most advanced system on the market! Users will be able to seamlessly monitor soil humidity, which is 3x more accurate, with up to 40% water savings.
>
> The new dashboard has been completely redesigned by our team and will be rolled out to all users over the coming weeks. Please do not hesitate to contact our support team should you have any questions whatsoever.
>
> Best regards,
> The Fern Team

`check_copy.py --medium email`: 12 gaps (L2, T1, T2, T4, C1, C2, C3 ×2, C4, C5, W1, U3), 1 note.

## After

> **Subject:** Fern now reads the soil, not the calendar.
>
> Starting today, Fern waters when your plants need it.
>
> A sensor in the pot measures soil humidity every hour. It reads 3 times more precisely than the first-generation sensor, so Fern waters less often and never too late. In our tests on 200 pots over 3 months, that saved up to 40 % of water, with pots left in direct sunlight.
>
> The new dashboard shows every plant on one screen: humidity, next watering, water used this month.
>
> It reaches your app over the next two weeks. Nothing to do on your side.
>
> **Open Fern**
>
> Questions? Reply to this email. A person answers.
>
> Léa, Fern

`check_copy.py --medium email`: 0 gaps, 1 note (B1: the script looks for “so you can” and misses the turn “so Fern waters less often and never too late”; the turn is there).

## What changed and why

| Before → after | Rule (count) |
|---|---|
| “Important update regarding your Fern account!” → “Fern now reads the soil, not the calendar.” | subject = the verdict, no exclamation (`media.md` § 4; exclamations 2 % of transcript sentences, rule 5) |
| “Dear valued customer, We are thrilled to announce…” → “Starting today, Fern waters when your plants need it.” | the opening line is the news; “thrilled / excited to announce”: 0 in the corpus as an opener (rule 10) |
| “innovative new watering solution … leverage smart sensors … optimize your plant care experience” → “A sensor in the pot measures soil humidity every hour.” | jargon replaced by the concrete thing (rule 9); 41 → 9 words (rule 1: median 14, 13 % at 25+) |
| “We believe it is probably the most advanced system on the market!” → cut | hedge + absolute superlative without proof + exclamation (rules 5, 7, 8); nothing in the brief backs “most advanced” |
| “Users will be able to seamlessly monitor” → “Fern waters … you” | “the user” → “you” (rule 3: you 3.5 / users 0.1 per 100 words); future → present (rule 4) |
| “3x more accurate” → “3 times more precisely than the first-generation sensor” | base in the same sentence (rule 6) |
| “up to 40% water savings” → “up to 40 % of water, with pots left in direct sunlight” | condition with the “up to” (rule 6); the condition came from the brief |
| “has been completely redesigned by our team and will be rolled out” → “shows every plant on one screen … It reaches your app over the next two weeks.” | passive → agent; future kept only for the date (rules 4, 11) |
| “Please do not hesitate to contact our support team should you have any questions whatsoever.” → “Questions? Reply to this email. A person answers.” | formula → the help itself (`media.md` § 4); one short landing sentence (rule 2) |
| “Best regards, The Fern Team” → “Léa, Fern” | a person signs (`media.md` § 4, convention) |
| — → “**Open Fern**” | one ask, verb first (rule 12) |

**To validate:** the subject line and the opening sentence are proposals (the brief gave no verdict).
**To provide:** nothing; the test figures (200 pots, 3 months, direct sunlight) came from the brief.
**Register:** English, casual; general public; email conventions from `media.md` § 4.
