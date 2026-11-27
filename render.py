#!/usr/bin/env python3
"""Render the front page for 27 November 2026 as entry.png.

The program paints a 1024x1024 newspaper front page entirely in code
with Pillow: masthead and date line, a lead story with a flat-illustration
panel, six story cards with small pictogram panels, and a bottom news
ticker. No photographs or external artwork are used; every pixel is drawn
here from shapes and text.

Run: python3 render.py   (writes entry.png next to this file)
"""

import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024

PAPER = (248, 244, 233)
INK = (26, 26, 26)
RED = (179, 39, 30)
NAVY = (31, 58, 95)
GREY = (90, 86, 76)
LIGHT_RULE = (200, 192, 172)
SKY_TOP = (44, 62, 110)
SKY_MID = (214, 122, 64)
SKY_LOW = (247, 196, 120)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: font("DejaVuSerif.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)


def wrap(draw, text, fnt, max_width):
    """Split text into lines that fit max_width, word by word."""
    lines, current = [], ""
    for word in text.split():
        trial = (current + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_lines(draw, lines, x, y, fnt, fill, leading):
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def rule(draw, x0, y, x1, width=2, fill=INK):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)

# ---------------------------------------------------------------------------
# Flat illustration panels. Every picture on the page is drawn from shapes.
# ---------------------------------------------------------------------------

def lead_panel(draw, x, y, w, h):
    """Dusk over the Gulf: Kuwait Towers, a radar dish and a drone."""
    # Banded dusk sky.
    bands = [SKY_TOP, (94, 84, 130), (176, 96, 84), SKY_MID, SKY_LOW]
    bh = h // len(bands) + 1
    for i, colour in enumerate(bands):
        draw.rectangle([x, y + i * bh, x + w, y + (i + 1) * bh], fill=colour)
    # Low sun.
    cx, cy, r = x + w - 78, y + 58, 26
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(250, 214, 130))
    # Sea at the bottom.
    draw.rectangle([x, y + h - 34, x + w, y + h], fill=(38, 74, 110))
    draw.line([x, y + h - 26, x + w, y + h - 26], fill=(120, 160, 200), width=2)
    draw.line([x, y + h - 16, x + w, y + h - 16], fill=(90, 130, 175), width=2)
    # Kuwait Towers silhouettes.
    base = y + h - 34
    for tx, th, tr in ((x + 52, 118, 17), (x + 108, 96, 14), (x + 156, 74, 11)):
        draw.rectangle([tx - 3, base - th, tx + 3, base], fill=(30, 30, 44))
        draw.ellipse([tx - tr, base - th - tr, tx + tr, base - th + tr],
                     fill=(30, 30, 44))
        draw.ellipse([tx - tr + 5, base - th - tr + 5, tx + tr - 5,
                      base - th + tr - 5], fill=(214, 122, 64))
    # Radar dish on a mast.
    mx = x + w - 150
    draw.rectangle([mx - 3, base - 66, mx + 3, base], fill=(30, 30, 44))
    draw.pieslice([mx - 34, base - 118, mx + 34, base - 50],
                  start=200, end=340, fill=(232, 228, 216))
    draw.line([mx, base - 84, mx + 26, base - 108], fill=(232, 228, 216),
              width=3)
    # Drone with a dotted flight path.
    dx, dy = x + 178, y + 42
    for i in range(7):
        px = x + 40 + i * 26
        py = y + 96 - i * 7
        draw.ellipse([px - 2, py - 2, px + 2, py + 2], fill=(250, 240, 210))
    draw.rectangle([dx - 22, dy - 6, dx + 22, dy + 6], fill=(20, 20, 30))
    draw.ellipse([dx - 30, dy - 9, dx - 14, dy - 3], fill=(20, 20, 30))
    draw.ellipse([dx + 14, dy - 9, dx + 30, dy - 3], fill=(20, 20, 30))
    draw.line([dx - 30, dy - 12, dx - 14, dy - 12], fill=(220, 220, 210),
              width=2)
    draw.line([dx + 14, dy - 12, dx + 30, dy - 12], fill=(220, 220, 210),
              width=2)
    # Blast starburst near the towers.
    bx, by = x + 128, base - 128
    for ang in range(0, 360, 30):
        import math
        ex = bx + int(20 * math.cos(math.radians(ang)))
        ey = by + int(20 * math.sin(math.radians(ang)))
        draw.line([bx, by, ex, ey], fill=(255, 196, 66), width=4)
    draw.ellipse([bx - 9, by - 9, bx + 9, by + 9], fill=(255, 220, 120))


def pic_storm(draw, x, y, w, h):
    """Thanksgiving storm: dark cloud, rain, lightning, a parade balloon."""
    draw.rectangle([x, y, x + w, y + h], fill=(58, 74, 102))
    draw.ellipse([x + 14, y + 22, x + 66, y + 62], fill=(40, 48, 70))
    draw.ellipse([x + 44, y + 12, x + 100, y + 56], fill=(40, 48, 70))
    draw.ellipse([x + 84, y + 26, x + 128, y + 62], fill=(40, 48, 70))
    draw.rectangle([x + 18, y + 52, x + 124, y + 64], fill=(40, 48, 70))
    for rx in (34, 58, 82, 106):
        draw.line([rx, y + 74, rx - 6, y + 96], fill=(140, 180, 230), width=3)
    draw.polygon([(x + 96, y + 78), (x + 80, y + 108), (x + 94, y + 108),
                  (x + 82, y + 132), (x + 108, y + 96), (x + 94, y + 96)],
                 fill=(255, 214, 64))
    draw.ellipse([x + 104, y + 108, x + 140, y + 138], fill=(214, 90, 70))
    draw.line([x + 122, y + 138, x + 122, y + 146], fill=(214, 90, 70),
              width=3)


def pic_dove(draw, x, y, w, h):
    """Gaza: a white dove over an olive branch."""
    draw.rectangle([x, y, x + w, y + h], fill=(232, 226, 205))
    draw.ellipse([x + 28, y + 52, x + 108, y + 92], fill=(255, 255, 250))
    draw.ellipse([x + 96, y + 34, x + 122, y + 60], fill=(255, 255, 250))
    draw.polygon([(x + 118, y + 44), (x + 136, y + 50), (x + 118, y + 56)],
                 fill=(240, 170, 40))
    draw.ellipse([x + 106, y + 40, x + 112, y + 46], fill=INK)
    draw.pieslice([x + 44, y + 30, x + 104, y + 84], start=200, end=330,
                  fill=(210, 210, 200))
    draw.line([x + 30, y + 96, x + 52, y + 118], fill=(255, 255, 250), width=3)
    draw.line([x + 52, y + 96, x + 74, y + 118], fill=(255, 255, 250), width=3)
    draw.line([x + 20, y + 128, x + 130, y + 112], fill=(96, 130, 62), width=4)
    for lx in (44, 68, 92, 114):
        draw.ellipse([lx, y + 104, lx + 16, y + 116], fill=(110, 148, 74))


def pic_chart(draw, x, y, w, h):
    """US economy: rising bars and an upward arrow."""
    draw.rectangle([x, y, x + w, y + h], fill=(31, 58, 95))
    base = y + h - 26
    for i, bh in enumerate((34, 52, 44, 74, 96)):
        bx = x + 18 + i * 24
        draw.rectangle([bx, base - bh, bx + 16, base], fill=(247, 196, 120))
    draw.line([x + 14, base - 100, x + 132, base - 118], fill=(255, 255, 255),
              width=4)
    draw.polygon([(x + 132, base - 118), (x + 118, base - 120),
                  (x + 130, base - 104)], fill=(255, 255, 255))
    draw.ellipse([x + 96, y + 14, x + 134, y + 52], fill=(255, 214, 64))
    draw.text((x + 108, y + 20), "$", font=SANS_B(24), fill=NAVY)


def pic_chess(draw, x, y, w, h):
    """World chess: a board and a king."""
    draw.rectangle([x, y, x + w, y + h], fill=(238, 230, 214))
    sq = 15
    ox, oy = x + 14, y + 26
    for r in range(8):
        for c in range(8):
            if (r + c) % 2 == 0:
                draw.rectangle([ox + c * sq, oy + r * sq,
                                ox + (c + 1) * sq, oy + (r + 1) * sq],
                               fill=(58, 52, 44))
    kx, ky = x + 108, y + 40
    draw.polygon([(kx - 12, ky + 44), (kx - 16, ky + 8), (kx - 6, ky + 20),
                  (kx, ky + 2), (kx + 6, ky + 20), (kx + 16, ky + 8),
                  (kx + 12, ky + 44)], fill=(214, 164, 32))
    draw.rectangle([kx - 14, ky + 44, kx + 14, ky + 54], fill=(214, 164, 32))
    draw.ellipse([kx - 4, ky - 6, kx + 4, ky + 2], fill=(214, 164, 32))


def pic_missile(draw, x, y, w, h):
    """Kyiv: a missile streaking over a shield."""
    draw.rectangle([x, y, x + w, y + h], fill=(70, 60, 66))
    draw.polygon([(x + 66, y + 18), (x + 86, y + 18), (x + 76, y + 66),
                  (x + 70, y + 78), (x + 62, y + 66)], fill=(226, 222, 210))
    draw.polygon([(x + 66, y + 18), (x + 76, y + 6), (x + 86, y + 18)],
                 fill=(179, 39, 30))
    draw.polygon([(x + 62, y + 66), (x + 52, y + 88), (x + 66, y + 74)],
                 fill=(179, 39, 30))
    draw.polygon([(x + 86, y + 66), (x + 96, y + 88), (x + 82, y + 74)],
                 fill=(179, 39, 30))
    for i in range(4):
        draw.ellipse([x + 70 - i, y + 86 + i * 10, x + 82 + i,
                      y + 96 + i * 10], fill=(255, 196, 66))
    draw.polygon([(x + 96, y + 96), (x + 134, y + 96), (x + 134, y + 118),
                  (x + 115, y + 142), (x + 96, y + 118)], fill=(31, 58, 95))
    draw.polygon([(x + 104, y + 104), (x + 126, y + 104), (x + 126, y + 116),
                  (x + 115, y + 130), (x + 104, y + 116)], fill=(247, 196, 120))


def pic_migration(draw, x, y, w, h):
    """UK migration: a falling line and a small plane."""
    draw.rectangle([x, y, x + w, y + h], fill=(214, 228, 226))
    draw.line([x + 16, y + 26, x + 132, y + 118], fill=(31, 58, 95), width=4)
    for px, py in ((28, 34), (58, 56), (88, 80), (118, 104)):
        draw.ellipse([x + px - 5, y + py - 5, x + px + 5, y + py + 5],
                     fill=(179, 39, 30))
    draw.polygon([(x + 118, y + 104), (x + 100, y + 106), (x + 116, y + 122)],
                 fill=(31, 58, 95))
    px, py = x + 30, y + 104
    draw.polygon([(px, py), (px + 44, py - 8), (px + 58, py - 4),
                  (px + 44, py + 2), (px + 52, py + 12), (px + 34, py + 8),
                  (px + 12, py + 10)], fill=(58, 58, 58))
    draw.line([x + 16, y + 132, x + 134, y + 132], fill=(120, 130, 125),
              width=2)

# ---------------------------------------------------------------------------
# The day's stories, checked against news reported on 27 November 2026.
# ---------------------------------------------------------------------------

LEAD = {
    "kicker": "THE GULF  •  LEAD STORY",
    "headline": "Drones kill two Italians in Kuwait as Iran denies any role",
    "standfirst": ("Two technicians for Rheinmetall Italia died at an air-defence "
                   "station hit by drones Kuwait blames on Iran. Tehran denies "
                   "involvement and calls the attack a fabrication."),
}

CARDS = [
    {
        "pic": pic_storm,
        "kicker": "UNITED STATES  •  WEATHER",
        "headline": "Thanksgiving storm blacks out 900,000 and grounds the parade",
        "standfirst": ("The 100th Macy's parade is postponed for the first time as "
                       "70 mph winds flood the East Coast and cancel hundreds "
                       "of flights."),
    },
    {
        "pic": pic_dove,
        "kicker": "GAZA  •  MIDDLE EAST",
        "headline": "Hamas weighs reply after Israeli strikes kill 10 in Gaza",
        "standfirst": ("The group considers its response as the ceasefire strains "
                       "and mediators press both sides to hold the truce."),
    },
    {
        "pic": pic_chart,
        "kicker": "UNITED STATES  •  ECONOMY",
        "headline": "US growth revised up to 4.3% as Trump attacks the figures",
        "standfirst": ("Third-quarter growth beats forecasts, but the president "
                       "demands a probe into what he calls \u201cfake\u201d GDP "
                       "numbers."),
    },
    {
        "pic": pic_chess,
        "kicker": "SPORT  •  CHESS",
        "headline": "Gukesh and Sindarov draw a marathon third game in Geneva",
        "standfirst": ("Nothing separates the champion and his challenger after "
                       "three games of the world title match."),
    },
    {
        "pic": pic_missile,
        "kicker": "UKRAINE  •  WAR",
        "headline": "Russia hits Kyiv with missiles as Zelensky faults US focus",
        "standfirst": ("The president tells the BBC Washington is too fixed on "
                       "the Middle East and not pressing Moscow hard enough."),
    },
    {
        "pic": pic_migration,
        "kicker": "BRITAIN  •  MIGRATION",
        "headline": "Net migration to UK falls to lowest level since 1997",
        "standfirst": ("The drop, excluding the pandemic years, comes as the "
                       "government tightens visas and asylum rules."),
    },
]

TICKER = ("ALSO TODAY:  Tanker capsizes off Ibiza, one dead  •  Depardieu to "
          "stand trial over alleged 2018 rape  •  Ebola in Congo passes "
          "12,000 cases  •  Nepal declares 4,000 landslide victims dead  •  "
          "Saudi Arabia intercepts Houthi missiles aimed at Riyadh")


def build():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    mx, mw = 36, W - 72  # margin and content width

    # Outer frame.
    d.rectangle([14, 14, W - 15, H - 15], outline=INK, width=2)
    d.rectangle([20, 20, W - 21, H - 21], outline=LIGHT_RULE, width=1)

    # Masthead.
    title = "THE DAILY GLOBE"
    tf = SERIF_B(68)
    d.text(((W - d.textlength(title, font=tf)) / 2, 30), title,
           font=tf, fill=INK)
    rule(d, mx, 118, mx + mw, 3)
    df = SANS_B(17)
    d.text((mx, 128), "FRIDAY, 27 NOVEMBER 2026", font=df, fill=INK)
    mid = "WORLD NEWS IN ONE IMAGE"
    d.text(((W - d.textlength(mid, font=df)) / 2, 128), mid, font=df,
           fill=RED)
    right = "No. 331"
    d.text((mx + mw - d.textlength(right, font=df), 128), right, font=df,
           fill=INK)
    rule(d, mx, 154, mx + mw, 1, LIGHT_RULE)
    rule(d, mx, 158, mx + mw, 2)

    # Lead story.
    y = 176
    d.text((mx, y), LEAD["kicker"], font=SANS_B(15), fill=RED)
    y += 26
    head_lines = wrap(d, LEAD["headline"], SERIF_B(38), 560)
    y = draw_lines(d, head_lines, mx, y, SERIF_B(38), INK, 46)
    y += 10
    lead_panel(d, 648, 176, 340, 236)
    stand_lines = wrap(d, LEAD["standfirst"], SERIF(19), 560)
    y = draw_lines(d, stand_lines, mx, y, SERIF(19), INK, 26)
    rule(d, mx, 458, mx + mw, 2)
    rule(d, mx, 462, mx + mw, 1, LIGHT_RULE)

    # Six story cards, two columns by three rows.
    cw, ch, gap = 466, 150, 20
    top = 470
    for i, card in enumerate(CARDS):
        cx = mx + (i % 2) * (cw + gap)
        cy = top + (i // 2) * (ch + 14)
        card["pic"](d, cx, cy, 140, 140)
        tx = cx + 152
        d.text((tx, cy + 2), card["kicker"], font=SANS_B(12), fill=RED)
        hl = wrap(d, card["headline"], SERIF_B(19), cw - 152)
        ny = draw_lines(d, hl, tx, cy + 24, SERIF_B(19), INK, 24)
        sl = wrap(d, card["standfirst"], SANS(13), cw - 152)
        draw_lines(d, sl, tx, ny + 4, SANS(13), (60, 58, 50), 18)
        if i % 2 == 0:
            d.line([(cx + cw + 10, cy + 4), (cx + cw + 10, cy + ch - 4)],
                   fill=LIGHT_RULE, width=1)

    # Bottom ticker.
    ty = 950
    d.rectangle([mx, ty, mx + mw, 1000], fill=NAVY)
    tick_lines = wrap(d, TICKER, SANS(13), mw - 24)
    draw_lines(d, tick_lines, mx + 12, ty + 7, SANS(13), (255, 255, 255), 18)
    return img


def main():
    img = build()
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "entry.png")
    img.save(out, format="PNG", optimize=True)
    size = os.path.getsize(out)
    print(f"wrote {out}: {img.size[0]}x{img.size[1]}, {size} bytes")
    assert img.size == (1024, 1024), "image must be 1024x1024"
    assert size <= 1048576, "image must be under 1 MiB"


if __name__ == "__main__":
    main()
