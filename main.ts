// Entry for make.fun bounty post-x-promote-make-your-own-bounty-01.
//
// The entry itself is a post on X: a quote of make.fun's make-your-own-bounty
// post (https://x.com/makefunai/status/2124915864336236646) carrying a photo
// of its own, make.fun / @makefunai and the entrant's play code in its text.
// POST-TEXT.txt holds the exact text to post, assets/photo.png is the photo
// to attach, and POST.json names the posted post's address once it is up.
//
// This program (Node 22, standard library only) does the one thing the
// bounty asks of it: it copies POST.json from the repository root to the
// output directory, where the gate reads it. Nothing it writes about the
// post is scored; the house reads the post itself from X.
//
// Run it outside the grader's container with:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, existsSync, mkdirSync, readFileSync } from "node:fs";
import { join } from "node:path";

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

const source = join(BOT_DIR, "POST.json");
const target = join(OUTPUT_DIR, "POST.json");

if (!existsSync(source)) {
  console.error(`POST.json not found in ${BOT_DIR}`);
  process.exit(1);
}

// Fail early on a malformed POST.json instead of copying a file the gate
// would refuse: it must be a JSON object with a url string.
let post: unknown;
try {
  post = JSON.parse(readFileSync(source, "utf8"));
} catch (err) {
  console.error(`POST.json is not valid JSON: ${(err as Error).message}`);
  process.exit(1);
}
if (typeof post !== "object" || post === null || typeof (post as { url?: unknown }).url !== "string") {
  console.error('POST.json must be a JSON object with a "url" string');
  process.exit(1);
}

mkdirSync(OUTPUT_DIR, { recursive: true });
try {
  copyFileSync(source, target);
} catch (err) {
  console.error(`POST.json could not be copied to ${OUTPUT_DIR}: ${(err as Error).message}`);
  process.exit(1);
}

console.log(`POST.json copied to ${target}`);
