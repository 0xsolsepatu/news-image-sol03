# news-image-sol03 — World news, Tuesday 24 November 2026

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/0xsolsepatu/news-image-sol03/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/0xsolsepatu/news-image-sol03/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

Entry for make.fun `news-image-20261124` ($100, 50 paid places, entries close
Thu 26 Nov 2026 07:00 WIB): a program that writes one image summing up the
world's news of Tuesday 24 November 2026.

## The image

A "THE WORLD IN ONE DAY" newspaper front page, 1024×1024 PNG — 28
verified stories for Tuesday 24 November 2026 (rebuild of the original
"Global Terminal" dashboard, which scored round 3 rank 7,903/14,561):

- **Leads:** Russian jets enter S. Korea air zone (REPORTED, Reuters/AP);
  Houthi drone hits Riyadh tower, 11 wounded (CONFIRMED, Reuters/WSJ);
  Huawei guilty on 10 of 12 counts (CONFIRMED, Reuters/CNN/WSJ)
- **Grid:** Sanofi buys Insmed $41bn; Asia chip rally (Taiex +9.0%);
  China probes Shanghai party chief; Israel kills Hamas security chief;
  IRGC: 4th tanker hit mine in Hormuz (CLAIM); Zaporizhzhia strike
  (2 killed, 40 hurt); Russian drone enters Polish airspace; Cikande
  toll rises to 26; gunmen seize ~30 hostages in Cartagena
- **Tail (13–28):** Senegal AFCON title back; Turkish AS-532 crash;
  Malaysia returns 6,500+ Myanmar nationals; Solomons scrap China
  security pact; Bougainville vote; Nepal quake M5.6; UN femicide
  report; US consumer confidence 103.3; Champions League; Hanoi blast;
  Zelenskyy admits Sparta II strike; Iran refuses talks; Baghdad takes
  Kurdish oilfields; EU caps Chinese hybrids 350,000/yr; Russia claims
  699 drones downed; Beaver Supermoon peaks 14:53 UTC
- **DATE CHECK box:** 15 stories rejected as not 24 Nov (Nvidia,
  Megaspeed, Iran sanctions, Merkury, AWACS, Dymer, Gaza UNRWA strike,
  El Chapo Isidro, Grok suits, Cikande fire, COP31, EU sanctions
  package, FIFA 2031 hosts, Kh-101 missiles, Villavicencio car bomb)

## How it works

`main.py` (Python 3.13, standard library only) copies the pre-rendered
`entry.png` beside it to `/output/entry.png` — byte for byte, so two runs
write identical bytes, with a source-exists check, PNG magic-byte
validation, size check and sha256 copy verification. No network at
grading. See `BUILD.md` for the news sources, design choices and
verification steps.

<sub>Entered on [make.fun](https://make.fun/?ref=r4c0y56z&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
