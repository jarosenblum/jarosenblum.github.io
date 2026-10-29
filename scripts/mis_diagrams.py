# Generates the MIS 302F diagrams in assets/snapshots/mis302f-assessment-engine/.
# Paths below point at the build machine; adjust before re-running.
"""Render MIS 302F diagrams as SVG (site palette) and wrap them in an HTML page
that loads the site's self-hosted fonts, for PNG capture with Playwright."""
import pathlib, html

OUT = pathlib.Path(__file__).parent
FONTS = pathlib.Path("/home/claude/jarosenblum.github.io/assets/fonts")

PAPER, SURF, INK, INK2, RULE, COBALT, MARKER = "#f6f7f9", "#ffffff", "#1e2342", "#4b5272", "#d4d8e2", "#2341b0", "#f4d03f"
COWORK_T, PY_T, YOU_T = "#e8ecfa", "#ffffff", "#fff4c2"   # lane tints

def t(x, y, s, size=22, w=400, fill=INK, anchor="start", italic=False):
    st = ' font-style="italic"' if italic else ""
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{anchor}"{st}>{html.escape(s)}</text>'

def box(x, y, w, h, fill=SURF, stroke=INK, sw=2, rx=8, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'

def arrow(x1, y1, x2, y2, color=INK, sw=2.5):
    return f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{color}" stroke-width="{sw}" fill="none" marker-end="url(#ah)"/>'

def diamond(cx, cy, r, fill=MARKER):
    return f'<path d="M{cx} {cy-r} L{cx+r} {cy} L{cx} {cy+r} L{cx-r} {cy} Z" fill="{fill}" stroke="{INK}" stroke-width="2"/>'

DEFS = f'<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{INK}"/></marker></defs>'

def svg(body, w=1600, h=1000, label=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{html.escape(label)}" '
            f'font-family="Atkinson Hyperlegible Next, Atkinson Hyperlegible, system-ui, sans-serif">{DEFS}'
            f'<rect width="{w}" height="{h}" fill="{PAPER}"/>{body}</svg>')

# ---------------------------------------------------------------- 02: architecture map
def architecture():
    b = []
    b.append(t(60, 70, "Nine agents, three kinds of work, four stops for my review", 36, 800))
    b.append(t(60, 108, "MIS 302F exam pipeline: who does each stage, what it hands on, and where it waits for me", 22, 400, INK2))
    b.append(box(60, 132, 1480, 58, SURF, RULE, 2))
    b.append(t(84, 168, "Loaded first by every agent:", 20, 600))
    b.append(t(372, 168, "a constitution and 7 stage contracts  ·  5 data schemas  ·  a 15-task library for Claude Cowork", 20, 400, INK2))
    lanes = [("Claude Cowork", "judgment", 214, COWORK_T), ("Python", "deterministic", 444, PY_T), ("Me", "review", 674, YOU_T)]
    for name, sub, y, tint in lanes:
        b.append(box(60, y, 1480, 214, tint, RULE, 1.5, 6))
        b.append(t(80, y + 34, name, 22, 800))
        b.append(t(80, y + 60, sub, 18, 400, INK2))
    W, H = 140, 112
    cols = [250 + i * 161 for i in range(8)]
    st = [
        (0, 1, ["Ingest"], "ingest", "ingestion record"),
        (1, 0, ["Read", "transcripts"], "transcript_processor", "evidence"),
        (2, 0, ["Map", "topics"], "topic_mapper", "topic map"),
        (3, 1, ["Build", "blueprint"], "blueprint_builder", "draft blueprint"),
        (4, 0, ["Write", "questions"], "question_generator", "Forms A and B"),
        (5, 0, ["5 judgment", "audits"], "governance_auditor", "audit reports"),
        (6, 1, ["Lock", "the set"], "canonical_lock", "lock manifest"),
        (7, 1, ["Export"], "qti_exporter", "8 QTI packages"),
    ]
    lane_y = {0: 214, 1: 444, 2: 674}
    centers = {}
    def stage(x, y, title, agent, out):
        b.append(box(x, y, W, H, SURF, INK, 2))
        if len(title) == 1:
            b.append(t(x + W/2, y + 34, title[0], 18, 700, INK, "middle"))
        else:
            b.append(t(x + W/2, y + 26, title[0], 18, 700, INK, "middle"))
            b.append(t(x + W/2, y + 47, title[1], 18, 700, INK, "middle"))
        b.append(t(x + W/2, y + 74, agent, 12.5, 400, COBALT, "middle"))
        b.append(t(x + W/2, y + 98, "→ " + out, 14, 400, INK2, "middle"))
    for i, lane, title, agent, out in st:
        x = cols[i]; y = lane_y[lane] + 52
        stage(x, y, title, agent, out); centers[i] = (x, y)
    stage(cols[5], lane_y[1] + 52, ["3 rule", "audits"], "governance_auditor", "audit reports")
    def edge(a, bb):
        (xa, ya), (xb, yb) = centers[a], centers[bb]
        if ya == yb:
            return arrow(xa + W, ya + H/2, xb - 3, yb + H/2)
        mx = xa + W + 10
        return f'<path d="M{xa+W} {ya+H/2} H{mx} V{yb+H/2} H{xb-3}" stroke="{INK}" stroke-width="2.5" fill="none" marker-end="url(#ah)"/>'
    for a in range(7):
        b.append(edge(a, a + 1))
    b.append(box(60, 522, 172, 128, SURF, INK, 1.5, 8, "6 5"))
    for k, line in enumerate(["Lecture transcripts", "In-class polls", "Slides and demos", "Assigned reading", "Past exams"]):
        b.append(t(74, 546 + k * 23, line, 15, 400, INK))
    gates = [(1, 0, ["Review flagged", "segments"]), (2, 0, ["Review flagged", "topics"]), (3, 1, ["Approve the", "blueprint"]), (5, 1, ["Resolve blocking", "findings"])]
    gy = lane_y[2] + 92
    for i, lane, label in gates:
        cx = cols[i] + W / 2
        top = lane_y[lane] + 52 + H
        b.append(f'<path d="M{cx} {top} V{gy - 30}" stroke="{INK}" stroke-width="2" stroke-dasharray="5 5" fill="none"/>')
        b.append(diamond(cx, gy, 26))
        b.append(t(cx, gy + 54, label[0], 15, 700, INK, "middle"))
        b.append(t(cx, gy + 74, label[1], 15, 700, INK, "middle"))
    b.append(t(60, 950, "Agent names are the pipeline's own. No agent can skip ahead: each checks that the step before it finished, and every hand-off is a file checked against its schema.", 17, 400, INK2))
    return svg("".join(b), label="MIS 302F exam pipeline architecture: nine agents across Claude Cowork and Python lanes, with four stops for instructor review")

# ---------------------------------------------------------------- 01: thumbnail
def thumbnail():
    b = []
    b.append(t(80, 150, "Lecture → exam,", 92, 800))
    b.append(t(80, 255, "with four stops for my review", 64, 800, INK2))
    steps = ["Ingest", "Evidence", "Topics", "Blueprint", "Questions", "Audits", "Lock", "Export"]
    lane = [1, 0, 0, 1, 0, 0, 1, 1]
    ys = {0: 420, 1: 620}
    b.append(box(60, 380, 1480, 170, COWORK_T, RULE, 1.5, 6)); b.append(t(1520, 538, "Claude Cowork", 26, 700, INK2, "end"))
    b.append(box(60, 580, 1480, 170, PY_T, RULE, 1.5, 6));    b.append(t(1520, 738, "Python", 26, 700, INK2, "end"))
    b.append(box(60, 780, 1480, 150, YOU_T, RULE, 1.5, 6));   b.append(t(1520, 916, "Me", 26, 700, INK2, "end"))
    xs = [100 + i * 172 for i in range(8)]
    prev = None
    for i, (s_, l) in enumerate(zip(steps, lane)):
        x, y = xs[i], ys[l]
        b.append(box(x, y, 156, 90, SURF, INK, 3, 10))
        b.append(t(x + 78, y + 56, s_, 27, 700, INK, "middle"))
        if prev:
            px, py = prev
            if py == y: b.append(arrow(px + 156, py + 45, x - 4, y + 45, INK, 3))
            else: b.append(f'<path d="M{px+156} {py+45} H{px+164} V{y+45} H{x-4}" stroke="{INK}" stroke-width="3" fill="none" marker-end="url(#ah)"/>')
        prev = (x, y)
    for i in (1, 2, 3, 5):
        cx = xs[i] + 78
        b.append(diamond(cx, 855, 34))
    return svg("".join(b), label="MIS 302F exam pipeline overview: eight stages across Claude Cowork and Python, with four stops for instructor review")

# ---------------------------------------------------------------- 03: audit gate
def audit_gate():
    b = []
    b.append(t(60, 70, "Nothing is locked until every blocking finding is resolved", 40, 800))
    b.append(t(60, 108, "Five audits need judgment and run in Claude Cowork; three are rule checks in Python. A blocking finding stops the run until I review it.", 21, 400, INK2))
    judg = ["Structural fairness", "Test-wiseness", "Distractor efficiency", "Content accuracy", "Transcript alignment"]
    rule = ["Answer distribution", "Blueprint compliance", "QTI integrity"]
    b.append(box(60, 150, 520, 470, COWORK_T, RULE, 1.5, 6)); b.append(t(84, 188, "Claude Cowork · judgment", 22, 800))
    for k, a in enumerate(judg):
        y = 210 + k * 80
        b.append(box(84, y, 472, 62, SURF, INK, 2)); b.append(t(108, y + 40, a, 22, 600))
    b.append(box(60, 650, 520, 310, PY_T, RULE, 1.5, 6)); b.append(t(84, 688, "Python · rules", 22, 800))
    for k, a in enumerate(rule):
        y = 710 + k * 80
        b.append(box(84, y, 472, 62, SURF, INK, 2)); b.append(t(108, y + 40, a, 22, 600))
    # converge
    for k in range(5): b.append(f'<path d="M556 {241 + k*80} H660" stroke="{INK}" stroke-width="2" fill="none"/>')
    for k in range(3): b.append(f'<path d="M556 {741 + k*80} H660" stroke="{INK}" stroke-width="2" fill="none"/>')
    b.append(f'<path d="M660 241 V901" stroke="{INK}" stroke-width="2" fill="none"/>')
    b.append(arrow(660, 560, 790, 560, INK, 3))
    b.append(diamond(880, 560, 90))
    b.append(t(880, 553, "Any blocking", 19, 800, INK, "middle")); b.append(t(880, 579, "findings?", 19, 800, INK, "middle"))
    # yes path
    b.append(arrow(970, 560, 1110, 560, INK, 3)); b.append(t(1040, 540, "no", 20, 600, INK2, "middle"))
    b.append(box(1110, 500, 200, 120, SURF, INK, 3)); b.append(t(1210, 552, "Lock the set", 24, 800, INK, "middle")); b.append(t(1210, 584, "Python freezes it", 18, 400, INK2, "middle"))
    b.append(arrow(1310, 560, 1370, 560, INK, 3))
    b.append(box(1370, 500, 170, 120, COBALT, COBALT, 3)); b.append(t(1455, 552, "Export", 24, 800, "#ffffff", "middle")); b.append(t(1455, 584, "8 QTI packages", 18, 400, "#ffffff", "middle"))
    # no path -> repair -> back
    b.append(f'<path d="M880 650 V800" stroke="{INK}" stroke-width="3" fill="none" marker-end="url(#ah)"/>'); b.append(t(900, 730, "yes", 20, 600, INK2))
    b.append(box(780, 800, 200, 100, YOU_T, INK, 2)); b.append(t(880, 840, "I review", 24, 800, INK, "middle")); b.append(t(880, 870, "repair or override", 18, 400, INK2, "middle"))
    b.append(f'<path d="M780 850 H700 V600" stroke="{INK}" stroke-width="2.5" stroke-dasharray="7 6" fill="none" marker-end="url(#ah)"/>')
    return svg("".join(b), label="MIS 302F audit gate: five judgment audits in Claude Cowork and three rule audits in Python; any blocking finding stops the run for instructor review before the set is locked and exported")

for name, fn in [("01-overview", thumbnail), ("02-architecture", architecture), ("03-audit-gate", audit_gate)]:
    (OUT / f"{name}.svg").write_text(fn(), encoding="utf-8")

faces = "".join(
    f'@font-face{{font-family:"Atkinson Hyperlegible Next";font-weight:{w};src:url("file://{FONTS}/atkinson-hyperlegible-next-latin-{w}-normal.woff2")}}'
    for w in (400, 600, 800))
for name in ("01-overview", "02-architecture", "03-audit-gate"):
    (OUT / f"{name}.html").write_text(
        f'<!doctype html><meta charset="utf-8"><style>{faces}html,body{{margin:0}}</style>' + (OUT / f"{name}.svg").read_text(encoding="utf-8"),
        encoding="utf-8")
print("written")
