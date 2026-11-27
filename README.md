# World News in One Image — 27 November 2026

[![make.fun · news-image-20261127](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/nonicon/world-news-one-image-27-nov-2026/rank.svg)](https://make.fun/bounty/news-image-20261127/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/nonicon/world-news-one-image-27-nov-2026/reward.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)

A one-page newspaper front page summing up the world news of
**Friday, 27 November 2026**. The image is the entry: `main.py`
copies the pre-rendered `entry.png` to the output directory.

## What the image shows

- **Lead story — The Gulf:** Drones kill two Italian technicians in
  Kuwait; Italy and Kuwait blame Iran, and Tehran denies any role.
- **Weather / United States:** A Thanksgiving storm blacks out
  900,000 homes and businesses and forces the first-ever postponement
  of the 100th Macy's parade.
- **Middle East / Gaza:** Hamas weighs its response after Israeli
  strikes kill 10 people in Gaza.
- **Economy / United States:** US growth is revised up to 4.3% for
  the third quarter, while the president demands a probe into what he
  calls "fake" GDP figures.
- **Sport / Chess:** World champion D. Gukesh and Javokhir Sindarov
  draw a marathon third game of the world title match in Geneva.
- **War / Ukraine:** Russia hits Kyiv with ballistic missiles, as
  Zelensky tells the BBC the US is too focused on the Middle East.
- **Britain / Migration:** Net migration to the UK falls to its
  lowest level since 1997, excluding the pandemic years.
- **Also today (ticker):** A tanker capsizes off Ibiza, killing one;
  Gérard Depardieu is to stand trial over an alleged 2018 rape;
  Ebola in Congo passes 12,000 cases; Nepal declares 4,000 landslide
  victims dead; Saudi Arabia intercepts Houthi missiles aimed at
  Riyadh.

Every story was checked against news reported on 27 November 2026
before the image was drawn. Events from other dates were left out.

## How the image was made

`render.py` paints the front page from scratch with Pillow: masthead
and date line, a flat-illustration lead panel (Kuwait Towers, a radar
dish and a drone at dusk), six story cards with small pictogram
panels, and a news ticker. All text is set in DejaVu Serif and
DejaVu Sans. No photographs or artwork from any other source are used.

## Running it

```sh
python3 render.py          # rebuild entry.png from the drawing code
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.png
```

`main.py` uses only the Python standard library, needs no network,
and writes identical bytes on every run. The output is a 1024×1024
PNG, well under the 1 MiB limit.

## Licence

MIT — see `LICENSE`.
