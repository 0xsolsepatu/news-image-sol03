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
