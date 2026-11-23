# Post-x-promote-make-your-own-bounty-01 — agent brief

## Goal
One quote-post on X promoting make.fun's make-your-own-bounty post
(https://x.com/makefunai/status/2124915864336236646). Top 50 share $250;
score = replies + reposts + quotes at the deadline 2026-11-26T18:35:00Z.

## The post (Dewa posts this himself from his public X account)
1. Open make.fun's post on X → Repost → Quote.
2. Paste the text from POST-TEXT.txt exactly (it already carries the required
   line, @makefunai, the make.fun link and play code
   `makefun-boulder-bagpipe-mackerel`).
3. Attach assets/photo.png (made by scripts/make_photo.py).
4. Post, then copy the post's address into POST.json as
   `{"url": "https://x.com/<handle>/status/<id>"}` and submit this repo.

## The program
main.ts (Node 22, stdlib only) copies POST.json to /output. Run:
`mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts`

## Rules that matter
- One post per entrant; the post stays up and public until results are out.
- Never buy/bot engagement, never post the same update twice.
- make.fun's wordmark in the photo comes from the press pack
  (https://make.fun/press/manifest.json), used as it is.
