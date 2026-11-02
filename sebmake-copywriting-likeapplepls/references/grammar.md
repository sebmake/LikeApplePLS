# The grammar of the keynote register

Twelve rules, each with its count. **Corpus:** the official English transcripts (WebVTT) of 8 keynotes, March 2019 to September 2026 (6 593 sentences, 104 700 words), and the official French subtitles of the 4 most recent (2024 to 2026 : 3 008 sentences, 50 100 words). Rates are **per 100 sentences** unless stated; a rate is the **median across keynotes** (the range in parentheses shows the spread between the calmest and the most emphatic keynote). The exact values the checker uses are in `targets.json`. What is not measured is marked **convention**.

Two cautions. The corpus is **spoken**: it was written to be said on a stage, then subtitled. Written media take the same sentence and tighten it (`media.md`). And the corpus is a **launch register** for the general public: the dose of superlatives and “up to” is the loud end; other audiences take less (`publics.md` of the keynote skill).

## Contents

0. In brief
1. Short sentences, and one very short one every few
2. The landing fragment
3. You, not the user
4. Present tense
5. No exclamation, almost no question
6. Every figure with its base
7. One superlative, bound to yourself
8. No hedge, few intensifiers
9. The concrete word, never the category
10. “And” carries the thread; “just” carries the ease
11. The agent is named
12. The ask is a verb
13. What the corpus never does
14. What these rules don't say (conventions)
15. Limits of the corpus

---

## 0. In brief

| Rule | Measured | What to do |
|---|---|---|
| 1 | median 14.5 words per sentence; 23 % at 8 words or fewer; 18 % at 25 or more | split past 25; one short sentence in four |
| 2 | 8 % of sentences have 5 words or fewer and no verb | land an idea with a fragment: *[Noun].* *Done.* |
| 3 | *you* 3.5 per 100 words, *we* 2.3, *I* 1.2, *the user / customer* 0.1 | the reader is *you*; the company is *we* |
| 4 | *will* in 7 % of sentences; *can* in 15 % | present for what works; future for a date |
| 5 | exclamation marks on 2 % of sentences, questions on 2 % | none in print; one rhetorical question at most |
| 6 | 8 % of sentences carry a number; multipliers 0.2 %, percentages 0.9 %, *up to* 0.8 % | each with its base in the same sentence; *up to* with its condition |
| 7 | superlative adjectives in 16 % of sentences; *ever* 2 %, *yet* 0.5 %, *world's* 0.5 % | one per announcement, bound (*yet*, *ever*); absolute only with proof |
| 8 | *we think / believe* 0.6 %, *maybe / probably* 0.6 %, *very / really / truly* 2.5 % | state or cut; intensifiers rare |
| 9 | acronyms 0.4 per 100 words; triads in 12 % of sentences | the concrete noun; lists of three same-kind nouns |
| 10 | *And* opens 14 % of sentences, *So* 4 %, *Now* 3 %; *just* in 7 % | thread openers in a script, cut in print; *just* for the one-step how |
| 11 | passive voice in 4 % of sentences | the product or you does it |
| 12 | *Let's* 3.6 %, *Here's* 1.6 %, *Introducing* 0.9 %, *so you can* 1.4 % | the ask and the demo start with the verb; the benefit turn once per block |

---

## 1. Short sentences, and one very short one every few

**Measured.** Median 14.5 words per sentence (11 to 16 across keynotes); mean 16. 23 % of sentences have 8 words or fewer (19 to 38 %); 18 % have 25 or more (11 to 22 %). The 2020 product event, prerecorded and tight, is the short end (median 11, 38 % at ≤ 8); the live 2019 developer keynote is the long end.

**Rule.** Write to a median of 14. Split any sentence past 25 words: the corpus allows one in five, and those are lists of names or features, not arguments. Land each idea with a short sentence: one in four at 8 words or fewer.

**In French** the median rises to 14 to 17 (`french.md` § 1): cut words, not sense.

## 2. The landing fragment

**Measured.** 8 % of sentences (5 to 20 %) have 5 words or fewer and no finite verb: a name, a verdict word, a close (*That's it.* *Done.* *[Name].* *Back to you.*). They come right after a long sentence or a demo step.

**Rule.** After the sentence that explains, a fragment that lands. Never two fragments in a row (**convention**); never a fragment as the first unit of a text (the name alone is the exception: hero, slide).

## 3. You, not the user

**Measured.** Per 100 words: *you / your* 3.5 (1.3 to 5.0), *we / our* 2.3 (1.4 to 2.8), *I / my* 1.2 (0.2 to 1.9), *they / their* 0.6, *user(s) / customer(s)* 0.12 (0.06 to 0.23). The reader is addressed 30 times more often than named. *I* belongs to the presenter's verdict and to the handover (*Back to you*); the 2026 keynote drops it to 0.2.

**Rule.** The reader is *you*, from the first sentence. The company is *we* when it did something (*We redesigned…*), not as a subject of opinion (*We think…*, rule 8). *I* only in a signed message about the signer's own act. *The user*, *the customer*, *the client* never appear in text the reader sees: they belong to the spec.

## 4. Present tense

**Measured.** *will* (and *'ll*) in 7 % of sentences (3 to 12 %); *can* in 15 % (8 to 25 %); *going to* is rare. The future is reserved for availability (*will be available in the fall*) and for the demo's next move (*you'll see*).

**Rule.** What the product does is in the present: *Fern waters when your plants need it.* *You can* opens the ability (15 % of sentences: it is the corpus's second verb). The future only for a date or a release. In French, « vous pouvez » runs even higher (up to 10 % of sentences, `french.md`).

## 5. No exclamation, almost no question

**Measured.** Exclamation marks on 2 % of sentences (0 to 6 %; the high values are live-audience lines: *Who's fired up!*). Questions on 2 % (0.2 to 4 %), most of them rhetorical before a reveal (*What if…?*) or a demo (*Isn't that cool?*). On the slides themselves: 0 exclamation marks observed on title cards.

**Rule.** In print, no exclamation mark: the verdict carries the weight. One rhetorical question per text at most, and only to open a tension. A notification, a confirmation, a button never end with *!*.

## 6. Every figure with its base

**Measured.** 8 % of sentences carry a number (4 to 28 %; the hardware keynotes are the high end). Multipliers (*3× / 3 times*) 0.2 %, percentages 0.9 %, *up to* 0.8 % (0.1 to 5.9 %), *more than / over [N]* 0.8 %. In the corpus the base of a comparison is said in the same sentence or written in the on-screen label (keynote skill, A5), and the condition of an *up to* is on the final card or in the label.

**Rule.** One or two figures per announcement. A multiplier or a percentage names what it is compared to **in the same sentence**: *3 times faster than the first-generation sensor*. An *up to* carries its condition in the same sentence or the label, or becomes the typical value. A figure turns into life once (*That's enough to…*, `functions.md` § 5). No figure the brief did not give: `[TO PROVIDE]`.

## 7. One superlative, bound to yourself

**Measured.** Sentences with a superlative adjective (*incredible, amazing, beautiful, powerful, best, most…*): 16 % (14 to 27 %), the loudest device of the register. the bounds: *ever* 2.2 %, *than ever* 1.1 %, *yet* 0.4 %, *for the first time* 0.5 %; the absolutes: *world's* 0.5 %, *industry* 0.6 %.

**Rule.** The dose is the launch register for the general public; written media and other audiences take less (one per page, one per email, one per announcement in a deck; none for buyers and investors, `publics.md`). The form is bound to yourself: *our fastest yet*, *the best [X] we've ever made*, *for the first time*. An absolute (*the best on the market*, *the world's first*) needs its proof next to it, or goes. The adjective goes on the claim that earns it, never on a plain description (*our beautiful dashboard* → cut).

## 8. No hedge, few intensifiers

**Measured.** *we think / we believe / I think* 0.6 % of sentences (0 to 1.8 %); *maybe / probably / perhaps / kind of* 0.6 %; *very / really / truly* 2.5 % (1.1 to 5.6 %); *actually* 0.4 %.

**Rule.** A claim is stated or cut: *We believe it is probably the most advanced* becomes a fact with its base, or nothing. *Very* and *really* add nothing the noun and the figure don't: keep one per text, if any. In French, « vraiment / très » run at the same 2.5 %.

## 9. The concrete word, never the category

**Measured.** Acronyms 0.4 per 100 words (0.1 to 2.4; the developer keynotes are the high end, and each acronym is spelled out or known to the room). Triads (*A, B and C*) in 12 % of sentences (6 to 15 %): nouns of the same kind, same length. The corpus says the thing (*your photos*, *the battery*, *a message*) and leaves the category (*content*, *solution*, *experience*, *ecosystem*) to the competition.

**Rule.** Replace each category word with the concrete thing it hides: *solution* → what it does; *experience* → what the reader sees; *leverage* → use; *seamless* → say what doesn't happen (*no export, no copy*). One acronym per text, spelled out. Lists in threes (English) or twos (French, `french.md`), same form for each item.

## 10. “And” carries the thread; “just” carries the ease

**Measured.** Sentence openers: *And* 14 % (9 to 17 %), *So* 4 %, *Now* 3 %, *This* 4 %, *It / It's* 6 %, *We* 3 %, *You* 3 %, *With* 2 %, *But* 1 %. *just* appears in 7 % of sentences (3 to 9 %): *just tap*, *it just works*, *just one more thing* excluded from the count. *right from / right on* 1.1 %; *all in / all with* 0.6 %; *whether you're* 0.4 %; *not only* 0.3 %.

**Rule.** In a **script** or a voice-over, keep the thread openers: one sentence in seven starts with *And*. In **print**, cut them to one or two per text; a heading does the linking. *Just* is the word of the one-step how (*Just tap, and it's done.*): one per how-it-works. *Right from* names the place; *all in one place* wraps a list; *whether you're A or B* speaks to two readers in one sentence (`functions.md` § 4, § 13).

## 11. The agent is named

**Measured.** Passive voice (*is / are / was / been + participle*) in 4 % of sentences (3 to 5 %). When the corpus uses it, the agent is obvious (*built into every…*) or the subject is the product's part.

**Rule.** The product does it, or you do it. *Your order has been saved* → *Order saved.* (the product acted) or *You saved the order.* In French, the passive with « par nos services / par le système » is the administrative register: cut (`french.md` § 6).

## 12. The ask is a verb

**Measured.** *Let's* opens or appears in 3.6 % of sentences (1 to 6 %), *Here's* 1.6 %, *Take a look* 0.5 %, *Introducing* 0.9 %. The benefit turn *so you can* 1.4 % (0.6 to 3.0 %), *which means* 0.1 %. On screen (keynote skill, A19 to A21): the call to action is an imperative of 1 to 3 words, after the name and the price.

**Rule.** Every text ends with one ask, verb first, 1 to 4 words (*Order today*, *Open Fern*, *Reply to this email*). Never *Click here*, *Submit*, *OK*, *Validate*: the verb names the outcome. The demo starts with its verb (*Take a look*, *Tap*). The benefit turn (*so you can…*) follows a feature about once per block, not after every sentence.

---

## 13. What the corpus never does

| Device | Seen | Base |
|---|---|---|
| *the user* / *the customer* addressed to the reader | 0.11 per 100 words | 104 700 words |
| exclamation mark on a title card | 0 | the on-screen text of 8 keynotes |
| greeting formula (*Dear…*, *Hello everyone, I hope…*) as an opener | 0 | 8 openings: greeting + place, then the day's meaning |
| *excited / thrilled to announce* as the first sentence | 0 | 8 openings (the emotion comes after the name, as a verdict) |
| a comparison without its base said or written | 0 | the multipliers and percentages measured against their labels |
| a counted figure that the speaker did not give (*many*, *tons of*) as a proof | — | convention: every proof figure is a number |
| *please*, *kindly*, *do not hesitate* | 0 | 6 593 sentences |
| *click here*, *submit*, *OK* as an on-screen ask | 0 | the A19 to A21 screens |
| a sentence that quotes a competitor by name in a launch | 0 | product launches (comparisons are anonymous or against yourself) |
| a hedge on a claim (*we think it's probably*) | 0.6 % | and never on a figure |
| an all-caps word for emphasis | 0 | on-screen text (sentence case; weight comes from size) |
| an emoji | 0 | on-screen text |
| an ellipsis outside the suspended name | ≈ 0 | the only ellipsis is *…and we call it* |
| a superlative on a plain description (*our beautiful menu*) | rare | the adjective sits on the claim: the product, the chip, the camera |
| a feature with no turn to the reader in its block | rare | *so you can* and *you can* run once per block |

## 14. What these rules don't say (conventions)

- **Written media**: emails, interface strings, web pages, release notes are not in the corpus. `media.md` applies the register to them and says **convention** at each step.
- **Length of an email, of a button, of an error**: conventions in `media.md` § 9.
- **The move (name → verdict → proof → ask)**: read from the keynote run of show (keynote skill, `grammaire.md` § 4), applied to a text: convention.
- **Tu / vous, on / nous**: the French corpus is *vous* and *nous* on stage; *tu* and *on* in writing are the brand's choice, asked.
- **Other audiences** (buyers, investors, internal): the dose of superlatives, sources and *up to* follows `publics.md` of the keynote skill, which is itself a convention built on the general-public corpus.

## 15. Limits of the corpus

- The transcripts are **subtitles**: sentence boundaries follow the subtitler's punctuation; the live keynotes (2019) carry applause lines and asides that raise the counts of exclamations and fragments.
- **One brand, one genre**: a product launch for the general public, in American English. The French is a translation of it, not French written first.
- Rates are medians across 8 keynotes; a single keynote can sit far from the median (ranges given). Use the median as the target and the range as the tolerance.
- The measures are **lexical**: a regular expression counts *very* and *will*, not the idea. The checker catches the register; you judge the move.
