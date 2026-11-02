# By medium: what the register becomes on a slide, in an interface, in an email, on a page

The grammar (`grammar.md`) was measured on spoken keynotes. A written medium keeps the same sentence, the same person, the same claims, but each one adds its own constraints: how much fits, who reads it, and what the reader is about to do. This file says what changes. Counts marked **(N/M)** come from the keynote corpus (8 keynotes, their on-screen text); the rest is **convention**, stated as such.

## Contents

1. The common frame
2. Slide and on-screen text
3. Interface strings (buttons, labels, empty states, errors, notifications)
4. Email
5. Web page (hero, feature block, specs, pricing, footer)
6. Release notes and changelog
7. Social post
8. Speaker script and voice-over
9. Length table

---

## 1. The common frame

Whatever the medium, the text does four things, in this order, and nothing else:

| Move | What it is | How long |
|---|---|---|
| **Name** | what we're talking about, in its exact name | 1 to 3 words |
| **Verdict** | what it is, in one plain sentence (“[Name] is the [simple] way to [benefit].”) | one sentence, 10 words or so |
| **Proof** | one feature, one figure with its base, or one thing you can now do | 1 to 3 sentences |
| **Ask** | what the reader does next, verb first | 1 to 4 words |

A text that skips the verdict is a feature list. A text that skips the proof is a slogan. A text that skips the ask leaves the reader where they were.

Across media, three constants from the corpus hold:
- **one idea per unit** (screen, string, paragraph): 8 of 8 keynotes put one idea per screen, shown when it is said;
- **the reader is “you”**, the product speaks as “we” when it must speak; “the user” never appears in the text the user reads;
- **nothing checkable is invented**: a figure, a price, a date, a name, a quote comes from the brief or stays `[TO PROVIDE]`.

---

## 2. Slide and on-screen text

The medium closest to the corpus: the keynote slides are on-screen text.

- **10 words at most per screen** (7/8), except lists, spec sheets and quotes. Count after translation: French runs about 15 to 20 % longer than English.
- **One idea per screen** (8/8). A slide that needs a second idea is two slides.
- **A title is a verdict or a name, not a topic.** “Faster syncing” says less than “Your files, everywhere, in seconds.” A topic title (“Performance”, “Our roadmap”) is allowed only as a section marker (A3 contents).
- **A figure stands alone, giant, with a one-line label that holds its base** (corpus: giant figure 30 to 40 % of the height, label about 4 %). “3×” means nothing without “than the previous version” in the label.
- **No bullets** on the slide (corpus: 0 bulleted lists). A list is a line-by-line build, each line a short noun phrase or a verb phrase, same form for every line.
- **Sentence case**, one period at most, no exclamation mark (keynote screens: 0 exclamation marks observed on title cards).
- **The call to action is the imperative**, 1 to 3 words (“Order today”, “Try it free”); the condition goes aloud or in the notes.
- **The speaker notes carry the rest**: everything cut from the screen goes to the spoken text, in full sentences (`§ 8`). The skill writes both when asked for a deck; the deck itself is `sebmake-keynote-likeapple-pls`'s job.

Trap: writing the spoken sentence on the slide. The screen shows the noun or the verdict; the mouth says the sentence.

---

## 3. Interface strings

Not in the corpus (the keynotes show interfaces, they don't write them). **Convention**, built from the corpus register applied to what a string must do.

| String | Form | Example of the move |
|---|---|---|
| **Button, primary action** | verb first, 1 to 3 words, what happens when you press it | *Download the invoice* · *Continue* · *Send the request* |
| **Button, secondary** | the exact alternative, not a politeness word | *Not now* · *Keep editing* · *Cancel* |
| **Title of a screen** | a noun or a name, 1 to 4 words, no verb | *Invoices* · *Your team* · *New order* |
| **Label of a field** | the thing asked, 1 to 3 words, no colon, no “please” | *Email* · *Delivery date* · *Company name* |
| **Helper text** | one sentence, present tense, says what the field is for or what it changes | *We'll send the receipt here.* |
| **Empty state** | verdict + ask: what belongs here, and the one verb to fill it | *No invoices yet. Create your first one.* |
| **Confirmation** | what just happened, past tense, named object | *Invoice sent.* · *Order saved.* |
| **Error** | what happened + what to do, two short sentences, no code, no “an error occurred” | *We couldn't save your changes. Check your connection and try again.* |
| **Destructive confirmation** | the consequence, plainly, then the verb on the button | *This deletes the order and its 3 documents. You can't undo this.* → **Delete the order** |
| **Notification** | subject + verb + object, 6 to 10 words, what the reader can do if anything | *Your order 1042 left the warehouse.* |
| **Toggle / option** | the state as a noun phrase, never a question | *Email notifications* · *Dark mode* |
| **Onboarding step** | one verb line + one benefit sentence | *Add your team. They'll see every order you share.* |

Rules that follow from the register:
- **The button says the action, never “Click here”, “OK”, “Submit”, “Validate”.** The verb names the outcome (*Pay*, *Send*, *Save*), the object when it's ambiguous (*Save the draft*).
- **No “please”, no “kindly”, no “successfully”.** Directness is the politeness: *Order saved.* says it; *Your order has been successfully saved.* says it slower.
- **No passive, no “has been”.** The product did it or you did it.
- **No “the user”, no “the customer”** in text the reader sees: *you*.
- **No jargon of the product's own making** in a first-level string: say *order*, not *transport instruction object*; the internal name goes in the documentation.
- **Keep the terms stable**: one word for one thing across the interface (if it's *order* here, it's *order* in the email too). The skill keeps a glossary when it rewrites a set of strings (see `SKILL.md`, step 3).
- **Numbers and dates**: the format of the audience's locale; relative when recent (*2 minutes ago*), absolute when it matters (*June 12, 9:41*).
- **Length is set by the component**: a button that wraps is a sentence pretending to be a button. The skill asks for the width when it matters and proposes the shortest form first.

---

## 4. Email

Not in the corpus. **Convention**, from the keynote register applied to a message someone opens by choice.

**Structure** (five parts, each one at most a few lines):

1. **Subject**: the verdict or the news, 4 to 8 words, no “Important”, no brackets, no exclamation mark. *Your invoices now arrive on time.*
2. **Opening line**: the news itself, in one sentence. No “Dear valued customer”, no “We are excited to announce”. Start with the thing: *Starting today, every order…*
3. **The move**: name → verdict → proof (one each), as in § 1. One feature per email; a second one is a second paragraph with its own verb line, or a second email.
4. **The ask**: one link or one button, verb first, 1 to 4 words. One ask per email.
5. **Sign-off**: a first name and a role, or the team's name; no “Best regards”, no closing formula.

**Register**:
- **Present tense**: what it does now. The future only for a date (*Available June 12.*).
- **You** throughout; **we** when we did something (*We've fixed…*). “I” only in a message signed by one person about their own act.
- **Short paragraphs**: 1 to 3 sentences, 8 to 16 words each; a long email is 120 to 180 words.
- **No apology, no hedge, no “as you know”**. A problem is stated as a fact and followed by what we did.
- **No politeness formula** (*please do not hesitate*, *should you have any questions*): the ask is the help offered. If support matters: *Reply to this email and a person answers.*

**French**: *vous* by default to a customer, *tu* if the brand does so everywhere (asked, never guessed); *on* rather than *nous* when the brand is casual; typographic rules in `french.md`.

---

## 5. Web page

Not in the corpus as pages, but the keynote blocks map onto them one for one: the announcement sequence is a landing page read from top to bottom. **Convention.**

| Section | Keynote equivalent | Text |
|---|---|---|
| **Hero** | name alone, then verdict (A1, A4) | the name (1 to 3 words), one verdict sentence (10 words or so), one ask verb-first. No paragraph. |
| **Tension** | the problem (step 5) | one or two sentences on what the reader lives with today; concrete, no drama. |
| **Feature blocks** | one announcement each (steps 7 to 9) | a verb headline (2 to 5 words) + one proof sentence + one benefit turn (*so you can…*). Three to six blocks, one idea each. |
| **Figure** | giant figure (A5) | the number alone, label with its base; the condition under it if the audience needs it (`publics.md` of the keynote skill). |
| **Proof from others** | testimonial (A17) | real, authorized, with name and role; never written by the skill. |
| **Specs** | spec sheet (A11) | a table: nouns, units, no adjectives. |
| **Pricing** | price anchored (A19) | *from [price]*, period and tax status stated; the ask right under. |
| **Footer card** | final card | sources, legal notes, small. |

Rules:
- **Headline = verb or verdict**, not a topic. *Share a quote in one tap.* beats *Quote sharing*.
- **One ask per screenful**, the same verb each time it repeats.
- **A superlative bound to yourself** (*our fastest yet*), one per page, and only if true; an absolute one (*the best on the market*) only with its proof next to it.
- **Benefit turn once per block** (*so you can…*, *which means…*): the corpus turns a feature into the reader's gain about once per announcement.
- **No “solutions”, “platform”, “ecosystem”, “seamless”**: say the thing.

---

## 6. Release notes and changelog

**Convention.** The keynote's mini-recap (step 12) in writing.

- **One line per change, verb first, past or present**: *Export invoices as PDF.* · *Fixed the date filter on orders.*
- **Group by what the reader does**, not by component: *Orders*, *Invoices*, *Team*; not *Backend*, *API*.
- **Say what changes for the reader**, not how it was done: *Pages load twice as fast* (with the base) rather than *Migrated the cache layer*.
- **No “various improvements”, no “minor fixes”**: name them or leave them out.
- A headline change gets the full move (name, verdict, proof, ask); the rest is the list.

---

## 7. Social post

**Convention.**

- **One idea, one verb line, one ask**, under 40 words. The verdict sentence can be the whole post.
- **No hashtag chain, no emoji** (none in the corpus; the verdict carries the weight).
- **The figure with its base** or no figure.
- **The name of the product once**, spelled as the brand spells it.

---

## 8. Speaker script and voice-over

The corpus itself (`grammar.md`). What a written script must keep:

- **Full sentences**, median 14 words, with a short one (≤ 8 words) every three or four sentences.
- **“And” / “So” / “Now” openers** carry the thread (about one sentence in six starts with one of them in the corpus): keep them in a script, cut them in print.
- **Phrases by function** (`functions.md`): opening, name, verdict, figure, demo, handover, recap, close.
- **The name alone, then silence** before the verdict (1 to 2 s on stage; a beat in a voice-over).
- **One superlative per announcement**, bound (*yet*, *ever*).
- A voice-over for a film: shorter sentences (median 13 words in the film measured), present tense, *you* throughout, and one sentence per shot (see the motion skill's `film-fonctionnalites.md`).

---

## 9. Length table

| Medium | Unit | Target | Source |
|---|---|---|---|
| Slide | words per screen | ≤ 10 | corpus (7/8) |
| Slide title | words | 1 to 6 | corpus title cards |
| Button | words | 1 to 3 | convention |
| Field label | words | 1 to 3 | convention |
| Error | sentences | 2 (what happened, what to do) | convention |
| Notification | words | 6 to 10 | convention |
| Email subject | words | 4 to 8 | convention |
| Email body | words | 60 to 180 | convention |
| Paragraph (email, web) | sentences | 1 to 3 | convention |
| Sentence (prose) | words | median 14, ≤ 8 for one in four, ≥ 25 for one in eight at most | corpus transcripts (see `targets.json`) |
| Headline (web) | words | 2 to 6, verb or verdict | convention |
| Verdict sentence | words | 8 to 14 | corpus (A4 thesis) |
| Release note line | words | 4 to 12 | convention |
| Social post | words | ≤ 40 | convention |
