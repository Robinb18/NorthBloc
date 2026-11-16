# Writes TO-CHECK.md from data/shaftoe.json: every problem with a "check" note.
import json, sys, os
src = sys.argv[1] if len(sys.argv) > 1 else "app/data/shaftoe.json"
out = sys.argv[2] if len(sys.argv) > 2 else "TO-CHECK.md"
d = json.load(open(src))
L = ["# Shaftoe: problems to check", "",
     "These are the problems where the guidebook photo was unreadable (glare, the page shadow, or the page fold), "
     "or where the guidebook and Rockfax disagree. Each one is in the app with a yellow note and can be found with Filters → Needs checking.", ""]
for s in d["sectors"]:
    rows = [(b["name"], p) for b in s["boulders"] for p in b["problems"] if p.get("check")]
    if not rows: continue
    L += [f"## {s['name']}", "", "| Boulder | No. | Name in app | Grade in app | What to check |", "|---|---|---|---|---|"]
    L += [f"| {bn} | {p['number']} | {p['name'] or '(unnamed)'} | {p['grade']} | {p['check']} |" for bn, p in rows]
    L.append("")
open(out, "w").write("\n".join(L))
print(len([1 for s in d['sectors'] for b in s['boulders'] for p in b['problems'] if p.get('check')]), "to check")
