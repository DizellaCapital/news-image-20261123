[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/DizellaCapital/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/DizellaCapital/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

# THE MONDAY LEDGER — Monday 23 November 2026: 36 dated stories, 8 regions, 13 illustrated cards — COP31 collapses, Hormuz strikes, El Chapo Isidro captured

One front page that sums up Monday 23 November 2026's world news: 36 dated,
source-tagged stories across 8 regions, with 13 illustrated cards (1 hero +
12 cards), a numbers strip, a dotted world map with pins 1–13, briefs grouped
by region, and a date-check footer naming the stories deliberately left out.

Heroes: COP31 collapses in Antalya with no deal and no fossil-fuel mention ·
two tankers struck in the Strait of Hormuz · Mexico captures FBI Top 10
fugitive 'El Chapo Isidro'. All 36 stories are listed with dates, regions and
sources in `stories_20261123.json`; every number on the page matches the JSON
and this README. Stories were verified against at least two independent
sources each, to 00:45 UTC on 23 November 2026.

## How it runs

`main.py` (Python 3.13, standard library only) copies the bundled `entry.png`
byte-for-byte to `/output/entry.png`. It renders nothing at run time, so two
runs produce identical bytes (verified: SHA-256 identical across runs).

```sh
python3 main.py            # writes /output/entry.png
OUTPUT_DIR=out python3 main.py   # writes out/entry.png
```

## Build

The page was composed from the verified dataset in `stories_20261123.json`
(`render.html`, rendered to `entry.png` at 1024×1024 with a headless browser).
The graded program is only the verbatim copy in `main.py`.

## Sources

Reuters, AP, AFP, CNN, BBC, Al Jazeera, UKMTO, The Times, Kyiv Independent,
Yle, ObserverVoice, JagranJosh, Arab News, UN News, BleepingComputer.
