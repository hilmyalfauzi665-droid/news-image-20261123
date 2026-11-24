// Entry program for news-image-20261123 (Node 22, standard library only).
//
// The entry is a newspaper front page summing up Monday 23 November 2026:
// Belgium's national strike grounding every flight, Modi's first in-person
// talks with Nepal's PM Balen Shah, the UN's continuing negotiations on
// lethal autonomous weapons, and the death of Paolo Bulgari at 89 — plus
// three briefs in the footer. The image was drawn from scratch by
// generate_image.py in this repository (Pillow shapes and text only, no
// photographs), and it lives here as entry.png.
//
// All this program does is check that entry.png really is a PNG under the
// 1 MiB limit and copy it, byte for byte, into the output directory the
// grader provides, so the two grading runs produce identical files.
//
// Run it locally with:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, readFileSync } from "node:fs";
import { join } from "node:path";

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const here = new URL("./entry.png", import.meta.url);

// A PNG always starts with these eight bytes. Refuse anything else
// rather than silently copying a corrupt or wrong-format file.
const pngMagic = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
const image = readFileSync(here);
if (image.subarray(0, pngMagic.length).equals(pngMagic) === false) {
  throw new Error("entry.png does not start with the PNG signature");
}
if (image.length > 1048576) {
  throw new Error(`entry.png is ${image.length} bytes, over the 1 MiB limit`);
}

mkdirSync(outDir, { recursive: true });
copyFileSync(here, join(outDir, "entry.png"));
