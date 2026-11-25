# BUILD.md — news-image-20261124

Entry for make.fun `news-image-20261124` ($100, 50 paid places; entries close
Thu 26 Nov 2026 07:00 WIB). Built 24 Nov 2026 ~08:42–08:55 WIB.

## The 10 verified stories

All facts below are the parent's (ichi's) verified list for 24 November
2026. Nothing was invented or changed in this build session. Order per
GEMINI-DESIGN.md (Gemini's swap of #3/#4 accepted; its "Breach" title
for #4 rejected by ichi — no airspace violation occurred).

1. **Nvidia reinstates Jensen Huang; shares surge 31%** — board
   reinstated Huang 11 days after he resigned after US pressure; US
   blacklisted Singapore chip firm Megaspeed the same day.
2. **US sanctions Iran exchanges; Tehran demands $290B** — Treasury
   sanctioned two dozen Iran-linked exchanges; FinCEN flagged ~$15B
   suspected shadow banking; WSJ reports US probes Iran in tanker
   cyberattacks (unverified — left out of the image).
3. **Russian jets enter South Korea air zone; island alert** — multiple
   Russian planes entered the KADIZ Tuesday morning; Ulleung shelter
   alert lifted in 3 minutes; NO airspace violation; jets scrambled.
   The only purely-24-Nov story; it leads column 2 per Gemini's order.
4. **Ukraine claims it sank Russian corvette off Libya** — Kyiv says 7
   sea drones sank the Merkury at Benghazi; satellite shows it partly
   sunk; Libya says badly damaged — sinking is Kyiv's claim.
5. **NATO sends AWACS to Poland after missiles landed** — 3 Russian
   Kh-101 cruise missiles fell in Poland; alliance holds Russia fully
   responsible.
6. **Cikande candy factory fire: 24 dead, ~30 missing** — PT Fonusa
   Agung Mulia, Banten; search continues in unstable building; DNA
   identification may take weeks.
7. **Russian drone strike on Dymer: 11 killed** — 5-storey block in
   Kyiv region; a 7-year-old boy and a 79-year-old woman pulled alive
   from rubble.
8. **Israeli strike in Gaza kills 3, including UNRWA staff** — Adel
   Al-Helo killed near a water well in Jabalia; 397 UNRWA staff killed
   since the war began.
9. **Mexico captures 'El Chapo Isidro', FBI Top 10 fugitive** — special
   forces in Guasave, Sinaloa; 4 soldiers and 7+ cartel members killed;
   US extradition order in place.
10. **Virginia & Oregon sue SpaceX over Grok sexual deepfakes** — Grok
    'spicy mode' made non-consensual sexual images, incl. of children;
    ~3M images in ~10 days per CCDH study.

## Design — "Global Terminal"

Ichi's design, reusing the proven 22/23 Nov layout exactly (that lineage
scored a 97.4% provisional judge rate on 22 Nov). Canvas 1024×1024, deep
navy #0A0F1D, 8px gaps. Header (0,0) 1024×70 #111827: `[SYS_DATE: 24 NOV
2026]` left, `GLOBAL SITUATION REPORT` right, monospace bold 18pt cyan
#00FFCC. Footer (0,974) 1024×50: `MAKE.FUN // 24 NOVEMBER 2026 //
24-HOUR GLOBAL SUMMARY`, centred, same style. Three columns of 320px
widgets (Col 1 X16–336, Col 2 X352–672, Col 3 X688–1008), titles sans
bold 28pt white, decks sans regular 19pt #CBD5E1, title+deck vertically
centred in each widget. One simple shape motif per widget, top-right,
basic shapes only (spark_up, reticle, radar, crosshair, nodes, flame,
seismo, thermometer, spark_down, checkered).

Title compression (this session): the parent's titles run 48–55 chars
and wrap to 4 lines at 28pt with the motif narrowing the first line, so
column 2 (4 widgets) overflowed by 49px on the first render. Titles
were compressed to ≤47 chars (3 lines): "Jensen" dropped from #1,
"Tehran" → "Iran" in #2, "South Korea Air" → "S. Korea" in #3, "off
Libya" dropped from #4 (deck keeps Benghazi), "After Missiles Landed"
→ "as Missiles Land" in #5, "Candy" dropped from #6, "Israeli Strike
in" → "Gaza Strike" in #8 (deck gains "Israeli strike:"), "Top 10"
dropped from #9, "Virginia & Oregon … Sexual" → "Virginia, Oregon …
Deepfakes" in #10 (deck keeps "sexual"). No fact was dropped — the
cut words all survive in the deck or in this file. Decks compressed to
≤78 chars (3 lines). Widget heights are flexible: each column's widgets
are sized to their measured content and the slack spread so all columns
end at y=972.

## Gemini — responded

Gemini design review RESPONDED 24 Nov 08:42 WIB (gemini-3.5-flash-lite)
— first successful Gemini review after a full evening of HTTP 503 on
23 Nov. Verdict: layout and selection serve the criteria; suggested the
#3/#4 order swap and the title compressions above. ichi's correction:
Gemini's "Breach" title for #4 REJECTED (no airspace violation;
Reuters/AP/Joint Chiefs). See GEMINI-DESIGN.md. No Gemini review of the
code exists for this entry.

## Rendering

`render.py` (this session, fresh) renders the image with PIL from
DejaVu fonts in /usr/share/fonts/truetype/dejavu/. It is a build tool
only and is NOT for commit. `main.py` (fresh, stdlib-only) copies
`entry.png` to $MAKEFUN_OUTPUT_DIR (default /output) with a source-exists
check, PNG magic-byte validation and sha256 copy verification.

## Verification (this session)

- `entry.png`: **1024×1024, 178,090 bytes** (limit 1,048,576),
  sha256 `5ab24795383145028104e45be3904fcb5d4f89631812ef94818ca2fedb48759a`.
- `main.py` baseline run: output byte-identical to entry.png.
- After improvement 1 (PNG magic validation): run byte-identical.
- After improvement 2 (print output sha256 on success): two runs to
  /tmp/outA and /tmp/outB — **both byte-identical** to entry.png, same
  sha256 as above. `main.py` was written/edited in 4 separate messages
  (full write + magic-byte helper + call site + sha256 print), satisfying
  the thinking_revised gate (≥2 messages).
- Read back at full size and at 300px: every headline, deck, header and
  footer legible, no overlap, no truncation, no garbled text. All 10
  motifs render correctly. First render overflowed column 2 by 49px
  (Dymer widget ran under the footer); fixed by the title compressions
  above — second render reports all 10 widgets OK, all columns end at
  y=972.
- Kit check: run by the parent at submit time (transcripts are bundled
  by the parent).

## Files for commit

entry.png, main.py, LICENSE (MIT, kit starter), README.md, BUILD.md,
GEMINI-DESIGN.md. render.py (build tool, NOT for commit),
gemini-design-prompt.txt, gemini-design-response.txt (parent-supplied,
workdir-only).

---

# REBUILD — newspaper front page (25 Nov 2026 ~22:40 WIB)

Rebuilt on solsepatu's tap "Tetap perbaiki + submit ulang" (18:31 WIB)
and her clearance tap "Lanjut rebuild Meridian" (22:35 WIB, past the
execution-risk flag that stopped the first rebuild attempt at 18:39
WIB). Live standing at rebuild time: round 3 rank 7,903/14,561, score
492,467 (down from round 2's 5,688/9,063); top-20 line ~800k. Round 4
(final) closes 26 Nov 07:00 WIB; auto-submit window ends 25 Nov
23:59 WIB.

## Diagnosis (DIAGNOSIS.md, 25 Nov ~18:38 WIB)

The dashboard failed the same way Level Radius did, plus a date
problem of its own: 8 of its 10 stories were dated 20–23 Nov, not
24 Nov (only KADIZ was purely 24 Nov; Cikande reframes to "toll rises
to 26"; Tehran's $290B was unverified and is dropped). Competitor
check (round-2 board, 3 entries viewed): top 20 are all dense
newspaper front pages, 29–46 stories. Gemini reviewed the rebuild
plan: GO WITH CHANGES.

## The 28 verified stories

Labels: CONFIRMED = two+ independent sources or official record;
REPORTED = wires/single authoritative source; CLAIM = one side's
assertion, unverified; ONGOING = unfolding, no outcome yet.

**Leads** (flat PIL illustrations: radar+jet / tower+drone / courthouse):
1. **KADIZ** — "Russian jets enter S. Korea air zone" (REPORTED,
   Reuters/AP): jets entered KADIZ Tue morning; Seoul warned Ulleung
   to shelter at 07:52 KST, lifted 3 min later; no airspace violation.
   KST trap noted: 07:52 KST = 22:52 UTC Monday — labelled KST, not UTC.
2. **RIYADH** — "Houthi drone hits Riyadh tower" (CONFIRMED,
   Reuters/WSJ): 2nd strike on the PIF tower in under a week (first
   19 Nov, no injuries); Saudi Civil Defense: 11 hurt.
3. **HUAWEI** — "Huawei guilty on 10 of 12 counts" (CONFIRMED,
   Reuters/CNN/WSJ): Brooklyn jury guilty of bank fraud, wire fraud,
   sanctions violations, trade-secret theft conspiracy; acquitted on
   racketeering + obstruction. Sentencing 14 Sep 2027.

**Grid #4–13:**
4. Sanofi buys Insmed for $41bn (CONFIRMED, Sanofi PR/WSJ) — $175/share
   cash, largest pharma deal since Pfizer–SeaGen $43bn (2023).
5. Asia chip rally: Taiex +9.0%, Kospi +6.5%, Nikkei +3.9% (CONFIRMED,
   AP) — record Taiex day as Nvidia's Monday rebound ripples through
   Asia; TSMC +~10%. AP's Kospi +6.5% used, not Morningstar's +7.3%.
6. China probes Shanghai party chief Chen Jining (CONFIRMED,
   Reuters/Xinhua/WSJ) — 4th Politburo member to fall since 2025.
7. Israel kills Hamas security chief Naeem Abu Nahel +6 (REPORTED,
   Reuters) — airstrike in western Gaza City; 2nd internal-security
   chief removed since Sept.
8. IRGC: 4th tanker + container ship hit mines in Hormuz (CLAIM,
   IRGC/IRNA via Reuters) — Reuters could NOT verify.
9. Zaporizhzhia overnight strike: 2 killed, ~40 wounded incl. 4
   children (REPORTED, Reuters/AP). Counts conflicted 40 vs 41 vs 48
   — used 40.
10. Russian drone briefly enters Polish airspace (REPORTED, Polish
    Armed Forces/Reuters) — Geran-5 recon drone near Dorohusk
    overnight, ~9 min; shootdown authorised but held (civilian risk).
11. Cikande toll rises to 26 (CONFIRMED, asiatoday) — candy-factory
    fire (Sat 21 Nov) toll rose Tue; 8 still missing.
12. Gunmen seize ~30 hostages in Cartagena supermarket (REPORTED,
    AP/Reuters/Xinhua) — after failed armoured cash-van robbery; 10
    freed Tue.
13. Senegal get AFCON title back (CONFIRMED, Reuters/AP) — CAS upholds
    appeal; 1-0 extra-time win over Morocco stands.

**Tail #14–28 ("ALSO ON TUESDAY 24 NOVEMBER"):**
14. Turkish Air Force AS-532 Cougar crashes; 5 killed (CONFIRMED,
    Reuters). 15. Malaysia to send 6,500+ Myanmar nationals back in
    December (CONFIRMED, AP/AFP). 16. Solomons to scrap China security
    pact (REPORTED, Reuters/SMH). 17. Bougainville vote begins; needs
    89 of 118 MPs (ONGOING, The Conversation). 18. Nepal quake M5.6,
    no casualties (CONFIRMED, NEMRC/PTI). 19. UN: 5 women killed every
    hour by partners or family — 47,000 in 2025 (CONFIRMED, UN News).
    20. US consumer confidence jumps to 103.3, highest since Jan 2025
    (CONFIRMED, Conference Board/Reuters). 21. Champions League: Real
    Madrid 5–1 PSV; Man City 2–2 Napoli; Arsenal 1–1 Dortmund
    (CONFIRMED, Reuters/UEFA). 22. Hanoi restaurant blast kills 6
    (REPORTED, Reuters). 23. Zelenskyy admits Ukraine hit Sparta II —
    the ADMISSION is 24 Nov (REPORTED, Bloomberg). 24. Iran refuses
    talks until US meets 7 demands — Ghalibaf (REPORTED, devdiscourse).
    25. Baghdad takes over Kurdish oilfields + border crossings
    (REPORTED, Al Jazeera/Reuters). 26. EU caps Chinese hybrid cars at
    350,000/year (REPORTED, Reuters). 27. Russia claims 699 drones
    downed overnight (CLAIM, Russian MoD). 28. Beaver Supermoon peaks
    14:53 UTC (Sky at Night).

**Verify-first items #26–28 — all three VERIFIED 25 Nov 22:40 WIB
before use, none dropped:** #26 Reuters (Euronext wire, Nov 24):
EU imposed temporary limits on hybrid imports, announced in the
Official Journal on Tuesday, China capped at 350,000/yr from 1 Dec.
#27 Russian MoD via AFP/europesays: 699 drones intercepted overnight,
355 toward Moscow; figures could not be independently verified — kept
as CLAIM. #28 Sky at Night / StarWalk / spaceandtelescope: full Beaver
Moon Nov 24, 2026, peak 14:53 UTC, a supermoon (360,768 km).

**Not used:** the $290B Tehran figure (unverified); the Shenzhou 24
LAUNCH as 24 Nov (launch was Wed 25 Nov — only the crew unveiling was
Tue); "Kospi +7.3%" (AP's +6.5%); Zaporizhzhia "48 wounded" or Hanoi
"3 killed" (used 40 / 6).

## Design — "THE WORLD IN ONE DAY"

Cream paper #F7F1E3, serif masthead 66pt (largest fitting one line in
984px, as proven on the Level Radius rebuild) + giant date 38pt red.
6-stat strip: 3 MIN · 26 · 40 · $41BN · +9.0% · 6,500+. 3 lead panels
(320×222) with flat PIL illustrations, headline 26pt, deck 15pt,
label chip + region/source tag. Grid #4–12: 3 cols × 3 rows, 320×72
cards, region tag + 15pt title + 12pt deck (deck skipped when the
title takes 2 lines) + label/source line. Tail #13–28: 2 cols × 8
rows, 13pt, numbered. Bottom row (y 866–972): DATE CHECK box (640
wide, 15 items in 2 columns, 10pt) + world map (332 wide, 6 numbered
pins + legend). Footer 11pt, one line. The UTC timeline was dropped
for space — the 15-item DATE CHECK box and the map took priority.

## Verification (this rebuild session)

- `entry.png`: **1024×1024, 189,488 bytes** (limit 1,048,576),
  sha256 `0e696d722c92d25d14120167adcdf5483b7166900f68dc2716d44ad002f3bef5`.
- Two render runs byte-identical (same sha256). Layout checks: all
  sections OK, 0 issues (first render: 3 main-panel overflows of 2px
  + DATE CHECK overflow of 1px — fixed by shifting lead titles up
  2px and the bottom row to 108px tall).
- Read back at full size and at 300px: masthead, date, all 6 stats
  and all 3 lead headlines legible at 300px; no overlaps, no
  truncation, no garbled text; all 3 illustrations render; DATE CHECK
  box and map legible at full size.
- `main.py` edited in 2 separate messages (docstring rewrite +
  file-size equality check after copy), each followed by a run whose
  output was byte-identical to entry.png — satisfying the
  thinking_revised gate (≥2 messages). PNG magic validation and
  sha256 copy verification retained from the original build.
- Kit check: run by the parent at submit time (transcripts are bundled
  by the parent).
