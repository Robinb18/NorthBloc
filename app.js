/* Northbloc: a bouldering map for Northumberland.
   Climb data lives in data/*.json, one file per crag, listed in data/crags.json. */
(function () {
  "use strict";

  // ---------- small helpers ----------
  const $ = (id) => document.getElementById(id);
  const esc = (s) => String(s == null ? "" : s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const norm = (s) => String(s || "").normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase().replace(/[’']/g, "'");
  const store = {
    get(k, d) { try { const v = localStorage.getItem("nb:" + k); return v == null ? d : JSON.parse(v); } catch (e) { return d; } },
    set(k, v) { try { localStorage.setItem("nb:" + k, JSON.stringify(v)); } catch (e) { /* storage unavailable */ } },
  };
  let toastTimer;
  function toast(msg, ms) {
    const t = $("toast"); t.textContent = msg; t.classList.add("show");
    clearTimeout(toastTimer); toastTimer = setTimeout(() => t.classList.remove("show"), ms || 3200);
  }
  const ICON = {
    star: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.8l2.8 6 6.5.7-4.9 4.4 1.4 6.4L12 17l-5.8 3.3 1.4-6.4-4.9-4.4 6.5-.7z"/></svg>',
    starO: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M12 2.8l2.8 6 6.5.7-4.9 4.4 1.4 6.4L12 17l-5.8 3.3 1.4-6.4-4.9-4.4 6.5-.7z"/></svg>',
    tick: '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" fill="#45d86f"/><path d="M7.5 12.3l3 3 6-6.3" fill="none" stroke="#0b1f10" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    tickO: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9.5"/><path d="M7.8 12.2l2.8 2.8 5.6-5.8"/></svg>',
    circuit: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-dasharray="2.5 2.5"><path d="M5 6h12a3 3 0 010 6H7a3 3 0 000 6h12"/><circle cx="4.5" cy="6" r="1.6" fill="currentColor" stroke-dasharray="0"/><circle cx="19.5" cy="18" r="1.6" fill="currentColor" stroke-dasharray="0"/></svg>',
    next: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 6l6 6-6 6"/></svg>',
    prev: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 6l-6 6 6 6"/></svg>',
    pin: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M12 21s-6.5-6.2-6.5-11.2a6.5 6.5 0 0113 0C18.5 14.8 12 21 12 21z"/><circle cx="12" cy="9.8" r="2.3"/></svg>',
    cam: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M4 7.5h3.2L9 5h6l1.8 2.5H20a1 1 0 011 1V18a1 1 0 01-1 1H4a1 1 0 01-1-1V8.5a1 1 0 011-1z"/><circle cx="12" cy="13" r="3.6"/></svg>',
    x: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>',
    ok: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>',
    warn: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linejoin="round"><path d="M12 3.5l9.5 16.5h-19z"/><path d="M12 10v4.5M12 17.2v.3" stroke-linecap="round"/></svg>',
    chev: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 5l7 7-7 7"/></svg>',
    sit: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="5" r="2"/><path d="M9 8v5h6l2 6M9 13l-4 6"/></svg>',
    trav: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12h18M7 8l-4 4 4 4M17 8l4 4-4 4"/></svg>',
    high: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21V3M7 8l5-5 5 5M5 21h14"/></svg>',
    jump: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 19c3-10 11-10 14 0"/><path d="M15 9l4-1-1 4"/></svg>',
    up: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M6 21l5-17 2 .6L8.3 21z"/><path d="M13 21l2.4-8 4.6 8z" opacity=".9"/><path d="M11.5 3.5l2 4.5-2.3-.8-1 2.2z"/></svg>',
    heart: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M12 20s-7.5-4.6-7.5-10A4.3 4.3 0 0112 7.3 4.3 4.3 0 0119.5 10c0 5.4-7.5 10-7.5 10z"/></svg>',
    bars: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3.5" y="12" width="4" height="8" rx="1"/><rect x="10" y="8" width="4" height="12" rx="1"/><rect x="16.5" y="4" width="4" height="16" rx="1"/></svg>',
    copy: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><rect x="8" y="8" width="12" height="12" rx="2"/><path d="M16 8V5a1 1 0 00-1-1H5a1 1 0 00-1 1v10a1 1 0 001 1h3"/></svg>',
    route: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="6" cy="18" r="2.2"/><circle cx="18" cy="6" r="2.2"/><path d="M8 18h7a3.5 3.5 0 000-7H9a3.5 3.5 0 010-7h7"/></svg>',
  };
  const LOGO = '<svg viewBox="0 0 64 64" aria-hidden="true"><rect width="64" height="64" rx="15" fill="#1d2a2f"/><path d="M10 46c3-12 9-22 19-25 6-2 10 1 14 4 5 3 9 9 11 21z" fill="#3b4b52"/><path d="M10 46c3-12 9-22 19-25 6-2 10 1 14 4 5 3 9 9 11 21z" fill="none" stroke="#7f939a" stroke-width="1.5"/><circle cx="44" cy="20" r="7" fill="#45d86f"/><text x="44" y="23.6" text-anchor="middle" font-family="Figtree,system-ui,sans-serif" font-size="10" font-weight="800" fill="#0b1f10">N</text></svg>';

  // ---------- grades and circuits ----------
  function gradeValue(g) {
    const m = /^(\d)([abc]?)(\+?)/.exec(g || "");
    if (!m) return -1;
    return (+m[1]) * 10 + ({ "": 0, a: 2, b: 4, c: 6 }[m[2]]) + (m[3] ? 1 : 0);
  }
  const LEVELS = [
    { id: "y", label: "Up to 4+", color: "yellow", test: (v) => v >= 0 && v < 50 },
    { id: "o", label: "5 to 5+", color: "orange", test: (v) => v >= 50 && v < 62 },
    { id: "b", label: "6a to 6b+", color: "blue", test: (v) => v >= 62 && v < 66 },
    { id: "r", label: "6c to 7a+", color: "red", test: (v) => v >= 66 && v < 74 },
    { id: "k", label: "7b and harder", color: "black", test: (v) => v >= 74 },
    { id: "u", label: "Grade unknown", color: "grey", test: (v) => v < 0 },
  ];
  const levelOf = (g) => { const v = gradeValue(g); return LEVELS.find((l) => l.test(v)); };

  // ---------- state ----------
  const S = {
    crags: [], problems: [], byUid: new Map(), boulders: new Map(), sectors: [],
    ticks: new Set(store.get("ticks", [])), projects: new Set(store.get("projects", [])),
    fixes: store.get("fixes", {}),
    filters: Object.assign({ levels: [], circuit: null, popular: false, project: false, ticked: false, check: false }, store.get("filters", {})),
    selected: null, me: null, editing: null,
  };
  const saveSets = () => { store.set("ticks", [...S.ticks]); store.set("projects", [...S.projects]); };

  // ---------- geometry (local metres around a point) ----------
  const M_LAT = 111320;
  const mLon = (lat) => 111320 * Math.cos(lat * Math.PI / 180);
  const toLL = (lat0, lon0, x, y) => [lat0 + y / M_LAT, lon0 + x / mLon(lat0)];
  function seeded(str) { let h = 2166136261; for (const c of str) { h ^= c.charCodeAt(0); h = Math.imul(h, 16777619); } return () => { h ^= h << 13; h ^= h >>> 17; h ^= h << 5; return ((h >>> 0) % 10000) / 10000; }; }
  // Rounded, slightly irregular boulder outline in local metres
  // Many problems on a small (estimated) boulder: draw it a bit bigger so the numbered dots fit around it
  function growth(b) {
    const n = b.problems.length, a = b.size[0] / 2 + 1.8, c = b.size[1] / 2 + 1.8;
    const span = n <= 7 ? Math.PI * 0.9 : Math.PI * 2 * Math.min(1, n / 16);
    const perim = Math.PI * (3 * (a + c) - Math.sqrt((3 * a + c) * (a + 3 * c)));
    const need = (n - 1) * 4, have = perim * span / (2 * Math.PI);
    return have < need ? Math.min(1.8, need / have) : 1;
  }
  function outline(b) {
    const rnd = seeded(b.id), n = 16, pts = [], g = growth(b);
    const a = b.size[0] / 2 * g, c = b.size[1] / 2 * g, rot = (b.rotation || 0) * Math.PI / 180;
    for (let i = 0; i < n; i++) {
      const t = (i / n) * Math.PI * 2;
      const ct = Math.cos(t), st = Math.sin(t);
      const k = 0.88 + rnd() * 0.22;
      // superellipse-ish so long walls look like walls
      const x = a * Math.sign(ct) * Math.pow(Math.abs(ct), 0.6) * k;
      const y = c * Math.sign(st) * Math.pow(Math.abs(st), 0.6) * k;
      pts.push([x * Math.cos(rot) - y * Math.sin(rot), x * Math.sin(rot) + y * Math.cos(rot)]);
    }
    return pts;
  }
  // Problem dot positions: spread along the south (front) edge left to right, wrapping round if there are many.
  function dotSpots(b, count) {
    const g = growth(b);
    let a = b.size[0] / 2 * g + 1.8, c = b.size[1] / 2 * g + 1.8;
    const rot = (b.rotation || 0) * Math.PI / 180, out = [];
    const span = count <= 7 ? Math.PI * 0.9 : Math.PI * 2 * Math.min(1, count / 16);
    // keep at least ~4.5 m between dots so numbers stay readable at close zoom
    const perim = Math.PI * (3 * (a + c) - Math.sqrt((3 * a + c) * (a + 3 * c)));
    const need = (count - 1) * 4, have = perim * span / (2 * Math.PI);
    if (have < need) { const f = need / have; a *= f; c *= f; }
    const start = Math.PI + (Math.PI - Math.min(span, Math.PI)) / 2 - (span > Math.PI ? (span - Math.PI) / 2 : 0);
    for (let i = 0; i < count; i++) {
      const t = start + (count === 1 ? span / 2 : (i / (count - 1)) * span);
      const ct = Math.cos(t), st = Math.sin(t);
      const x = a * Math.sign(ct) * Math.pow(Math.abs(ct), 0.6), y = c * Math.sign(st) * Math.pow(Math.abs(st), 0.6);
      out.push([x * Math.cos(rot) - y * Math.sin(rot), x * Math.sin(rot) + y * Math.cos(rot)]);
    }
    return out;
  }
  function hull(points) {
    const p = points.slice().sort((a, b) => a[0] - b[0] || a[1] - b[1]);
    const cross = (o, a, b) => (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0]);
    const lo = [], up = [];
    for (const q of p) { while (lo.length >= 2 && cross(lo[lo.length - 2], lo[lo.length - 1], q) <= 0) lo.pop(); lo.push(q); }
    for (let i = p.length - 1; i >= 0; i--) { const q = p[i]; while (up.length >= 2 && cross(up[up.length - 2], up[up.length - 1], q) <= 0) up.pop(); up.push(q); }
    up.pop(); lo.pop(); return lo.concat(up);
  }

  // ---------- data ----------
  async function loadData() {
    const idx = await (await fetch("data/crags.json", { cache: "no-cache" })).json();
    for (const file of idx.crags) {
      const crag = await (await fetch("data/" + file, { cache: "no-cache" })).json();
      S.crags.push(crag);
      for (const sec of crag.sectors) {
        sec.crag = crag; S.sectors.push(sec);
        for (const b of sec.boulders) {
          b.sector = sec; b.crag = crag; b.key = crag.id + "/" + b.id;
          b._orig = [b.lat, b.lon];
          const fx = S.fixes[b.key]; if (fx) { b.lat = fx.lat; b.lon = fx.lon; b.fixed = true; }
          S.boulders.set(b.key, b);
          for (const p of b.problems) {
            p.boulder = b; p.sector = sec; p.crag = crag;
            p.uid = b.key + "/" + p.number;
            p.gv = gradeValue(p.grade); p.level = levelOf(p.grade);
            p.label = p.name || "Problem " + p.number;
            p.search = norm(p.name + " " + b.name + " " + sec.name);
            S.problems.push(p); S.byUid.set(p.uid, p);
          }
        }
      }
    }
  }

  // ---------- map ----------
  const CRAG_Z = 14.5, BOULDER_Z = 16, NUM_Z = 19;
  const BASES = [
    { id: "dark", name: "Dark map", make: () => L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", { maxNativeZoom: 19, maxZoom: 22, className: "tiles-dark", attribution: '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors' }) },
    { id: "sat", name: "Satellite", make: () => L.tileLayer("https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}", { maxNativeZoom: 19, maxZoom: 22, attribution: "Imagery © Esri, Maxar, Earthstar Geographics" }) },
    { id: "none", name: "Boulders only", make: () => null },
  ];
  let map, baseLayer, baseIdx = Math.max(0, BASES.findIndex((b) => b.id === store.get("base", "dark")));
    let sectorLayer, sectorLabelLayer, cragLabelLayer, boulderLayer, dotLayer, boulderNameLayer, meLayer, editLayer;
  const dotMarkers = new Map();

  function setBase(i) {
    if (baseLayer) map.removeLayer(baseLayer);
    baseIdx = i; const b = BASES[i]; baseLayer = b.make();
    if (baseLayer) baseLayer.addTo(map).bringToBack();
    store.set("base", b.id);
  }

  function boulderLatLngs(b) { return outline(b).map(([x, y]) => toLL(b.lat, b.lon, x, y)); }

  function drawBoulder(b) {
    if (b._poly) boulderLayer.removeLayer(b._poly);
    b._poly = L.polygon(boulderLatLngs(b), { color: "#14182a", weight: 1, fillColor: "#232838", fillOpacity: 1, interactive: true, bubblingMouseEvents: false });
    b._poly.on("click", () => { const first = visibleProblems().find((p) => p.boulder === b) || b.problems[0]; if (first) selectProblem(first, false); });
    boulderLayer.addLayer(b._poly);
    if (b._name) boulderNameLayer.removeLayer(b._name);
    b._name = L.marker(toLL(b.lat, b.lon, 0, b.size[1] / 2 * growth(b) + 4.5), { interactive: false, icon: L.divIcon({ className: "", html: '<span class="lbl boulder">' + esc(b.name) + "</span>", iconSize: [0, 0] }) });
    boulderNameLayer.addLayer(b._name);
    const spots = dotSpots(b, b.problems.length);
    b.problems.forEach((p, i) => { p.ll = toLL(b.lat, b.lon, spots[i][0], spots[i][1]); });
  }

  function sectorHull(sec) {
    const pts = [];
    for (const b of sec.boulders) {
      const m = mLon(b.lat), r = Math.max(b.size[0], b.size[1]) / 2 + 14;
      for (let i = 0; i < 10; i++) { const t = i / 10 * Math.PI * 2; pts.push([b.lon + r * Math.cos(t) / m, b.lat + r * Math.sin(t) / M_LAT]); }
    }
    return hull(pts).map(([x, y]) => [y, x]);
  }
  function centroid(lls) { let a = 0, b = 0; lls.forEach((p) => { a += p[0]; b += p[1]; }); return [a / lls.length, b / lls.length]; }

  function drawSectors() {
    sectorLayer.clearLayers(); sectorLabelLayer.clearLayers();
    for (const sec of S.sectors) {
      const h = sectorHull(sec); sec.hull = h; sec.center = centroid(sec.boulders.map((b) => [b.lat, b.lon]));
      L.polygon(h, { stroke: true, color: "#1e2633", weight: 1, opacity: .5, fillColor: "#28313f", fillOpacity: .55, smoothFactor: 2 })
        .on("click", () => flyToSector(sec)).addTo(sectorLayer);
      L.marker(sec.center, { icon: L.divIcon({ className: "", html: '<span class="lbl sector">' + esc(sec.name) + "</span>", iconSize: [0, 0] }) })
        .on("click", () => flyToSector(sec)).addTo(sectorLabelLayer);
    }
  }

  function drawCragLabels() {
    cragLabelLayer.clearLayers();
    for (const c of S.crags) {
      L.marker([c.lat, c.lon], { icon: L.divIcon({ className: "", html: '<span class="lbl crag">' + esc(c.name) + "</span>", iconSize: [0, 0] }) })
        .on("click", () => map.flyTo([c.lat, c.lon], 15.5, { duration: .8 })).addTo(cragLabelLayer);
    }
  }

  function dotHtml(p, small) {
    const cls = ["dot", "c-" + p.level.color];
    if (small) cls.push("small");
    if (S.ticks.has(p.uid)) cls.push("ticked");
    if (S.projects.has(p.uid)) cls.push("proj");
    if (S.selected === p) cls.push("sel");
    return '<div class="' + cls.join(" ") + '">' + (small ? "" : esc(p.number)) + "</div>";
  }

  function filtersActive() { const f = S.filters; return f.levels.length || f.circuit || f.popular || f.project || f.ticked || f.check; }
  function passes(p) {
    const f = S.filters;
    if (f.levels.length && !f.levels.includes(p.level.id)) return false;
    if (f.circuit && p.sector.crag.id + "/" + p.sector.id !== f.circuit) return false;
    if (f.popular && !p.popular) return false;
    if (f.project && !S.projects.has(p.uid)) return false;
    if (f.ticked && !S.ticks.has(p.uid)) return false;
    if (f.check && !p.check) return false;
    return true;
  }
  const visibleProblems = () => S.problems.filter(passes);

  function drawDots() {
    dotLayer.clearLayers(); dotMarkers.clear();
    const small = map.getZoom() < NUM_Z;
    for (const p of S.problems) {
      if (!passes(p)) continue;
      const m = L.marker(p.ll, { icon: L.divIcon({ className: "", html: dotHtml(p, small), iconSize: [0, 0] }), zIndexOffset: S.selected === p ? 1000 : (p.level.id === "u" ? 0 : 10) });
      m.on("click", (e) => { L.DomEvent.stopPropagation(e); selectProblem(p, false); });
      dotLayer.addLayer(m); dotMarkers.set(p.uid, m);
    }
    $("filterDot").hidden = !filtersActive();
  }

  function onZoom() {
    const z = map.getZoom();
    const show = (layer, on) => { if (on && !map.hasLayer(layer)) layer.addTo(map); if (!on && map.hasLayer(layer)) map.removeLayer(layer); };
    show(cragLabelLayer, z < CRAG_Z - .5);
    show(sectorLayer, z >= 12.5 && z < 18);
    show(sectorLabelLayer, z >= CRAG_Z - .5 && z < 17.5);
    show(boulderLayer, z >= BOULDER_Z - .5);
    show(boulderNameLayer, z >= 19);
    show(dotLayer, z >= BOULDER_Z);
    const small = z < NUM_Z;
    if (small !== onZoom._small) { onZoom._small = small; drawDots(); }
    const inCrag = z >= CRAG_Z;
    $("searchPill").hidden = inCrag; $("searchRound").hidden = !inCrag; $("areaPill").hidden = !inCrag;
    updateAreaName();
  }

  function nearestSector() {
    // the area of the boulder closest to the middle of the screen
    const c = map.getCenter(); let best = null, bd = Infinity;
    for (const b of S.boulders.values()) { const d = map.distance(c, [b.lat, b.lon]); if (d < bd) { bd = d; best = b.sector; } }
    return { sector: best, dist: bd };
  }
  function updateAreaName() {
    if (!S.sectors.length) return;
    const { sector, dist } = nearestSector();
    const z = map.getZoom();
    $("areaName").textContent = z >= 15.5 && dist < 400 ? sector.name : (sector ? sector.crag.name : "Northumberland");
  }

  function flyToSector(sec) {
    const b = L.latLngBounds(sec.hull);
    map.flyToBounds(b, { paddingTopLeft: [20, 90], paddingBottomRight: [20, 120], maxZoom: 18.5, duration: .8 });
  }

  // ---------- problem sheet ----------
  const photoUrls = new Map();
  function openSheet(id) { closeSheets(id); const el = $(id); el.classList.add("open"); el.setAttribute("aria-hidden", "false"); }
  function closeSheets(except) {
    for (const id of ["problemSheet", "filterSheet", "infoSheet"]) {
      if (id === except) continue; const el = $(id); el.classList.remove("open"); el.setAttribute("aria-hidden", "true");
    }
    if (except !== "problemSheet" && S.selected) { const p = S.selected; S.selected = null; refreshDot(p); }
  }
  function refreshDot(p) {
    const m = dotMarkers.get(p.uid); if (!m) return;
    m.setIcon(L.divIcon({ className: "", html: dotHtml(p, map.getZoom() < NUM_Z), iconSize: [0, 0] }));
    m.setZIndexOffset(S.selected === p ? 1000 : 10);
  }
  function circuitList(p) { return p.sector.boulders.flatMap((b) => b.problems).filter(passes); }

  function selectProblem(p, fly) {
    const prev = S.selected; S.selected = p; if (prev) refreshDot(prev); refreshDot(p);
    renderProblem(p);
    openSheet("problemSheet");
    const sheetH = $("problemSheet").offsetHeight || window.innerHeight * .6;
    const targetZoom = Math.max(map.getZoom(), NUM_Z + .75);
    const pt = map.project(p.ll, targetZoom);
    const H = map.getSize().y, top = 80;
    const offsetY = H / 2 - (top + Math.max(60, H - sheetH - top) / 2);
    const center = map.unproject(pt.add([0, offsetY]), targetZoom);
    if (fly) map.flyTo(center, targetZoom, { duration: .7 }); else map.panTo(center, { animate: true });
  }

  async function photoFor(p) {
    if (photoUrls.has(p.uid)) return photoUrls.get(p.uid);
    const blob = await idbGet(p.uid);
    if (blob) { const u = URL.createObjectURL(blob); photoUrls.set(p.uid, u); return u; }
    if (p.photo) return p.photo;
    return null;
  }

  function styleBits(p) {
    const out = [];
    if (p.sitStart) out.push('<span>' + ICON.sit + "Sit start</span>");
    if (p.traverse) out.push('<span>' + ICON.trav + "Traverse</span>");
    if (p.highball) out.push('<span>' + ICON.high + "Highball</span>");
    if (p.jumpStart) out.push('<span>' + ICON.jump + "Jump start</span>");
    if (!out.length) out.push('<span>' + ICON.up + "Problem</span>");
    return out.join("");
  }

  async function renderProblem(p) {
    const el = $("problemSheet");
    const proj = S.projects.has(p.uid), ticked = S.ticks.has(p.uid);
    const list = circuitList(p); const i = list.indexOf(p);
    el.innerHTML =
      '<div class="photo" id="photoBox"><div class="empty">' +
        '<div class="circ">' + ICON.cam + "</div>" +
        "<div>No photo yet for this problem</div>" +
        '<button class="btn-white" id="addPhoto">Add a photo</button></div>' +
        '<button class="x glass" id="closeProblem" aria-label="Close">' + ICON.x + "</button></div>" +
      '<div class="card-body">' +
        '<div class="title-row"><div class="dot c-' + p.level.color + '">' + esc(p.number) + "</div>" +
          "<h2>" + (p.name ? esc(p.name) : '<span class="muted">Unnamed</span>') + "</h2>" +
          '<div class="grade">' + esc(p.grade === "?" ? "–" : p.grade) + "</div></div>" +
        '<div class="meta">' + styleBits(p) + "</div>" +
        '<div class="where">' + esc(p.boulder.name) + " · " + esc(p.sector.name) + " · " + esc(p.crag.name) + "</div>" +
        (p.description ? '<p class="desc">' + esc(p.description) + "</p>" : "") +
        (p.check ? '<div class="check">' + ICON.warn + "<div><b>Check this one:</b> " + esc(p.check) + ". The guidebook photo was unreadable here.</div></div>" : "") +
        (p.boulder.positionEstimated && !p.boulder.fixed ? '<div class="where">' + ICON.pin.replace("<svg", '<svg style="width:15px;height:15px;vertical-align:-2px"') + " Position on the map is estimated. Use Fix position when you are there.</div>" : "") +
        '<div class="actions">' +
          '<button class="act ' + (proj ? "on-star" : "") + '" id="btnProj">' + (proj ? ICON.star : ICON.starO) + (proj ? "Project" : "Save") + "</button>" +
          '<button class="act ' + (ticked ? "on-tick" : "") + '" id="btnTick">' + (ticked ? ICON.tick : ICON.tickO) + (ticked ? "Ticked" : "Tick") + "</button>" +
          '<button class="act" id="btnPrev" aria-label="Previous in circuit"' + (i <= 0 ? " disabled style=\"opacity:.4\"" : "") + ">" + ICON.prev + "</button>" +
          '<button class="act" id="btnCircuit">' + ICON.circuit + "Circuit</button>" +
          '<button class="act" id="btnNext" aria-label="Next in circuit"' + (i < 0 || i >= list.length - 1 ? " disabled style=\"opacity:.4\"" : "") + ">" + ICON.next + "</button>" +
          '<button class="act" id="btnFix">' + ICON.pin + "Fix position</button>" +
        "</div></div>";
    $("closeProblem").onclick = () => closeSheets();
    $("addPhoto").onclick = () => { $("photoInput").dataset.uid = p.uid; $("photoInput").click(); };
    $("btnProj").onclick = () => { S.projects.has(p.uid) ? S.projects.delete(p.uid) : S.projects.add(p.uid); saveSets(); refreshDot(p); renderProblem(p); toast(S.projects.has(p.uid) ? "Saved as a project" : "Removed from projects", 1600); };
    $("btnTick").onclick = () => { S.ticks.has(p.uid) ? S.ticks.delete(p.uid) : S.ticks.add(p.uid); saveSets(); refreshDot(p); renderProblem(p); toast(S.ticks.has(p.uid) ? "Ticked. Nice one." : "Tick removed", 1600); };
    $("btnPrev").onclick = () => { if (i > 0) selectProblem(list[i - 1], true); };
    $("btnNext").onclick = () => { if (i >= 0 && i < list.length - 1) selectProblem(list[i + 1], true); };
    $("btnCircuit").onclick = () => {
      const key = p.crag.id + "/" + p.sector.id;
      S.filters.circuit = S.filters.circuit === key ? null : key; store.set("filters", S.filters); drawDots();
      toast(S.filters.circuit ? "Showing only the " + p.sector.name + " circuit. Use the arrows to step through it." : "Showing all problems again", 2600);
      renderProblem(p);
    };
    $("btnFix").onclick = () => startEdit(p.boulder);
    const url = await photoFor(p);
    if (url && S.selected === p) {
      $("photoBox").innerHTML = '<img alt="Photo of ' + esc(p.label) + '" src="' + esc(url) + '">' +
        '<button class="x glass" id="closeProblem2" aria-label="Close">' + ICON.x + "</button>" +
        '<div class="photo-actions"><button class="chip" id="replacePhoto">Replace photo</button><button class="chip" id="removePhoto">Remove</button></div>';
      $("closeProblem2").onclick = () => closeSheets();
      $("replacePhoto").onclick = () => { $("photoInput").dataset.uid = p.uid; $("photoInput").click(); };
      $("removePhoto").onclick = async () => { await idbDel(p.uid); photoUrls.delete(p.uid); renderProblem(p); };
    }
  }

  // ---------- photos (kept on this device) ----------
  let dbp = null;
  function idb() {
    if (dbp) return dbp;
    dbp = new Promise((res) => {
      try {
        const r = indexedDB.open("northbloc", 1);
        r.onupgradeneeded = () => r.result.createObjectStore("photos");
        r.onsuccess = () => res(r.result); r.onerror = () => res(null);
      } catch (e) { res(null); }
    });
    return dbp;
  }
  async function idbGet(k) { const d = await idb(); if (!d) return null; return new Promise((res) => { try { const q = d.transaction("photos").objectStore("photos").get(k); q.onsuccess = () => res(q.result || null); q.onerror = () => res(null); } catch (e) { res(null); } }); }
  async function idbSet(k, v) { const d = await idb(); if (!d) return false; return new Promise((res) => { try { const tx = d.transaction("photos", "readwrite"); tx.objectStore("photos").put(v, k); tx.oncomplete = () => res(true); tx.onerror = () => res(false); } catch (e) { res(false); } }); }
  async function idbDel(k) { const d = await idb(); if (!d) return; return new Promise((res) => { try { const tx = d.transaction("photos", "readwrite"); tx.objectStore("photos").delete(k); tx.oncomplete = () => res(); tx.onerror = () => res(); } catch (e) { res(); } }); }
  $("photoInput").addEventListener("change", async (e) => {
    const f = e.target.files && e.target.files[0]; const uid = e.target.dataset.uid; e.target.value = "";
    if (!f || !uid) return;
    try {
      const img = await createImageBitmap(f);
      const s = Math.min(1, 1600 / Math.max(img.width, img.height));
      const c = document.createElement("canvas"); c.width = Math.round(img.width * s); c.height = Math.round(img.height * s);
      c.getContext("2d").drawImage(img, 0, 0, c.width, c.height);
      const blob = await new Promise((r) => c.toBlob(r, "image/jpeg", .85));
      const ok = await idbSet(uid, blob);
      if (!ok) { toast("This browser would not store the photo. Try the installed app."); return; }
      photoUrls.delete(uid); const p = S.byUid.get(uid); if (p && S.selected === p) renderProblem(p);
      toast("Photo saved on this phone", 1800);
    } catch (err) { toast("That photo could not be opened. Try a JPEG or PNG."); }
  });

  // ---------- filters ----------
  function renderFilters() {
    const f = S.filters, el = $("filterSheet");
    const levelBtns = LEVELS.map((l) => '<button class="opt" data-level="' + l.id + '" aria-pressed="' + f.levels.includes(l.id) + '"><i class="swatch" style="background:var(--c-' + l.color + ");" + (l.color === "black" ? "border:1.5px solid #ddd;box-sizing:border-box" : "") + '"></i><span class="grow">' + l.label + '</span><i class="tick-box"></i></button>').join("");
    const circBtns = '<button class="opt" data-circuit="" aria-pressed="' + !f.circuit + '"><span class="grow">All areas</span><i class="tick-box"></i></button>' +
      S.sectors.map((s) => { const k = s.crag.id + "/" + s.id; const n = s.boulders.reduce((a, b) => a + b.problems.length, 0);
        return '<button class="opt" data-circuit="' + esc(k) + '" aria-pressed="' + (f.circuit === k) + '"><span class="grow">' + esc(s.name) + '<br><span class="sub">' + esc(s.crag.name) + " · " + n + ' problems</span></span><i class="tick-box"></i></button>'; }).join("");
    const tog = (key, icon, label, sub) => '<button class="opt" data-toggle="' + key + '" aria-pressed="' + !!f[key] + '">' + icon + '<span class="grow">' + label + (sub ? '<br><span class="sub">' + sub + "</span>" : "") + '</span><i class="tick-box"></i></button>';
    el.innerHTML = '<div class="grab"></div><div class="sheet-head"><button class="btn-clear" id="fClear">Clear</button><h3>Filters</h3><button class="btn-ok" id="fDone" aria-label="Apply filters">' + ICON.ok + "</button></div>" +
      '<div class="filter-scroll">' +
      '<div class="group">' + '<div class="opt" style="pointer-events:none">' + ICON.bars + '<span class="grow"><b>Level</b><br><span class="sub">Dot colours match these bands</span></span></div>' + levelBtns + "</div>" +
      '<div class="group">' + '<div class="opt" style="pointer-events:none">' + ICON.circuit + '<span class="grow"><b>Circuit</b><br><span class="sub">The guidebook numbers each area as a circuit</span></span></div>' + circBtns + "</div>" +
      '<div class="group">' + tog("popular", ICON.heart, "Popular", "Classics picked from the guidebook notes") + "</div>" +
      '<div class="group">' + tog("project", ICON.starO, "Project") + tog("ticked", ICON.tickO, "Ticked") + "</div>" +
      '<div class="group">' + tog("check", ICON.warn, "Needs checking", "Names or grades hidden in the page photos") + "</div></div>";
    el.querySelectorAll("[data-level]").forEach((b) => b.onclick = () => { const id = b.dataset.level; const i = f.levels.indexOf(id); i < 0 ? f.levels.push(id) : f.levels.splice(i, 1); b.setAttribute("aria-pressed", f.levels.includes(id)); applyFilters(); });
    el.querySelectorAll("[data-circuit]").forEach((b) => b.onclick = () => { f.circuit = b.dataset.circuit || null; el.querySelectorAll("[data-circuit]").forEach((x) => x.setAttribute("aria-pressed", (x.dataset.circuit || null) === f.circuit)); applyFilters(); });
    el.querySelectorAll("[data-toggle]").forEach((b) => b.onclick = () => { const k = b.dataset.toggle; f[k] = !f[k]; b.setAttribute("aria-pressed", f[k]); applyFilters(); });
    $("fClear").onclick = () => { Object.assign(f, { levels: [], circuit: null, popular: false, project: false, ticked: false, check: false }); applyFilters(); renderFilters(); };
    $("fDone").onclick = () => {
      closeSheets();
      const n = visibleProblems().length;
      if (filtersActive()) {
        toast(n + (n === 1 ? " problem matches" : " problems match"), 1800);
        if (n && map.getZoom() < BOULDER_Z) { const b = L.latLngBounds(visibleProblems().map((p) => p.ll)); map.flyToBounds(b, { padding: [60, 140], maxZoom: 18.5, duration: .8 }); }
      }
    };
  }
  function applyFilters() { store.set("filters", S.filters); drawDots(); }

  // ---------- info sheet ----------
  function renderInfo() {
    const { sector, dist } = nearestSector(); const crag = sector.crag;
    const showSector = map.getZoom() >= 15.5 && dist < 400;
    const el = $("infoSheet");
    const n = crag.sectors.reduce((a, s) => a + s.boulders.reduce((x, b) => x + b.problems.length, 0), 0);
    el.innerHTML = '<div class="grab"></div><div class="sheet-head"><span></span><h3>' + esc(showSector ? sector.name : crag.name) + '</h3><button class="round dark" id="infoClose" aria-label="Close" style="width:44px;height:44px">' + ICON.x + "</button></div>" +
      '<div class="card-body">' +
      (showSector ? '<p class="desc">' + esc(sector.description) + "</p>" : "") +
      '<p class="desc">' + esc(crag.notes) + "</p>" +
      '<div class="meta"><span>' + ICON.pin + esc(crag.gridRef) + "</span><span>" + esc(crag.altitude) + "</span><span>" + esc(crag.aspect) + "</span><span>Walk-in " + esc(crag.approach) + "</span><span>" + n + " problems</span></div>" +
      '<div class="where">' + esc(crag.access) + "</div>" +
      crag.parking.map((pk) => '<div class="card" style="margin:0;padding:16px;background:rgba(255,255,255,.06)"><b>' + esc(pk.name) + '</b><p style="margin:6px 0 10px">' + esc(pk.note) + '</p><a class="btn-line" style="text-decoration:none;color:inherit" target="_blank" rel="noopener" href="https://www.google.com/maps/dir/?api=1&destination=' + pk.lat + "," + pk.lon + '">' + ICON.route + "Directions</a>" + (pk.positionEstimated ? '<span class="where"> Parking spot estimated</span>' : "") + "</div>").join("") +
      '<div class="check">' + ICON.warn + "<div>" + esc(crag.positionsNote) + "</div></div>" +
      (crag.missing || []).map((m) => '<div class="where">Not loaded yet: ' + esc(m) + "</div>").join("") +
      "</div>";
    $("infoClose").onclick = () => closeSheets();
  }

  // ---------- search ----------
  function renderResults() {
    const q = norm($("q").value.trim()); const out = [];
    const areaRow = (title, sub, act) => { out.push('<button class="res" data-act="' + act + '"><span class="nm">' + esc(title) + '</span><span class="ar">' + esc(sub) + "</span></button>"); };
    const probRow = (p) => out.push('<button class="res" data-p="' + esc(p.uid) + '"><span class="dot c-' + p.level.color + '">' + esc(p.number) + '</span><span class="nm">' + esc(p.label) + '</span><span class="gr">' + esc(p.grade === "?" ? "" : p.grade) + '</span><span class="ar">' + esc(p.boulder.name) + "</span></button>");
    if (!q) {
      out.push('<h3 class="sec-title">Popular areas</h3>');
      ["western", "summit", "north", "south"].forEach((id) => { const s = S.sectors.find((x) => x.id === id); if (s) areaRow(s.name, s.crag.name, "s:" + s.crag.id + "/" + s.id); });
      out.push('<h3 class="sec-title">Popular problems</h3>');
      S.problems.filter((p) => p.popular).slice(0, 12).forEach(probRow);
    } else {
      const words = q.split(/\s+/);
      const hit = (s) => words.every((w) => s.includes(w));
      const rank = (p) => (norm(p.boulder.name).includes(q) ? 2 : 0) + (norm(p.name).startsWith(q) ? 3 : 0) + (p.name ? 1 : 0) + (p.popular ? 1 : 0);
      const areas = [];
      S.crags.forEach((c) => { if (hit(norm(c.name + " " + c.region))) areas.push(["c", c.name, c.region, "c:" + c.id]); });
      S.sectors.forEach((s) => { if (hit(norm(s.name + " " + s.crag.name))) areas.push(["s", s.name, s.crag.name, "s:" + s.crag.id + "/" + s.id]); });
      S.boulders.forEach((b) => { if (hit(norm(b.name + " " + b.sector.name))) areas.push(["b", b.name, b.sector.name, "b:" + b.key]); });
      const probs = S.problems.filter((p) => hit(p.search) || words.length === 1 && norm(p.grade) === words[0]).sort((a, b) => rank(b) - rank(a) || a.gv - b.gv);
      if (areas.length) { out.push('<h3 class="sec-title">Areas</h3>'); areas.slice(0, 8).forEach((a) => areaRow(a[1], a[2], a[3])); }
      if (probs.length) { out.push('<h3 class="sec-title">Problems</h3>'); probs.slice(0, 40).forEach(probRow); }
      if (!areas.length && !probs.length) out.push('<p class="empty-note">Nothing called “' + esc($("q").value) + '” yet. Try a boulder name such as Neb, or a grade such as 6a.</p>');
    }
    $("results").innerHTML = out.join("");
  }
  $("results").addEventListener("click", (e) => {
    const b = e.target.closest("button"); if (!b) return;
    closeSearch(); showTab("map");
    if (b.dataset.p) { const p = S.byUid.get(b.dataset.p); if (p) selectProblem(p, true); return; }
    const [kind, key] = b.dataset.act.split(/:(.+)/);
    if (kind === "c") { const c = S.crags.find((x) => x.id === key); map.flyTo([c.lat, c.lon], 15.5, { duration: .8 }); }
    if (kind === "s") { const s = S.sectors.find((x) => x.crag.id + "/" + x.id === key); flyToSector(s); }
    if (kind === "b") { const bo = S.boulders.get(key); map.flyTo([bo.lat, bo.lon], 19.5, { duration: .8 }); }
  });
  function openSearch() { closeSheets(); $("searchPanel").classList.add("open"); $("searchPanel").setAttribute("aria-hidden", "false"); renderResults(); setTimeout(() => $("q").focus(), 60); }
  function closeSearch() { $("searchPanel").classList.remove("open"); $("searchPanel").setAttribute("aria-hidden", "true"); $("q").blur(); }
  $("q").addEventListener("input", renderResults);

  // ---------- tick list ----------
  function renderTicks() {
    const rows = S.problems.filter((p) => S.ticks.has(p.uid) || S.projects.has(p.uid));
    let h = '<div class="screen-inner"><h1>Tick List</h1>';
    if (!rows.length) {
      h += '<div class="card"><h2>Nothing here yet</h2><p>Open a problem on the map and tap <b>Save</b> to mark it as a project, or <b>Tick</b> once you have sent it. Both show up here, grouped by area.</p></div>';
    } else {
      const bySector = new Map();
      rows.forEach((p) => { const k = p.crag.name + " · " + p.sector.name; if (!bySector.has(k)) bySector.set(k, []); bySector.get(k).push(p); });
      for (const [k, ps] of bySector) {
        h += '<div class="list-head">' + esc(k) + "</div>";
        ps.sort((a, b) => a.boulder.name.localeCompare(b.boulder.name) || String(a.number).localeCompare(String(b.number), undefined, { numeric: true }));
        for (const p of ps) {
          const t = S.ticks.has(p.uid), pr = S.projects.has(p.uid);
          h += '<button class="tl-row" data-p="' + esc(p.uid) + '"><span class="num"><span class="dot c-' + p.level.color + '">' + esc(p.number) + '</span></span><span class="nm">' + esc(p.label) + '</span><span class="st">' + (pr ? '<span style="color:var(--star)">' + ICON.star + "</span>" : "") + (t ? ICON.tick : "") + '</span><span class="gr">' + esc(p.grade === "?" ? "–" : p.grade) + "</span></button>";
        }
      }
      const tk = S.problems.filter((p) => S.ticks.has(p.uid));
      const best = tk.slice().sort((a, b) => b.gv - a.gv)[0];
      h += '<div class="where" style="margin:18px 6px">' + tk.length + " ticked · " + S.problems.filter((p) => S.projects.has(p.uid)).length + " projects" + (best ? " · hardest tick " + esc(best.grade) : "") + "</div>";
    }
    h += '<div class="where" style="margin:10px 6px">Ticks, projects and photos are kept on this phone only.</div></div>';
    $("ticks").innerHTML = h;
  }
  $("ticks").addEventListener("click", (e) => { const b = e.target.closest("[data-p]"); if (!b) return; const p = S.byUid.get(b.dataset.p); showTab("map"); if (p) selectProblem(p, true); });

  // ---------- discover ----------
  function renderDiscover() {
    let h = '<div class="screen-inner"><div class="brand">' + LOGO + "<div><b>Northbloc</b><span>Bouldering in Northumberland</span></div></div><h1>Discover</h1>";
    for (const c of S.crags) {
      const ps = S.problems.filter((p) => p.crag === c), bs = c.sectors.reduce((a, s) => a + s.boulders.length, 0);
      const ticked = ps.filter((p) => S.ticks.has(p.uid)).length;
      const bands = LEVELS.filter((l) => l.id !== "u").map((l) => ({ l, n: ps.filter((p) => p.level === l).length }));
      const max = Math.max(...bands.map((b) => b.n), 1);
      h += '<div class="card"><h2>' + esc(c.name) + '</h2><p>' + esc(c.notes) + "</p>" +
        '<div class="stats"><div class="stat"><b>' + ps.length + '</b><span>Problems</span></div><div class="stat"><b>' + bs + '</b><span>Boulders</span></div><div class="stat"><b>' + ticked + "</b><span>Ticked</span></div></div>" +
        '<div class="bars" aria-label="Problems by level">' + bands.map((b) => '<div><small>' + b.n + '</small><i style="height:' + Math.round(b.n / max * 70) + "%;background:var(--c-" + b.l.color + ");" + (b.l.color === "black" ? "outline:1px solid #555" : "") + '"></i><small>' + esc(b.l.label.replace(" and harder", "+").replace("Up to ", "≤").replace(" to ", "–")) + "</small></div>").join("") + "</div>" +
        c.sectors.map((s) => '<button class="sector-row" data-s="' + esc(c.id + "/" + s.id) + '">' + esc(s.name) + '<span class="cnt">' + s.boulders.reduce((a, b) => a + b.problems.length, 0) + " problems</span>" + ICON.chev + "</button>").join("") +
        "</div>";
    }
    const nCheck = S.problems.filter((p) => p.check).length;
    h += '<div class="card"><h2>Needs checking</h2><p>' + nCheck + " problems have a name, number or grade that was hidden by glare or the page shadow in the guidebook photos. They show a yellow note on their card.</p>" +
      '<button class="btn-line" id="showCheck">' + ICON.warn + "Show them on the map</button></div>";
    const fixes = Object.keys(S.fixes).length;
    h += '<div class="card"><h2>Boulder positions</h2><p>Positions came from the guidebook sketch maps, lined up with the rocks on satellite imagery and OpenStreetMap, so treat them as close but not exact. When you are at a boulder, open any of its problems and tap <b>Fix position</b>. Your fixes stay on this phone; copy them below and send them over to update the map for everyone.</p>' +
      "<p><b>" + fixes + "</b> boulder" + (fixes === 1 ? "" : "s") + " fixed so far.</p>" +
      (fixes ? '<button class="btn-line" id="copyFixes">' + ICON.copy + 'Copy fixes</button><textarea class="export" id="fixText" readonly aria-label="Position fixes">' + esc(JSON.stringify(S.fixes, null, 1)) + "</textarea>" : "") + "</div>";
    h += '<div class="card"><h2>Adding crags and climbs</h2><p>Each crag is one file in the <b>data</b> folder, and data/crags.json lists them. Copy shaftoe.json, change the names, grades and positions, and add the file name to the list. Each problem has a <b>photo</b> slot for a topo picture.</p><p>Photos you add from your phone appear straight away but stay on your phone until they are added to the data.</p></div>';
    h += '<div class="card"><h2>About the data</h2><p>' + S.crags.map((c) => esc(c.source)).join(" ") + "</p>" + S.crags.flatMap((c) => (c.missing || []).map((m) => "<p>" + esc(m) + "</p>")).join("") + "<p>Map data © OpenStreetMap contributors. Satellite imagery © Esri.</p></div></div>";
    $("discover").innerHTML = h;
    $("discover").querySelectorAll("[data-s]").forEach((b) => b.onclick = () => { const s = S.sectors.find((x) => x.crag.id + "/" + x.id === b.dataset.s); showTab("map"); flyToSector(s); });
    $("showCheck").onclick = () => { Object.assign(S.filters, { check: true }); applyFilters(); showTab("map"); const b = L.latLngBounds(visibleProblems().map((p) => p.ll)); map.flyToBounds(b, { padding: [60, 140], duration: .8 }); toast("Showing problems that need checking. Clear it in Filters.", 2600); };
    const cp = $("copyFixes");
    if (cp) cp.onclick = () => {
      const t = $("fixText"); const txt = t.value;
      try { navigator.clipboard.writeText(txt).then(() => toast("Fixes copied", 1500), () => { t.select(); toast("Select all and copy the text below"); }); }
      catch (e) { t.select(); toast("Select all and copy the text below"); }
    };
  }

  // ---------- tabs ----------
  function showTab(tab) {
    document.querySelectorAll(".tab").forEach((t) => t.setAttribute("aria-selected", t.dataset.tab === tab));
    $("discover").hidden = tab !== "discover"; $("ticks").hidden = tab !== "ticks";
    if (tab === "discover") renderDiscover();
    if (tab === "ticks") renderTicks();
    if (tab !== "map") { closeSheets(); closeSearch(); }
    const glassOnMap = tab === "map";
    document.querySelector(".tabbar").style.background = glassOnMap ? "" : "rgba(28,28,30,.92)";
  }
  document.querySelectorAll(".tab").forEach((t) => t.onclick = () => showTab(t.dataset.tab));

  // ---------- location ----------
  let watchId = null, meMarker = null, meCircle = null, firstFix = true;
  function locate() {
    if (!("geolocation" in navigator)) { toast("This browser cannot share your location."); return; }
    if (S.me && watchId != null) { map.flyTo([S.me.lat, S.me.lon], Math.max(map.getZoom(), 17), { duration: .8 }); return; }
    $("locateBtn").classList.add("on"); firstFix = true;
    try {
      watchId = navigator.geolocation.watchPosition((pos) => {
        S.me = { lat: pos.coords.latitude, lon: pos.coords.longitude, acc: pos.coords.accuracy };
        const ll = [S.me.lat, S.me.lon];
        if (!meMarker) {
          meMarker = L.marker(ll, { icon: L.divIcon({ className: "", html: '<div class="me"></div>', iconSize: [0, 0] }), interactive: false, zIndexOffset: 2000 }).addTo(map);
          meCircle = L.circle(ll, { radius: S.me.acc, color: "#0a84ff", weight: 1, fillOpacity: .12, interactive: false }).addTo(map);
        } else { meMarker.setLatLng(ll); meCircle.setLatLng(ll).setRadius(S.me.acc); }
        if (firstFix) { firstFix = false; map.flyTo(ll, Math.max(map.getZoom(), 17), { duration: .8 }); }
      }, (err) => {
        $("locateBtn").classList.remove("on"); watchId = null;
        toast(err.code === 1 ? "Location is blocked here. Open Northbloc from its own web link (or the home-screen app) and allow location." : "Could not get a GPS fix. Try again in the open.", 4200);
      }, { enableHighAccuracy: true, maximumAge: 5000, timeout: 20000 });
    } catch (e) { toast("Location is not available in this view."); }
  }
  $("locateBtn").onclick = locate;

  // ---------- fixing boulder positions ----------
  function startEdit(b) {
    closeSheets(); S.editing = b;
    $("editBar").hidden = false; $("editText").textContent = "Moving " + b.name + ". Drag the handle to where the boulder really is, or stand next to it and use your position.";
    map.flyTo([b.lat, b.lon], 19.5, { duration: .6 });
    if (editLayer) map.removeLayer(editLayer);
    editLayer = L.marker([b.lat, b.lon], { draggable: true, zIndexOffset: 3000, icon: L.divIcon({ className: "", html: '<div style="width:34px;height:34px;border-radius:50%;background:#45d86f;border:3px solid #fff;transform:translate(-50%,-50%);box-shadow:0 2px 8px rgba(0,0,0,.5)"></div>', iconSize: [0, 0] }) }).addTo(map);
    editLayer.on("drag", (e) => moveBoulder(b, e.target.getLatLng(), false));
    editLayer.on("dragend", (e) => moveBoulder(b, e.target.getLatLng(), true));
  }
  function moveBoulder(b, ll, save) {
    b.lat = ll.lat; b.lon = ll.lng; drawBoulder(b);
    if (save) { b.fixed = true; S.fixes[b.key] = { lat: +b.lat.toFixed(6), lon: +b.lon.toFixed(6) }; store.set("fixes", S.fixes); drawDots(); drawSectors(); }
  }
  $("editGps").onclick = () => {
    const b = S.editing; if (!b) return;
    const use = () => { const ll = L.latLng(S.me.lat, S.me.lon); editLayer.setLatLng(ll); moveBoulder(b, ll, true); map.panTo(ll); toast("Moved to your position (±" + Math.round(S.me.acc) + " m)", 2200); };
    if (S.me) use(); else { locate(); toast("Getting your position… tap again once the blue dot appears.", 3000); }
  };
  $("editDone").onclick = () => { S.editing = null; $("editBar").hidden = true; if (editLayer) { map.removeLayer(editLayer); editLayer = null; } };
  $("editReset").onclick = () => {
    const b = S.editing; if (!b) return; delete S.fixes[b.key]; store.set("fixes", S.fixes);
    const orig = b._orig; b.lat = orig[0]; b.lon = orig[1]; b.fixed = false; drawBoulder(b); drawDots(); drawSectors(); editLayer.setLatLng(orig); toast("Back to the estimated position", 1800);
  };

  // ---------- offline ----------
  function tileList(bounds, z0, z1) {
    const out = [];
    for (let z = z0; z <= z1; z++) {
      const a = map.project(bounds.getNorthWest(), z).divideBy(256).floor(), b = map.project(bounds.getSouthEast(), z).divideBy(256).floor();
      for (let x = a.x; x <= b.x; x++) for (let y = a.y; y <= b.y; y++) out.push({ x, y, z });
    }
    return out;
  }
  $("offlineBtn").onclick = async () => {
    const reg = ("serviceWorker" in navigator) ? await navigator.serviceWorker.getRegistration().catch(() => null) : null;
    if (!reg) { toast("Offline download works in the installed app. Open Northbloc from its own link, add it to your Home Screen, then tap this again.", 5000); return; }
    const bounds = L.latLngBounds(S.problems.map((p) => p.ll)).pad(0.25);
    const base = BASES[baseIdx].id === "sat" ? BASES[1] : BASES[0];
    const layer = base.make();
    const tiles = tileList(bounds, 12, 18);
    let done = 0, failed = 0; const total = tiles.length;
    toast("Saving " + total + " map tiles for offline use…", 2000);
    const urlFor = (t) => L.Util.template(layer._url, { x: t.x, y: t.y, z: t.z });
    const queue = tiles.slice();
    async function worker() {
      while (queue.length) {
        const t = queue.shift();
        try { const u = urlFor(t); if (u) { const r = await fetch(u, { mode: "no-cors" }); if (!r) failed++; } } catch (e) { failed++; }
        done++; if (done % 40 === 0) toast("Saving map tiles… " + Math.round(done / total * 100) + "%", 1500);
      }
    }
    await Promise.all([worker(), worker(), worker(), worker(), worker(), worker()]);
    toast(failed ? "Saved most tiles (" + failed + " failed). Climbs are always available offline." : "Shaftoe map saved for offline use.", 3500);
  };

  // ---------- wiring ----------
  $("searchPill").onclick = openSearch; $("searchRound").onclick = openSearch; $("searchClose").onclick = closeSearch;
  $("filterBtn").onclick = () => { renderFilters(); openSheet("filterSheet"); };
  $("areaPill").onclick = () => { renderInfo(); openSheet("infoSheet"); };
  $("layerBtn").onclick = () => { const i = (baseIdx + 1) % BASES.length; setBase(i); toast(BASES[i].name, 1200); };

  async function start() {
    map = L.map("map", { zoomControl: false, attributionControl: true, zoomSnap: .25, zoomDelta: .5, maxZoom: 22, minZoom: 6, tap: true, worldCopyJump: false });
    setBase(baseIdx);
    sectorLayer = L.layerGroup(); sectorLabelLayer = L.layerGroup(); cragLabelLayer = L.layerGroup();
    boulderLayer = L.featureGroup(); dotLayer = L.layerGroup(); boulderNameLayer = L.layerGroup();
    const view = store.get("view", null);
    map.setView(view ? [view[0], view[1]] : [55.18, -1.95], view ? view[2] : 10);
    try { await loadData(); }
    catch (e) { toast("Could not load the climb data. Check your connection and reload.", 6000); return; }
    for (const b of S.boulders.values()) drawBoulder(b);
    drawSectors(); drawCragLabels(); drawDots();
    map.on("zoomend", onZoom); map.on("moveend", () => { updateAreaName(); const c = map.getCenter(); store.set("view", [+c.lat.toFixed(5), +c.lng.toFixed(5), map.getZoom()]); });
    map.on("click", () => { if (S.selected) closeSheets(); });
    onZoom();
    if (!view && S.crags.length === 1) setTimeout(() => toast("Tap Shaftoe to zoom in. Positions are estimates, see the info button.", 3800), 600);
  }

  if ("serviceWorker" in navigator && location.protocol === "https:" && !/claude\.ai|claudeusercontent|claude\.site/.test(location.hostname)) {
    try { navigator.serviceWorker.register("sw.js").catch(() => {}); } catch (e) { /* not available */ }
  }
  start();
})();
