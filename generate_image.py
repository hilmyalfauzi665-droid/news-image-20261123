#!/usr/bin/env python3
"""Draw the entry image for make.fun news-image-20261123.

A newspaper front page summing up Monday 23 November 2026, drawn from
scratch with Pillow: no photographs, no copied art, only shapes and text.
Every story was verified against news reports dated 23 November 2026
(events that happened, or were first reported, on that day):

  1. Belgium's national strike grounds all flights, 07:00-21:00 (AFP).
  2. Modi meets Nepal PM Balen Shah in Delhi, first in-person talks (The Hindu).
  3. Nations agree to keep negotiating curbs on lethal AI weapons (UN).
  4. Paolo Bulgari dies at 89 (Economic Times, 23 Nov).
  Footer: Bank of Korea rate-hike preview; India's oil import bill +60%;
  India-Nepal bridge and rail link inaugurations.

Run: python3 generate_image.py  ->  writes entry.png (1024x1024).
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 243, 230)
INK = (20, 20, 20)
RED = (163, 22, 33)
BLUE = (31, 58, 95)
GREY = (85, 85, 85)
LIGHT_RULE = (120, 110, 90)

F_DIR = "/usr/share/fonts/truetype/dejavu/"
SERIF_B = F_DIR + "DejaVuSerif-Bold.ttf"
SERIF = F_DIR + "DejaVuSerif.ttf"
SANS = F_DIR + "DejaVuSans.ttf"
SANS_B = F_DIR + "DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Split text into lines that fit max_w pixels."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, max_w, text, fnt, fill=INK, leading=6):
    """Draw a wrapped paragraph; return the y just below it."""
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + leading
    return y


def rule(draw, x0, x1, y, width=2, fill=INK):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def kicker(draw, x, y, text):
    f = font(SANS_B, 17)
    draw.text((x, y), text, font=f, fill=RED)
    return y + 24


def headline(draw, x, y, max_w, text, size):
    f = font(SERIF_B, size)
    return para(draw, x, y, max_w, text, f, leading=2)


def draw_plane(draw, cx, cy, scale, body=BLUE):
    """Simple side-view airliner silhouette, nose pointing right."""
    s = scale
    # fuselage
    draw.rounded_rectangle(
        [cx - 150 * s, cy - 26 * s, cx + 150 * s, cy + 26 * s],
        radius=26 * s, fill=body)
    # nose
    draw.polygon([(cx + 140 * s, cy - 24 * s), (cx + 185 * s, cy),
                  (cx + 140 * s, cy + 24 * s)], fill=body)
    # tail fin
    draw.polygon([(cx - 150 * s, cy - 20 * s), (cx - 105 * s, cy - 20 * s),
                  (cx - 125 * s, cy - 85 * s), (cx - 150 * s, cy - 85 * s)],
                 fill=body)
    # main wing (down)
    draw.polygon([(cx - 30 * s, cy + 20 * s), (cx + 40 * s, cy + 20 * s),
                  (cx + 95 * s, cy + 78 * s), (cx + 55 * s, cy + 78 * s)],
                 fill=body)
    # rear stabiliser
    draw.polygon([(cx - 140 * s, cy + 20 * s), (cx - 100 * s, cy + 20 * s),
                  (cx - 70 * s, cy + 55 * s), (cx - 100 * s, cy + 55 * s)],
                 fill=body)
    # windows
    for i in range(7):
        wx = cx - 105 * s + i * 30 * s
        draw.ellipse([wx, cy - 12 * s, wx + 12 * s, cy + 2 * s],
                     fill=(220, 230, 240))
    # wheels
    draw.ellipse([cx - 60 * s, cy + 26 * s, cx - 44 * s, cy + 42 * s], fill=INK)
    draw.ellipse([cx + 60 * s, cy + 26 * s, cx + 76 * s, cy + 42 * s], fill=INK)


def draw_flags(draw, x, y, w, h):
    """Two small simplified flags: India (left) and Nepal (right)."""
    # India: saffron / white / green horizontal bands
    fw, fh = w // 2 - 8, h
    draw.rectangle([x, y, x + fw, y + fh // 3], fill=(255, 153, 51))
    draw.rectangle([x, y + fh // 3, x + fw, y + 2 * fh // 3], fill=(255, 255, 255))
    draw.rectangle([x, y + 2 * fh // 3, x + fw, y + fh], fill=(19, 136, 8))
    draw.ellipse([x + fw // 2 - 9, y + fh // 2 - 9, x + fw // 2 + 9,
                  y + fh // 2 + 9], outline=(0, 0, 128), width=2)
    # Nepal: crimson double pennant, simplified as two triangles
    nx = x + fw + 16
    draw.polygon([(nx, y), (nx + fw, y + fh // 2), (nx, y + fh // 2)],
                 fill=(220, 20, 60))
    draw.polygon([(nx, y + fh // 2), (nx + fw, y + fh), (nx, y + fh)],
                 fill=(220, 20, 60))
    draw.line([(nx, y), (nx, y + fh)], fill=(0, 0, 139), width=3)


def draw_robot(draw, x, y, w, h):
    """Simple robot head: rounded square, antenna, eyes, grill mouth."""
    draw.rounded_rectangle([x, y + 14, x + w, y + h], radius=10,
                           outline=BLUE, width=4)
    draw.line([(x + w // 2, y + 14), (x + w // 2, y)], fill=BLUE, width=4)
    draw.ellipse([x + w // 2 - 6, y - 6, x + w // 2 + 6, y + 6],
                 fill=RED)
    draw.ellipse([x + 14, y + 34, x + 34, y + 54], fill=BLUE)
    draw.ellipse([x + w - 34, y + 34, x + w - 14, y + 54], fill=BLUE)
    for i in range(3):
        gx = x + 22 + i * 18
        draw.line([(gx, y + h - 18), (gx, y + h - 8)], fill=BLUE, width=3)


def draw_gem(draw, x, y, w, h):
    """A cut diamond: crown facets above, pavilion below."""
    top = y + 6
    mid = y + h // 2
    bot = y + h - 4
    cx = x + w // 2
    draw.polygon([(x, mid), (x + 14, top), (cx, top), (x + w - 14, top),
                  (x + w, mid), (cx, bot)], outline=BLUE, width=3)
    draw.line([(x, mid), (x + w, mid)], fill=BLUE, width=2)
    draw.line([(x + 14, top), (cx - 18, mid)], fill=BLUE, width=2)
    draw.line([(x + w - 14, top), (cx + 18, mid)], fill=BLUE, width=2)
    draw.line([(cx, top), (cx, mid)], fill=BLUE, width=2)
    draw.line([(cx - 18, mid), (cx, bot)], fill=BLUE, width=2)
    draw.line([(cx + 18, mid), (cx, bot)], fill=BLUE, width=2)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 36                      # page margin
    R = W - M                   # right edge

    # ---------- masthead ----------
    y = 26
    f_top = font(SANS_B, 16)
    top = "MONDAY, 23 NOVEMBER 2026"
    d.text(((W - d.textlength(top, font=f_top)) / 2, y), top,
           font=f_top, fill=INK)
    y += 26
    f_mast = font(SERIF_B, 62)
    mast = "THE WORLD IN ONE DAY"
    d.text(((W - d.textlength(mast, font=f_mast)) / 2, y), mast,
           font=f_mast, fill=INK)
    y += 78
    f_tag = font(SANS, 16)
    tag = "ONE DAY  •  ONE PAGE  •  THE WHOLE WORLD"
    d.text(((W - d.textlength(tag, font=f_tag)) / 2, y), tag,
           font=f_tag, fill=GREY)
    y += 30
    rule(d, M, R, y, width=4)
    rule(d, M, R, y + 6, width=1)

    # ---------- lead story: Belgium grounded ----------
    y += 18
    lead_top = y
    lx, lw = M, 600
    y = kicker(d, lx, y, "EUROPE  —  TRANSPORT")
    y = headline(d, lx, y, lw, "BELGIUM GROUNDED", 76)
    y += 6
    f_sub = font(SANS_B, 23)
    y = para(d, lx, y, lw,
             "A national strike shuts the country's skies: no commercial "
             "flights from 7am to 9pm.",
             f_sub, leading=4)
    y += 8
    f_body = font(SERIF, 19)
    y = para(d, lx, y, lw,
             "Brussels Airport cancelled every departure and arrival in the "
             "14-hour window — about 429 flights carrying 59,500 "
             "passengers. Air-traffic controllers joined a nationwide "
             "walkout against austerity plans; only emergency flights kept "
             "flying.",
             f_body, leading=5)

    # lead illustration: grounded plane under a red no-flights sign
    ix0, iy0, ix1, iy1 = M + 636, lead_top, R, lead_top + 300
    d.rectangle([ix0, iy0, ix1, iy1], outline=INK, width=2)
    pcx, pcy = (ix0 + ix1) // 2, iy0 + 112
    draw_plane(d, pcx, pcy, 0.85)
    d.ellipse([pcx - 92, pcy - 92, pcx + 92, pcy + 92], outline=RED, width=9)
    d.line([(pcx - 65, pcy + 65), (pcx + 65, pcy - 65)], fill=RED, width=9)
    f_board = font(SANS_B, 24)
    board = "NO FLIGHTS TODAY"
    d.text(((ix0 + ix1 - d.textlength(board, font=f_board)) / 2, iy0 + 258),
           board, font=f_board, fill=RED)

    y = max(y, iy1 + 14)
    rule(d, M, R, y, width=2)
    y += 14

    # ---------- three secondary stories ----------
    cols = [(M, 300), (M + 332, 300), (M + 664, 316)]
    stories = [
        ("SOUTH ASIA  —  DIPLOMACY",
         "MODI MEETS NEPAL'S BALEN SHAH",
         "The two prime ministers hold their first in-person talks in "
         "Delhi — energy, hydropower, rail links and connectivity on the "
         "agenda.",
         draw_flags),
        ("UNITED NATIONS  —  ARMS",
         "TALKS GO ON OVER KILLER ROBOTS",
         "Nations agree to keep negotiating curbs on lethal autonomous "
         "weapons at the UN conference.",
         draw_robot),
        ("OBITUARY",
         "PAOLO BULGARI DIES AT 89",
         "The jeweller who helped turn the family house into a global "
         "luxury name has died in Rome. He was 89.",
         draw_gem),
    ]
    col_bottom = y
    for (cx, cw), (kick, head, body, icon) in zip(cols, stories):
        cy = y
        icon(d, cx + 4, cy, 56, 56)
        cy += 62
        cy = kicker(d, cx, cy, kick)
        cy = headline(d, cx, cy, cw, head, 27)
        cy += 4
        cy = para(d, cx, cy, cw, body, font(SERIF, 17), leading=4)
        col_bottom = max(col_bottom, cy)
    y = col_bottom + 12
    rule(d, M, R, y, width=2)
    y += 12

    # ---------- footer: also today ----------
    f_also = font(SANS_B, 17)
    d.text((M, y), "ALSO TODAY", font=f_also, fill=RED)
    y += 28
    briefs = [
        "Bank of Korea tipped to lift its rate to 3.25% on Thursday — "
        "the highest in two years — as chip exports drive growth.",
        "India's oil and gas import bill jumps 60% in October as Brent "
        "crude surges.",
        "India–Nepal: a new bridge at Dharchula and the Janakpur–Gorakhpur "
        "rail link open today.",
    ]
    f_brief = font(SERIF, 16)
    bx = M
    for i, b in enumerate(briefs):
        bw = 300 if i < 2 else 316
        para(d, bx, y, bw, b, f_brief, leading=4)
        if i < 2:
            d.line([(bx + bw + 14, y), (bx + bw + 14, y + 66)],
                   fill=LIGHT_RULE, width=1)
        bx += 332 if i < 2 else 0
    y += 78
    rule(d, M, R, y, width=1, fill=LIGHT_RULE)
    y += 12
    f_foot = font(SANS, 15)
    foot = ("Every story above happened, or was first reported, on "
            "Monday, 23 November 2026.")
    d.text(((W - d.textlength(foot, font=f_foot)) / 2, y), foot,
           font=f_foot, fill=GREY)

    img.save("entry.png", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
