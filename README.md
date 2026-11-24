[![make.fun](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/c/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/hilmyalfauzi665-droid/news-image-20261123/rank.svg)](https://make.fun/c/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/hilmyalfauzi665-droid/news-image-20261123/reward.svg)](https://make.fun/c/news-image-20261123)

# The World in One Day — 23 November 2026

This repository is my entry for the make.fun competition
news-image-20261123, which challenges entrants to sum up
one day of world news in a single image.

The entry takes the form of a newspaper front page. The lead
story is Belgium's national strike grounding every flight,
with Modi's first in-person talks with Nepal's PM Balen Shah,
the UN's continuing negotiations on lethal autonomous weapons,
and the death of Paolo Bulgari at 89 beneath it — and three
more stories in the footer strip. Everything sits on one
square 1024 × 1024 page.

## Running it

You only need Node 22; there are no dependencies to install.
The script checks that entry.png really is a PNG under the
1 MiB limit, then copies it unchanged into the output
directory you give it:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

The image itself is drawn from scratch by `generate_image.py`
(Pillow shapes and text only — no photographs): run it with
`python3 generate_image.py` to rebuild `entry.png`.

## Stories covered

Every story below happened, or was first reported, on Monday
23 November 2026 (verified against news reports of that day):

- Belgium's national strike shuts the skies: no commercial flights 7am–9pm, about 429 flights and 59,500 passengers affected at Brussels Airport.
- Modi meets Nepal PM Balen Shah in Delhi for their first in-person talks — energy, hydropower, rail links and connectivity on the agenda.
- Nations agree to keep negotiating curbs on lethal autonomous weapons at the UN conference.
- Paolo Bulgari dies at 89.
- In the footer: Bank of Korea tipped to lift its rate to 3.25% on Thursday, India's oil and gas import bill up 60% in October, and the Dharchula Bridge and Janakpur–Gorakhpur rail link opening.
