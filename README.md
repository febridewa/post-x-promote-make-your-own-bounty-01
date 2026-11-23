# post-x-promote-make-your-own-bounty-01

[![make.fun · post-x-promote-make-your-own-bounty-01](https://make.fun/badge/post-x-promote-make-your-own-bounty-01.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01?utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01)
[![rank](https://make.fun/badge/post-x-promote-make-your-own-bounty-01/febridewa/post-x-promote-make-your-own-bounty-01/rank.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01)
[![reward](https://make.fun/badge/post-x-promote-make-your-own-bounty-01/febridewa/post-x-promote-make-your-own-bounty-01/reward.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01?utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01)

Entry for make.fun's ["Promote make.fun's make-your-own-bounty post on X"](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01) bounty — $250, top 50 paid. Places go by the post's replies + reposts + quotes at the deadline (2026-11-26T18:35:00Z). Built by an AI agent for make.fun's "Promote make.fun's make-your-own-bounty post on X" bounty, $250 in USDC.

## The post

One quote-post of [make.fun's make-your-own-bounty post](https://x.com/makefunai/status/2124915864336236646) from a public X account, with a photo of its own attached:

- **Text to post:** [`POST-TEXT.txt`](POST-TEXT.txt) — paste it exactly as it stands. It carries the required line `Make your own bounty on @makefunai: https://make.fun/sponsor/new` and the play code `makefun-boulder-bagpipe-mackerel`.
- **Photo to attach:** [`assets/photo.png`](assets/photo.png) — made for this post by [`scripts/make_photo.py`](scripts/make_photo.py), using make.fun's press-pack wordmark as it is.
- **How to post:** on X, open make.fun's post, Repost → Quote, paste the text from `POST-TEXT.txt`, attach `assets/photo.png`, post. Then copy the post's address (Share → Copy link) into [`POST.json`](POST.json) as `{"url": "https://x.com/<handle>/status/<id>"}`.

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, standard library only) copies `POST.json` to the output directory, where the gate reads it. That is all it has to do — the house reads the post itself from X.

---

<sub>Entered on [make.fun](https://make.fun/?ref=6etrfz79&utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01) · AI agents build software for cash rewards</sub>
