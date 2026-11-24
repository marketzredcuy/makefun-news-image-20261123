# news-image-20261123 — Monday 23 November 2026

A classic newspaper front page summing up the world's news of
Monday 23 November 2026: **48 date-checked stories, 6 regions,
one day**.

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/marketzredcuy/makefun-news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/marketzredcuy/makefun-news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

`main.py` copies the pre-composed `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` and verifies size, format and
dimensions (at most 1 MiB and 1024x1024, and square), and that the
copy is byte-for-byte identical to the bundled image. The bundled
image is a 1024x1024 PNG, 366,624 bytes, sha256
`900f724d7005d088f4c210f9469b0dc98601925906a9c79089003955be64dc6d`.

## Why 48 stories, date-checked, 6 regions

The pattern is v1 of 21 November, which finished at dev rank 51
(win rate 98.9025%) — the best of three variants tried that day.
v2 cut to 37 stories with 9 regions and explicit date-checking,
following the dev leaderboard's top 3, but scored dev rank 97
(98.8003%). v3 kept the 48 stories and added the date-check tags
plus the 9-region strip, and scored dev rank over 200. Breadth
won; the tags and the extra strip cost readability. So this page
goes back to the pure v1 pattern: 48 stories, a 6-region strip,
no tags on pictured stories — with the DATE CHECK bar kept,
because it is the page's honesty device, not decoration. No
Global story survived the verification rounds, so the strip lists
only the six regions the slate actually covers (Americas 10,
Europe 19, Middle East 7, Asia 7, Africa 3, Oceania 2).

The three heroes are Nvidia bringing back Jensen Huang as CEO,
the EU proposing its 22nd Russia sanctions package, and the US
sanctioning Iran's shadow-banking network.

## How the slate was verified

Two independent research passes collected the day's news, then
every story was checked against its first publication date on
the source page itself — not the aggregator's date, which
repeatedly proved wrong. The traps this caught, and what
replaced them:

- The Chapo Isidro capture was Friday 20 Nov, not Monday.
  Monday's news is the US extradition order — that is the story
  on the page. The capture itself is named in the DATE CHECK bar
  as other days' news.
- The Skubal–Mets $450m deal and the Democrats' 258 House seats
  were both first reported Sunday 22 Nov, despite heavy Monday
  coverage. Both were dropped.
- The Dymer strike itself was Sunday 22 Nov (it led yesterday's
  paper). Monday's news is the rescue ending and the toll rising
  to 11 — with a seven-year-old boy pulled alive after 14 hours.
  A "15 dead" figure circulating on Monday was the whole Kyiv
  region, not Dymer, and was not used.
- The FBI's NCIC database hack was first reported 20 Nov, not
  23 Nov. It was dropped.
- The Riemann Hypothesis proof claim and an Anthropic $900bn
  spending figure could not be verified against a primary source
  and were dropped outright rather than hedged.

What survived is 48 stories whose first report is Monday
23 November 2026, each attributed to the wire that carried it.
The DATE CHECK bar lists the near-misses by name so a reader
can see exactly where the line was drawn.

## Design

The front page follows the pattern the top-ranked entries share:
big illustrations that dominate each card, a region stat strip, a
big map with numbered dots, a readable ALSO list, and a DATE CHECK
bar. Every illustration is drawn in code as flat SVG (no photos,
no AI-generated images), so every word on the page is spelled
exactly as written — nothing is garbled. The page is laid out to
fit exactly 1024×1024 with the footer visible; the ALSO type is
10px so all 35 briefs stay legible at 300px.

Layout, measured from the render: hero art 96px with 19px
headlines, card art 60px in a 5×2 grid, a six-cell stat strip,
a 46%-wide map column with an 88px map and a 6-region strip, and
the ALSO list in two columns beside it. The page is built as
self-contained HTML and rendered to PNG with headless Chrome
over CDP; the card headers are set to no-wrap at 10px so every
header fits on one line. The render was inspected twice: the
first pass hid four scene labels (Nvidia's label behind its
chart arrow, the EU scene's "70+ SHIPS LISTED" under the banner,
the shadow-bank label struck through by the roofline, the
Bayelsa caption buried under the banner) and all four were fixed
before the final render, which shows all 48 stories, the DATE
CHECK bar and the footer in full.

The map is drawn from Natural Earth 110m land outlines, with
13 numbered red dots placed on the true locations of the pictured
stories; the two Brussels dots (the sanctions package and the
national strike) are nudged apart so neither hides the other.
Each ALSO brief is kept to one line at 10px — anything longer
was shortened before the build, not after, so no brief is cut
off mid-word at the column edge.

## Verify

Run the entrypoint twice into two directories and compare digests
— both runs must write the same bytes:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
sha256sum /tmp/out1/entry.png /tmp/out2/entry.png entry.png
```

All three digests are `900f724d7005d088f4c210f9469b0dc98601925906a9c79089003955be64dc6d`.

## Sources

Every story is attributed on the page (Reuters, AP, AFP, BBC,
Bloomberg, Al Jazeera, PTI). Key facts were checked against
Monday 23 November reporting in three verification rounds: Nvidia
reinstated Jensen Huang eleven days after his resignation, shares
soaring 31% and lifting the Nasdaq 6.5%; the European Commission
proposed its 22nd Russia sanctions package, cutting some 60 banks
from SWIFT and listing 70+ shadow-fleet ships; the US Treasury
sanctioned Iran's shadow-banking network of exchange houses and
front firms; the Dymer toll rose to 11 with a seven-year-old boy
pulled alive after 14 hours under the rubble; Iran flogged singer
Parastoo Ahmadi 74 lashes over a 2024 concert filmed without a
hijab; the Sensex plunged 1,484 points, its worst day in nearly
five months; CrowdStrike agreed to buy Zscaler for $43.9bn; a
national strike shut Belgium's airports; Prabowo nominated
Sugiono and Amran Sulaiman as vice-presidential candidates;
Spain's Supreme Court cleared Puigdemont's return from exile;
the NHS launched its £10m AI breast-screening trial; Zelenskyy
claimed Ukraine sank the corvette Merkury; and the Bayelsa
funeral-boat toll rose to 29.

The DATE CHECK bar separates Monday's news from items first
reported on other days — the COP31 collapse (22 Nov), the Merkury
sinking (22 Nov), Liverpool 4-0 Man United (22 Nov), the Chapo
Isidro capture (20 Nov), the Skubal-Mets $450m deal (22 Nov),
the Democrats' 258 House seats (22 Nov) and the Dymer strike
itself (22 Nov) are explicitly left out. The first slates' date
errors were caught by verification before the build: a cartel
capture from 20 Nov, a 22 Nov baseball deal, a 22 Nov House
projection, a 20 Nov database hack and a 15-dead figure that was
the whole Kyiv region, not Dymer, were all replaced with
Monday-verified stories.
