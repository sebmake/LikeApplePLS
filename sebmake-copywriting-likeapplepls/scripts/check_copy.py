#!/usr/bin/env python3
"""check_copy.py — measure a text against the keynote register and list the gaps.

Usage:
  python3 check_copy.py text.md [--lang en|fr] [--medium prose|slide|ui|email|web|notes] [--json]
  cat text.txt | python3 check_copy.py - --lang fr --medium email

Exit code: 0 = within the targets, 1 = gaps found, 2 = error.
Python 3.9+, standard library only. Targets live in ../references/targets.json
(measured on the official transcripts of 8 keynotes, 2019 to 2026; see grammar.md).
"""
import sys, re, json, os, statistics as st
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
TARGETS = os.path.join(HERE, "..", "references", "targets.json")

# ---------------------------------------------------------------- text helpers
def norm(text):
    text = text.replace("’", "'").replace("‘", "'").replace(" ", " ")
    text = re.sub(r"<[^>]+>", " ", text)                 # HTML tags
    text = re.sub(r"^\s{0,3}#+\s*", "", text, flags=re.M)  # markdown headings
    text = re.sub(r"[*_`>]+", "", text)
    return text

def units(text, medium):
    """Sentences for prose; one unit per line for slide / ui."""
    if medium in ("slide", "ui"):
        return [l.strip() for l in text.splitlines() if l.strip()]
    text = re.sub(r"\s*\n\s*\n\s*", " ¶ ", text)
    text = re.sub(r"\s+", " ", text)
    parts = re.split(r"(?<=[.!?…])\s+(?=[A-ZÀ-Ý«\"'“‘0-9¶])|\s¶\s", text)
    return [p.strip(" ¶") for p in parts if p and len(p.strip(" ¶")) > 1]

def words(s):
    return re.findall(r"[A-Za-zÀ-ÿ'\-]+|\d[\d,.]*%?", s)

def detect_lang(text):
    low = text.lower()
    fr = len(re.findall(r"\b(le|la|les|des|une|vous|nous|est|et|pour|avec|dans|sur|pas|plus|que|qui)\b", low))
    en = len(re.findall(r"\b(the|and|you|your|with|for|that|this|is|are|it|of|to|in|on|we)\b", low))
    return "fr" if fr > en else "en"

# ---------------------------------------------------------------- lexicons
EN = {
    "superlative_adj": r"\b(incredible|incredibly|amazing|amazingly|beautiful|beautifully|powerful|gorgeous|stunning|remarkable|remarkably|awesome|fantastic|huge|massive|breakthrough|magical|unbelievable|revolutionary|game.?changing|cutting.?edge|state.?of.?the.?art|best|fastest|biggest|thinnest|lightest|brightest|most\s+\w+)\b",
    "absolute": r"\b(world'?s (first|best|fastest|thinnest|most)|industry.?leading|best.?in.?class|(the )?(most \w+|best|fastest|\w+est) (\w+ ){1,3}(on the market|in the world|in the industry|of all time|ever made|available today)|unmatched|unrivaled|unparalleled|#1|number one)\b",
    "bounded": r"\b(yet|ever|to date|than ever|our most \w+)\b",
    "hedges": r"\b(we think|we believe|i think|i believe|we feel|maybe|perhaps|probably|kind of|sort of|a bit|somewhat|arguably|in our opinion|we hope)\b",
    "intensifiers": r"\b(very|really|truly|extremely|highly|super|totally|absolutely|literally)\b",
    "jargon": r"\b(leverage|synerg\w+|seamless\w*|robust|scalable|end.?to.?end|best practices?|streamline\w*|optimi[sz]\w+|empower\w*|holistic|paradigm|ecosystem|solution|solutions|innovative|innovation|cutting.?edge|next.?gen\w*|disrupt\w*|frictionless|turnkey|value.?add\w*|stakeholders?|deliverables?|touch ?points?|utili[sz]e|facilitate|enable[sd]?)\b",
    "passive": r"\b(is|are|was|were|been|being|be)\s+(\w+ed|built|made|done|designed|given|taken|seen|shown|sent|set|put|kept|held|chosen|written|brought)\b",
    "benefit_turn": r"\b(so you can|so that you|which means|that means|so you|now you can|you can now)\b",
    "second_person": r"\b(you|your|yours|you're|you've|you'll|you'd)\b",
    "first_plural": r"\b(we|our|ours|we're|we've|we'll|us)\b",
    "first_single": r"\b(i|my|i'm|i've|i'll|me|mine)\b",
    "third_user": r"\b(users?|customers?|clients?|the user|the customer|end.?users?)\b",
    "future": r"\b(will|'ll|shall|going to)\b",
    "openers": ["and", "so", "now", "but", "it", "it's", "this", "that's", "we", "you", "with", "introducing", "here's", "let's", "today"],
    "nominal_openers": r"^(introducing|meet|say hello to|welcome to|all.?new|the new)\b",
    "numbers_without_base": r"\b\d+(\.\d+)?\s?(x|times)\b(?![^.]*\b(than|compared|vs\.?|versus|over|from)\b)",
    "percent_without_base": r"\d+\s?%(?![^.]*\b(than|compared|vs\.?|versus|of|over|from)\b)",
    "up_to_bare": r"\bup to\b(?![^.]*\b(when|with|if|depending|on|under|in)\b)",
    "cta_verbs": r"^(get|try|start|learn more|see|buy|order|sign up|sign in|log in|download|watch|explore|discover|join|book|request|contact|continue|save|send|add|create|open|share|upgrade|subscribe|choose|compare|shop|view|read|install|activate|enable|turn on|turn off|cancel|done|skip|next|back|go|show|hide|edit|delete|remove|copy|print|export|import|search|filter|sort|select|apply|confirm|retry|pay|check out|accept|allow|deny|close|finish|submit|reset|undo|redo)\b",
    "click_here": r"\b(click|tap|press) (here|below|this link|the button)\b",
    "please_formula": r"\b(please|kindly|do not hesitate|feel free to|should you have)\b",
    "generic_error": r"\b(an error (has )?occurred|something went wrong|invalid input|operation failed|unknown error|error \d+)\b",
}
FR = {
    "superlative_adj": r"\b(incroyable\w*|magnifique\w*|superbe\w*|puissant\w*|remarquable\w*|exceptionnel\w*|révolutionnaire\w*|formidable\w*|génial\w*|énorme\w*|époustouflant\w*|spectaculaire\w*|le plus \w+|la plus \w+|les plus \w+|meilleur\w*)\b",
    "absolute": r"\b(au monde|du marché|de l'histoire|inégalé\w*|sans équivalent|numéro un|n°\s?1|leader (du|de la|des) \w+)\b",
    "bounded": r"\b(à ce jour|jamais|depuis sa création|de notre histoire|notre \w+ le plus|notre \w+ la plus)\b",
    "hedges": r"\b(nous pensons|je pense|nous croyons|je crois|peut-être|probablement|sans doute|un peu|plutôt|à notre avis|nous espérons|on espère)\b",
    "intensifiers": r"\b(vraiment|très|tellement|extrêmement|hautement|totalement|absolument|littéralement|super)\b",
    "jargon": r"\b(synergi\w+|robuste\w*|scalable\w*|optimis\w+|solution\w*|innovant\w*|innovation\w*|disrupt\w+|écosystème\w*|holistique\w*|paradigme\w*|levier\w*|accompagn\w+|fluidif\w+|processus|workflow\w*|roadmap\w*|onboarding|use case\w*|KPI\w*|ROI|parties prenantes|livrable\w*|déploy\w+|mise en place|dispositif\w*|problématique\w*|au niveau de|en termes de|dans le cadre de|afin de|permettre de|permet de|permettant)\b",
    "passive": r"\b(est|sont|a été|ont été|sera|seront|était|étaient)\s+\w+(é|ée|és|ées|is|ise|us|ue|it|ite)\b(\s+par\b)?",
    "benefit_turn": r"\b(pour que vous puissiez|pour que tu puisses|ce qui veut dire|ce qui signifie|vous pouvez donc|tu peux donc|désormais vous pouvez|vous pouvez désormais|de quoi \w+)\b",
    "second_person": r"\b(vous|votre|vos|tu|ton|ta|tes|toi)\b",
    "first_plural": r"\b(nous|notre|nos|on)\b",
    "first_single": r"\b(je|j'|mon|ma|mes|moi)\b",
    "third_user": r"\b(l'utilisateur\w*|les utilisateurs|le client|les clients|la clientèle|l'usager\w*)\b",
    "future": r"\b(\w+(erons|erez|eront|irons|irez|iront|aurez|aurons|serez|serons|pourrez|pourront)|va \w+er|allez \w+er|allons \w+er)\b",
    "openers": ["et", "mais", "voici", "c'est", "vous", "nous", "on", "avec", "maintenant", "il", "aujourd'hui", "découvrez", "imaginez"],
    "nominal_openers": r"^(voici|découvrez|bienvenue|le nouveau|la nouvelle|tout nouveau|toute nouvelle)\b",
    "numbers_without_base": r"\b\d+(\s?x|\s?×| fois) plus\b(?![^.]*\b(que|qu')\b)",
    "percent_without_base": r"\d+\s?%(?![^.]*\b(que|qu'|des|de|du|par rapport)\b)",
    "up_to_bare": r"\bjusqu'à\b(?![^.]*\b(selon|avec|si|en|sur|lorsque|quand|dans)\b)",
    "cta_verbs": r"^(\w+(ez|er|ir|re)|en savoir plus|voir|s'abonner|s'inscrire|passer à|aller à)\b",
    "click_here": r"\b(cliquez|cliquer|appuyez|appuyer|tapez) (ici|là|sur ce lien|sur le bouton|ci-dessous)\b",
    "please_formula": r"\b(veuillez|merci de|n'hésitez pas|prière de|ultérieurement|nos services|prise en compte|pris en compte|dans les meilleurs délais)\b",
    "generic_error": r"\b(une erreur (s'est produite|est survenue)|quelque chose s'est mal passé|erreur inconnue|opération échouée|saisie invalide|erreur \d+)\b",
}

# ---------------------------------------------------------------- measure
def measure(text, lang, medium):
    L = EN if lang == "en" else FR
    S = units(text, medium)
    W = [words(s) for s in S]
    lens = [len(w) for w in W if w]
    n = max(1, len(lens)); nw = max(1, sum(lens))
    low = text.lower()
    def p100s(c): return round(100.0 * c / n, 1)
    def p100w(c): return round(100.0 * c / nw, 2)
    def cnt(rx, where=low): return len(re.findall(rx, where))
    first = Counter(w[0].lower().strip("'") for w in W if w)
    m = {
        "units": len(lens), "words": sum(lens),
        "words_per_unit_median": st.median(lens) if lens else 0,
        "words_per_unit_max": max(lens) if lens else 0,
        "share_le_8": round(100 * sum(1 for l in lens if l <= 8) / n, 1),
        "share_ge_25": round(100 * sum(1 for l in lens if l >= 25) / n, 1),
        "units_ge_25": [s for s, l in zip(S, lens) if l >= 25],
        "units_gt_10_words": [s for s, l in zip(S, lens) if l > 10],
        "openers_and_so": p100s(first["and"] + first["so"] + first["et"] + first["donc"]),
        "openers_we": p100s(first["we"] + first["nous"] + first["on"]),
        "second_person_per100w": p100w(cnt(L["second_person"])),
        "first_plural_per100w": p100w(cnt(L["first_plural"])),
        "first_single_per100w": p100w(cnt(L["first_single"])),
        "third_user_per100w": p100w(cnt(L["third_user"])),
        "future_per100s": p100s(cnt(L["future"])),
        "passive_per100s": p100s(cnt(L["passive"])),
        "questions_per100s": p100s(sum(1 for s in S if s.rstrip().endswith("?"))),
        "exclamations_per100s": p100s(sum(1 for s in S if s.rstrip().endswith("!"))),
        "superlatives_per100s": p100s(cnt(L["superlative_adj"])),
        "superlatives_found": sorted(set(x if isinstance(x, str) else x[0] for x in re.findall(L["superlative_adj"], low))),
        "absolute_found": sorted(set(x if isinstance(x, str) else x[0] for x in re.findall(L["absolute"], low))),
        "bounded_found": sorted(set(x if isinstance(x, str) else x[0] for x in re.findall(L["bounded"], low))),
        "hedges_found": sorted(set(x if isinstance(x, str) else x[0] for x in re.findall(L["hedges"], low))),
        "intensifiers_per100s": p100s(cnt(L["intensifiers"])),
        "jargon_found": sorted(set(x if isinstance(x, str) else x[0] for x in re.findall(L["jargon"], low))),
        "benefit_turns_per100s": p100s(cnt(L["benefit_turn"])),
        "acronyms_found": sorted(set(re.findall(r"\b[A-Z]{3,}\b", text)) - {"USD", "EUR", "GPS", "USB", "PDF", "SMS", "API"} if False else set(re.findall(r"\b[A-Z]{3,}\b", text))),
        "numbers_units": p100s(sum(1 for s in S if re.search(r"\d", s))),
        "x_without_base": [s for s in S if re.search(L["numbers_without_base"], s.lower())],
        "percent_without_base": [s for s in S if re.search(L["percent_without_base"], s.lower())],
        "up_to_bare": [s for s in S if re.search(L["up_to_bare"], s.lower())],
        "triads_per100s": p100s(sum(1 for s in S if re.search(r"\w+, \w[\w ]*,? (and|et) \w", s) and s.count(",") >= 2)),
        "ellipsis_units": [s for s in S if "..." in s or "…" in s],
        "all_caps_units": [s for s in S if len(s) > 3 and s.upper() == s and re.search(r"[A-Z]{4,}", s)],
        "emoji_units": [s for s in S if re.search(r"[\U0001F300-\U0001FAFF☀-➿]", s)],
        "cta_units_not_verb_first": [s for s in S if medium == "ui" and len(words(s)) <= 4 and not re.match(L["cta_verbs"], s.lower()) and not re.match(L["nominal_openers"], s.lower())],
        "click_here_units": [s for s in S if re.search(L["click_here"], s.lower())],
        "please_units": [s for s in S if re.search(L["please_formula"], s.lower())],
        "generic_error_units": [s for s in S if re.search(L["generic_error"], s.lower())],
    }
    m["acronyms_found"] = sorted(m["acronyms_found"])
    return m

# ---------------------------------------------------------------- judge
def judge(m, lang, medium, T):
    gaps, notes = [], []
    t = T.get(lang, {})
    def gap(code, what, fix): gaps.append({"code": code, "what": what, "fix": fix})
    def note(code, what): notes.append({"code": code, "what": what})

    # length
    if medium in ("slide",):
        for u in m["units_gt_10_words"]:
            gap("L1", f"on-screen line over 10 words: “{u[:80]}”", "cut to 10 words or fewer (7 of 8 keynotes keep 10 or fewer per screen); move the rest to the spoken or body text")
    elif medium == "ui":
        for u in m["units_gt_10_words"]:
            note("L1", f"UI string over 10 words: “{u[:80]}” — fine for a description or an empty state, not for a label or a button")
    else:
        for u in m["units_ge_25"]:
            gap("L2", f"sentence of 25+ words: “{u[:90]}…”", f"split it; the transcripts run a median of {t.get('words_per_sentence_median', 14)} words and only {t.get('share_ge_25', 13)} % of sentences reach 25")
        if m["units"] >= 8 and m["share_le_8"] < t.get("share_le_8_min", 15):
            gap("L3", f"only {m['share_le_8']} % of sentences have 8 words or fewer", f"add short sentences: {t.get('share_le_8', 25)} % in the transcripts; a short one lands each idea")
    # person
    if m["third_user_per100w"] > 0 and m["second_person_per100w"] < m["third_user_per100w"]:
        gap("P1", "the reader is called “the user / the customer” more than “you”", f"address the reader: “you” runs {t.get('you_per100w', 2.3)} per 100 words in the transcripts, “the user” {t.get('users_per100w', 0.1)}")
    if m["first_single_per100w"] > 1.5 and medium != "email":
        gap("P2", f"“I / my” at {m['first_single_per100w']} per 100 words", f"keep the first person singular for a signed line or a spoken verdict ({t.get('i_per100w', 0.9)} per 100 words in the transcripts); the product speaks as “we”")
    if m["first_plural_per100w"] > 2.5 * max(0.3, m["second_person_per100w"]):
        gap("P3", f"“we” ({m['first_plural_per100w']}) outweighs “you” ({m['second_person_per100w']}) by more than 2.5 to 1", f"turn claims toward the reader: in the transcripts the two run close ({t.get('we_per100w', 2.5)} vs {t.get('you_per100w', 2.3)} per 100 words)")
    # tense / voice
    if m["future_per100s"] > t.get("will_per100s_max", 12):
        gap("T1", f"future tense in {m['future_per100s']} % of sentences", f"say what it does, not what it will do: the transcripts stay in the present ({t.get('will_per100s', 6)} % with “will”), except for dates")
    if m["passive_per100s"] > t.get("passive_per100s_max", 8):
        gap("T2", f"passive voice in {m['passive_per100s']} % of sentences", f"give each sentence its agent (the product, or you): {t.get('passive_per100s', 5)} % passive in the transcripts")
    if m["questions_per100s"] > 10:
        note("T3", f"questions in {m['questions_per100s']} % of sentences; the transcripts ask almost none ({t.get('questions_per100s', 1)} %) — one rhetorical question per text, at most")
    if m["exclamations_per100s"] > t.get("exclamations_per100s_max", 6):
        gap("T4", f"exclamation marks on {m['exclamations_per100s']} % of sentences", f"drop them: the verdict carries the weight, not the punctuation ({t.get('exclamations_per100s', 3)} % in the transcripts, mostly live applause lines)")
    # claims
    if m["absolute_found"]:
        gap("C1", f"absolute superlative without a cited proof: {', '.join(m['absolute_found'])}", "bound it to yourself (“our most … yet”, “for the first time”) or cite the external proof next to it")
    if m["superlatives_per100s"] > t.get("superlatives_per100s_max", 12):
        gap("C2", f"superlative adjectives on {m['superlatives_per100s']} % of sentences", f"one per announcement: the transcripts run {t.get('superlatives_per100s', 8)} %; the rest is plain description")
    for s in m["x_without_base"]:
        gap("C3", f"multiplier without its base: “{s[:80]}”", "name what it is compared to, in the same sentence (“than the previous version”, “than doing it by hand”)")
    for s in m["percent_without_base"]:
        gap("C3", f"percentage without its base: “{s[:80]}”", "say percent of what, compared to what")
    for s in m["up_to_bare"]:
        gap("C4", f"“up to” without its condition: “{s[:80]}”", "add the condition in the same sentence, or give the typical value")
    if m["hedges_found"]:
        gap("C5", f"hedges: {', '.join(m['hedges_found'])}", f"state it or cut it: “we think” appears in {t.get('hedges_per100s', 0.3)} % of transcript sentences")
    if m["intensifiers_per100s"] > t.get("intensifiers_per100s_max", 5):
        gap("C6", f"intensifiers (very, really, truly…) on {m['intensifiers_per100s']} % of sentences", f"cut them; the transcripts stay at {t.get('intensifiers_per100s', 2.5)} %")
    # words
    if m["jargon_found"]:
        gap("W1", f"jargon or filler: {', '.join(m['jargon_found'])}", "replace each with the concrete thing it hides (what it does, for whom, in which situation)")
    if m["acronyms_found"]:
        note("W2", f"acronyms: {', '.join(m['acronyms_found'])} — the transcripts carry {t.get('acronyms_per100w', 0.4)} per 100 words, each one spelled out the first time or known to the audience")
    for s in m["ellipsis_units"]:
        note("W3", f"ellipsis: “{s[:60]}” — keep it only for a suspended name before the reveal")
    for s in m["all_caps_units"]:
        gap("W4", f"all caps: “{s[:60]}”", "sentence case; weight comes from size and placement, not from capitals")
    for s in m["emoji_units"]:
        gap("W5", f"emoji in “{s[:60]}”", "none in the corpus; remove")
    # ui
    for s in m["cta_units_not_verb_first"]:
        note("U1", f"short UI string not verb-first: “{s}” — a button or a call to action starts with the verb; a label can stay a noun")
    for s in m["click_here_units"]:
        gap("U2", f"“click here”: “{s[:60]}”", "name the action itself on the button or the link (“Download the invoice”, “Continue”)")
    for s in m["please_units"]:
        gap("U3", f"formula: “{s[:70]}”", "say the thing plainly, without the politeness formula or the administrative wording; the register is direct and warm, not deferential")
    for s in m["generic_error_units"]:
        gap("U4", f"generic error: “{s[:70]}”", "say what happened and what to do next (“We couldn't save your changes. Check your connection and try again.”)")
    # benefit turn
    if medium in ("prose", "email", "web", "notes") and m["units"] >= 6 and m["benefit_turns_per100s"] == 0:
        note("B1", "no benefit turn (“so you can…”, “which means…”): the transcripts turn a feature into the reader's gain about once per block")
    return gaps, notes

def render(m, gaps, notes, lang, medium):
    out = [f"# check_copy — {lang}, {medium}", "",
           f"{m['units']} units, {m['words']} words, median {m['words_per_unit_median']} words per unit, "
           f"{m['share_le_8']} % at 8 words or fewer, {m['share_ge_25']} % at 25 or more.",
           f"you {m['second_person_per100w']} / we {m['first_plural_per100w']} / I {m['first_single_per100w']} per 100 words; "
           f"future {m['future_per100s']} %, passive {m['passive_per100s']} %, superlatives {m['superlatives_per100s']} %, "
           f"benefit turns {m['benefit_turns_per100s']} % of units.", ""]
    out.append(f"## Gaps ({len(gaps)})" if gaps else "## Gaps: none")
    for g in gaps: out.append(f"- **{g['code']}** {g['what']} → {g['fix']}")
    if notes:
        out.append(""); out.append(f"## Notes ({len(notes)})")
        for g in notes: out.append(f"- {g['code']} {g['what']}")
    return "\n".join(out)

def main(argv):
    if len(argv) < 2 or argv[1] in ("-h", "--help"):
        print(__doc__); return 2
    src = argv[1]
    lang = medium = None; as_json = False
    i = 2
    while i < len(argv):
        if argv[i] == "--lang": lang = argv[i + 1]; i += 2
        elif argv[i] == "--medium": medium = argv[i + 1]; i += 2
        elif argv[i] == "--json": as_json = True; i += 1
        else: print("unknown option", argv[i]); return 2
    try:
        text = sys.stdin.read() if src == "-" else open(src, encoding="utf-8").read()
    except OSError as e:
        print("cannot read:", e); return 2
    text = norm(text)
    if not text.strip():
        print("empty text"); return 2
    lang = lang or detect_lang(text)
    ALIASES = {"prose": "prose", "text": "prose", "texte": "prose", "email": "email", "mail": "email", "e-mail": "email", "newsletter": "email",
               "slide": "slide", "slides": "slide", "deck": "slide", "pptx": "slide", "powerpoint": "slide", "keynote": "slide", "screen": "slide",
               "ui": "ui", "strings": "ui", "interface": "ui", "microcopy": "ui", "app": "ui",
               "web": "web", "page": "web", "landing": "web", "site": "web", "notes": "notes", "release": "notes", "changelog": "notes",
               "script": "prose", "voice": "prose", "social": "web", "post": "web"}
    medium = (medium or "prose").lower()
    if medium not in ALIASES:
        print("unknown medium:", medium, "— use one of prose, email, slide, ui, web, notes"); return 2
    medium = ALIASES[medium]
    T = {}
    if os.path.exists(TARGETS):
        try: T = json.load(open(TARGETS, encoding="utf-8"))
        except Exception as e: print("targets unreadable:", e, file=sys.stderr)
    m = measure(text, lang, medium)
    gaps, notes = judge(m, lang, medium, T)
    if as_json:
        print(json.dumps({"lang": lang, "medium": medium, "measures": {k: v for k, v in m.items() if not isinstance(v, list)}, "gaps": gaps, "notes": notes}, ensure_ascii=False, indent=1))
    else:
        print(render(m, gaps, notes, lang, medium))
    return 1 if gaps else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
