---
name: sebmake-copywriting-likeapplepls
description: "Rewrites any text the way Apple keynotes speak (or reviews one against that register): emails, slide text, interface strings (buttons, labels, errors, empty states), web pages, release notes, scripts and voice-overs, in French or English. Rules measured on the official transcripts of 8 keynotes (2019-2026): sentence length, 'you' over 'the user', present tense, one bound superlative, every figure with its base, verb-first asks, no jargon, no hedges. Returns the rewritten text plus a table of what changed and why, each change tied to a measured rule, and keeps every fact, figure and name as given. Use it whenever someone wants text that sounds like Apple or like a keynote, wants copy rewritten, tightened, punchier or clearer, asks to review wording, microcopy, UX writing, an email, a landing page, a slide or a product description, or asks how Apple would say something, even without the word Apple. Not for building a deck (sebmake-keynote-likeapple-pls) or a film."
---

# Writing the way keynotes speak

This skill does two things:

1. **rewrite** a text in the keynote register, for the medium it lives in (email, slide, interface, page, notes, script), and show what changed and why;
2. **review** a text without rewriting it: its gaps against the register, each tied to a rule and its count.

The rules come from the official transcripts of 8 keynotes (2019 to 2026, 6 593 sentences in English, 3 008 in French) and from the on-screen text of their slides. Each rule carries its count (“N out of M”, or a rate per 100 sentences); what is not measured is marked **convention**. The skill takes the **grammar**, never the **brand**: no sentence from a keynote, no slogan, no signature phrase, no product name, no Apple font or logo. The words, names, figures and voice are the user's.

```bash
SKILL="<folder of this SKILL.md>"   # often ~/.claude/skills/sebmake-copywriting-likeapplepls
```

Requirements: Python 3.9 or later, standard library only. Nothing to install.

## Step 1 — Intake

Reread the request and the text. Don't ask again for anything already said; a short text with an obvious medium needs no question at all.

Ask the missing questions with the AskUserQuestion tool if it exists, otherwise in plain text, in a single message. **At most 4 questions per call**, 4 choices at most per question (plus “Other”).

| Question | Choices | Why |
|---|---|---|
| What is this text? | an email; slide text (or a deck's titles); interface strings; a web page or product description (script, release notes, social post: in “Other”) | Each medium has its lengths and forms (`media.md`). |
| Who reads it? | customers, general public; business clients (decision makers, buyers); the internal team; investors or partners | Sets the dose of superlatives, sources and “up to” (`publics.md` of the keynote skill, § 3). |
| Language and register | French, vous; French, tu; English, casual; English, formal | Never guess tu / vous: it's the brand's choice (`french.md` § 3). |
| What must not change? | names, figures and dates (default); also the legal and contractual wording; also the product's own terms (give them); nothing is fixed, rewrite freely | The skill never invents a checkable fact; it needs to know which words are terms. |

When the text comes from an interface, ask for **the width of the component** if a string must fit a button or a label, and for **the existing glossary** (one word for one thing). When it comes from a deck, ask whether the slide text and the speaker notes both need rewriting.

**What the skill never asks for**: a figure, a price, a date or a client's name that the text lacks. It leaves `[TO PROVIDE: label]` (`[À FOURNIR : libellé]` in French) and says so at delivery.

## Step 2 — Read the register, then measure the text

Read `references/grammar.md` once per conversation: the twelve rules and their counts. Then the medium's section in `references/media.md`, and `references/french.md` if the text is in French.

Measure the text before touching it:

```bash
python3 "$SKILL/scripts/check_copy.py" text.md --lang fr --medium email
python3 "$SKILL/scripts/check_copy.py" strings.txt --lang en --medium ui      # one string per line
python3 "$SKILL/scripts/check_copy.py" slides.txt --medium slide               # one screen per line
```

Media: `prose` (default), `email`, `slide`, `ui`, `web`, `notes`. The report lists **gaps** (a rule broken, with the fix) and **notes** (worth a look, not a fault). Exit code 1 means gaps. `--json` for the raw measures.

The script measures what can be counted: sentence length, who speaks and who is spoken to, tense and voice, superlatives and their proof, figures and their base, hedges, jargon, formulas, verb-first asks. **It does not judge the idea**: a text can pass the script and still say nothing. You judge the move (name, verdict, proof, ask: `media.md` § 1) yourself.

## Step 3 — Rewrite

Work unit by unit (sentence, string, screen), in this order:

1. **Find the move.** What is the name, the verdict, the proof, the ask? What is missing? A text without a verdict gets one, marked **TO VALIDATE** in the delivery (it's a proposal, not a fact). A text without a proof keeps its place: `[TO PROVIDE: the figure or the feature that proves it]`.
2. **Cut what the corpus never says**: the greeting and closing formulas, “we are excited to announce”, the hedge (“we think”, “probably”), the intensifier (“very”, “really”), the jargon (“solution”, “leverage”, “seamless”, “optimize”), the passive without an agent, the future for what already works, “the user” for the reader, “click here”, “please”, the exclamation mark.
3. **Shorten to the corpus lengths** (`grammar.md` § 1): split any sentence past 25 words; land each idea with a short sentence; on a slide, 10 words per screen; on a button, the verb and its object.
4. **Turn toward the reader**: *you* for the reader, *we* for what the company did, present tense for what the product does. Each feature gets its benefit turn (“so you can…”, « vous pouvez donc… ») about once per block, not after every sentence.
5. **Bound the claims**: one superlative per announcement, relative to yourself (“our fastest yet”) unless the proof is cited; every multiplier and percentage with its base in the same sentence; every “up to” with its condition.
6. **Pick the shapes** in `references/functions.md` for the moves that remain (announce, verdict, figure, how it works, price, ask, recap, close), fill them with the user's words, and vary from one block to the next.
7. **Keep the terms stable**: one word for one thing across the whole text and across the set of strings. Build the glossary as you go (the product's terms given at intake win over yours).
8. **Recount** after the rewrite, in the target language (French runs 15 to 20 % longer): run the script again on the result. Zero gaps before delivery; a gap you keep on purpose is said at delivery with its reason.

What you never do: add a figure, a date, a price, a name, a quote or a feature the text didn't have; translate a term the brand keeps in the other language; change a legal or contractual sentence (you flag it instead); reuse a sentence from a keynote, even translated; name the brand the register comes from inside the user's text.

## Step 4 — Review (when asked for a review, not a rewrite)

Run the script, read the text as its reader, then give:

1. the **verdict in one line**: what the text does well, what it fails at (the move or the register);
2. the **gaps**, one line each: the sentence, the rule (`grammar.md` number and its count), the fix — rewritten sentence included when it's one sentence;
3. the **notes** worth a look;
4. **what the script can't see**: a missing verdict, a feature without its benefit, a claim without its proof, a term that changes name halfway.

No score out of ten: the corpus gives counts, not grades. Say “within the register” or “outside it”, and on which rules.

## Step 5 — Delivery

A short message:

1. **the rewritten text**, in the medium's form (a string per line for an interface, subject then body for an email, one screen per line for slides, with speaker notes under each if asked);
2. **the table of changes**: *before → after · rule (number, count)*, one line per change that matters; small cuts grouped in one line (“12 intensifiers and 4 hedges cut, rule 8”);
3. **to validate**: every sentence you proposed that states something the source didn't (a verdict, a benefit), one per line;
4. **to provide**: every `[TO PROVIDE]`, with what it must contain;
5. one line on the register chosen (language, tu/vous, audience) and the conventions taken (a medium outside the corpus is a convention: say it);
6. the glossary, when the text is a set of strings or a page (one word for one thing).

The files, when the user works in files: the rewritten text next to the original (`name.rewritten.md`), the script's report (`name.check.md`).

## Reminders

- **The rules are measured.** Quote a count only from `grammar.md` or `targets.json`; what isn't there is a convention, said as such.
- **Nothing checkable is invented**: figure, price, date, name, quote, testimonial, feature. `[TO PROVIDE]` is the honest answer.
- **The grammar, never the brand**: no sentence from a keynote, no slogan, no signature phrase, no product name, no “like Apple” in the user's text.
- **The reader is “you”**; the product is “we” when it acts. “The user” lives in the spec, not in the copy.
- **One superlative per announcement, bound to yourself**; every figure with its base; every “up to” with its condition.
- **The medium sets the length**: 10 words per screen, the verb and its object on a button, 60 to 180 words in an email, a median of 14 words per sentence in prose.
- **French is asked, never guessed**: tu or vous, on or nous; then the typography of `french.md` § 4.

## Reference files: when to read them

| File | When |
|---|---|
| `references/grammar.md` | Step 2, once: the twelve rules, their counts, what the corpus never does (§ 13). |
| `references/media.md` | Step 2: the medium's section; § 1 for the move; § 9 for the lengths. |
| `references/functions.md` | Step 3: the shapes by function (announce, verdict, figure, how it works, price, ask, recap, close) and the short devices (§ 13). |
| `references/french.md` | When the text is in French: the French counts (§ 1), the French turns (§ 2), tu / vous / on (§ 3), typography (§ 4). |
| `references/targets.json` | The thresholds the script uses; cite them when a user asks where a number comes from. |
| `scripts/check_copy.py` | Steps 2, 3 and 4: the measures and the gaps. Python 3.9, no dependency. |
| `assets/example-email.md`, `assets/example-ui.md` | A before / after on a fictional product, with its table of changes: the level of detail expected at delivery. |
