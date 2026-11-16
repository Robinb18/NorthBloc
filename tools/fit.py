# Lines the sketch-map layout up with the real rocks.
# 1) Each sector is moved (and for Shaftoe North, rotated/stretched) so it sits on the right group of rocks,
#    judged against satellite imagery and the rock outlines mapped in OpenStreetMap (osm_rocks.json, local metres).
# 2) Each boulder is then pulled onto the nearest mapped rock edge within SNAP metres, without overlapping others.
# Positions are still estimates: OSM does not map every boulder.
import json, math, os
HERE = os.path.dirname(os.path.abspath(__file__))
SNAP = 40

def similarity(a1, b1, a2, b2):
    """Transform taking a1->b1 and a2->b2 (rotation + uniform scale + shift)."""
    za, zb = complex(*a1), complex(*b1)
    k = (complex(*b2) - zb) / (complex(*a2) - za)
    def f(x, y):
        z = (complex(x, y) - za) * k + zb
        return z.real, z.imag, math.degrees(math.atan2(k.imag, k.real))
    return f

def shift(dx, dy):
    return lambda x, y: (x + dx, y + dy, 0.0)

SECTOR_FIT = {
    "rift":    shift(43, -281),     # east-west valley with trees, east side
    "north":   similarity((-262, 322), (-80, 165), (-100, 780), (140, 618)),  # NNE escarpment
    "central": shift(-8, -198),     # west-facing edge around Salter's Nick
    "western": shift(122, -265),    # rocks just east of Shaftoe Grange
    "summit":  shift(330, -120),    # main mass of rocks on the top
    "south":   shift(10, -30),      # southern escarpment above the A696
}

def _segments():
    rocks = json.load(open(os.path.join(HERE, "osm_rocks.json")))
    segs = []
    for _, kind, pts in rocks:
        axis = _axis(pts)
        for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
            segs.append((x1, y1, x2, y2, axis))
    return segs

def _axis(pts):
    """Direction of the long axis of a rock outline, in degrees."""
    n = len(pts); mx = sum(p[0] for p in pts) / n; my = sum(p[1] for p in pts) / n
    sxx = sum((p[0] - mx) ** 2 for p in pts); syy = sum((p[1] - my) ** 2 for p in pts)
    sxy = sum((p[0] - mx) * (p[1] - my) for p in pts)
    return math.degrees(0.5 * math.atan2(2 * sxy, sxx - syy))

def _nearest(segs, x, y):
    best = None
    for x1, y1, x2, y2, axis in segs:
        dx, dy = x2 - x1, y2 - y1
        L2 = dx * dx + dy * dy or 1e-9
        t = max(0, min(1, ((x - x1) * dx + (y - y1) * dy) / L2))
        px, py = x1 + t * dx, y1 + t * dy
        d = math.hypot(x - px, y - py)
        if best is None or d < best[0]:
            best = (d, px, py, axis)
    return best

def _norm(a):
    a = (a + 90) % 180 - 90
    return round(a)

def fit(boulders):
    """boulders: list of dicts with sector,x,y,w,h,rot,problems. Updates x,y,rot in place."""
    segs = _segments()
    for b in boulders:
        x, y, r = SECTOR_FIT[b["sector"]](b["x"], b["y"])
        b["x"], b["y"], b["rot"] = round(x), round(y), _norm(b["rot"] + r)
    placed = []
    for b in sorted(boulders, key=lambda b: -len(b["problems"])):
        rad = max(b["w"], b["h"]) / 2
        near = _nearest(segs, b["x"], b["y"])
        if near and near[0] <= SNAP:
            # try the nearest edge point, then slide along nearby points until it doesn't overlap
            cands = [(near[1], near[2], near[3])]
            for step in range(1, 9):
                for sgn in (1, -1):
                    a = math.radians(near[3])
                    cands.append((near[1] + sgn * step * 6 * math.cos(a), near[2] + sgn * step * 6 * math.sin(a), near[3]))
            for cx, cy, ang in cands:
                n2 = _nearest(segs, cx, cy)
                cx, cy = n2[1], n2[2]
                if all(math.hypot(cx - px, cy - py) >= rad + pr + 2 for px, py, pr in placed):
                    b["x"], b["y"], b["rot"] = round(cx), round(cy), _norm(n2[3])
                    break
        placed.append((b["x"], b["y"], rad))
    return boulders
