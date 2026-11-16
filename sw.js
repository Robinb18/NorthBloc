// Northbloc service worker: app and climb data cached for offline use, map tiles cached as you view or download them.
const APP = "northbloc-app-v3", TILES = "northbloc-tiles-v1";
const SHELL = ["./", "index.html", "app.js", "vendor/leaflet.js", "data/crags.json", "data/shaftoe.json", "manifest.webmanifest", "icon-192.png", "icon-512.png"];
self.addEventListener("install", (e) => { e.waitUntil(caches.open(APP).then((c) => c.addAll(SHELL.map((u) => new Request(u, { cache: "reload" })))).then(() => self.skipWaiting())); });
self.addEventListener("activate", (e) => { e.waitUntil(caches.keys().then((ks) => Promise.all(ks.filter((k) => k !== APP && k !== TILES).map((k) => caches.delete(k)))).then(() => self.clients.claim())); });
self.addEventListener("fetch", (e) => {
  const url = new URL(e.request.url);
  if (e.request.method !== "GET") return;
  const isTile = /tile\.openstreetmap\.org|arcgisonline\.com/.test(url.hostname);
  if (isTile) {
    e.respondWith(caches.open(TILES).then(async (c) => {
      const hit = await c.match(e.request, { ignoreVary: true });
      if (hit) return hit;
      try { const r = await fetch(e.request); if (r && (r.ok || r.type === "opaque")) c.put(e.request, r.clone()); return r; }
      catch (err) { return hit || Response.error(); }
    }));
    return;
  }
  if (url.origin === location.origin) {
    // network first (skipping the browser cache) so updates and new climbs show up, cache fallback offline
    e.respondWith(fetch(url.href, { cache: "no-cache" }).then((r) => { if (r.ok) caches.open(APP).then((c) => c.put(e.request, r.clone())); return r; })
      .catch(() => caches.match(e.request, { ignoreSearch: true }).then((r) => r || caches.match("index.html"))));
  } else if (/fonts\.(googleapis|gstatic)\.com/.test(url.hostname)) {
    e.respondWith(caches.open(APP).then(async (c) => { const hit = await c.match(e.request); if (hit) return hit; const r = await fetch(e.request); c.put(e.request, r.clone()); return r; }));
  }
});
