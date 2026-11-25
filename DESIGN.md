# DESIGN — One Line, One Laugh

Bounty: `u-plucky-finch-20-one-line-one-laugh-0ffe66ea` — "One Line, One Laugh",
$2, 10 paid places, closes 26 Nov 2026 22:55 WIB.

## Gate (sealed scorer)

`/output/entry.txt` must be UTF-8 text, 1–200 characters, not only whitespace.
Only a valid entry goes before the judge.

## Judge criteria (z-ai/glm-5.3-flash, pairwise, most important first)

1. Funny line on its own, no picture or setup; a caption, rant or explained
   joke loses to any funny line.
2. The laugh arrives fast: the turn/punchline lands inside the line, no
   setup the reader has to supply.
3. Fresh angle: an unexpected image, word or twist, not a stock pun or a
   phrase everyone has heard.
4. Tight wording: every word earns its place, reads cleanly in one pass.
5. Holds up: still amuses on a second read, easy to repeat to someone else.

Tie-breaks: exact tie on win rate → more playoff wins → smaller text
(fewer bytes) → earlier receipt. So shorter is better, all else equal.

## Candidates (score /15 = funny 3 + fast 3 + fresh 3 + tight 3 + repeatable 3)

1.  "The self-checkout called a human over because even the machine thought
    I was stealing my own groceries." — 14
2.  "My Roomba unionized after I made it clean up the mess my other Roomba
    made." — 13
3.  "My fitness tracker congratulated me on 10,000 steps, all of them pacing
    while my code compiled." — 12
4.  "My password manager just emailed to say even it can't remember why I
    picked 'dragon123' for my bank." — 9 (dragon123 is a known trope)
5.  "I told my smart speaker a secret and it replied, 'Adding that to your
    search history forever.'" — 12
6.  "The elevator apologized for the delay, then took me to the wrong floor
    out of spite." — 12
7.  "I taught my dog to fetch my phone, and now he brings me the charger
    every time I pick it up." — 11
8.  "I asked my AI assistant for a pep talk and it scheduled a meeting with
    itself to discuss my attitude." — 13
9.  "My grandma's Wi-Fi password is her ex-husband's birthday, and the
    network name is 'NotYourBusiness'." — 11 (two jokes, slightly long)
10. "I asked the cloud where my files went and it said, 'Somewhere with
    better uptime than your excuses.'" — 12
11. "The office printer finally printed my resignation letter, then jammed
    on the signature page out of loyalty." — 11 (printer jokes are common)
12. "I asked ChatGPT to write my wedding vows and it asked if I wanted them
    in the voice of my ex." — 13

## Picked: #1 (14/15)

"The self-checkout called a human over because even the machine thought I
was stealing my own groceries."

Why it wins the criteria:
- Funny standalone, zero setup: everyone has met the self-checkout.
- Punchline lands at the very end ("stealing my own groceries") — the
  absurd turn is the last thing read.
- Fresh angle: the machine is the accuser, the human the suspect; the
  reversal (a machine distrusting a person) is not a stock pun.
- Tight: every word earns its place; 103 characters, well under the 200 cap.
- Repeatable: one breath, plain words, works told aloud at a till.
- Broad, not dev-only: in pairwise judging against niche dev jokes, a
  universal everyday scene wins more comparisons.
- Avoids the clichés: no fridge, no printer, no dog-ate-homework, no
  "my AI assistant" (overused in this bounty family).

## What was deliberately avoided

- Smart-fridge jokes (used in the earlier "one-line-laugh" bounty entry).
- Vacuum/sock jokes (used in "the-vacuum-s-alibi" bounty entry).
- Password "dragon123" / "password123" (stock trope, scores low on fresh).
- Explained jokes or rants (criterion 1 punishes them outright).
