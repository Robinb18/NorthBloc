# Northbloc

A bouldering map for Northumberland, laid out like Boolder: a dark map that zooms from crags, to areas, to boulders with numbered, colour-coded problem dots. Search, filters, problem cards with a photo slot, projects and ticks, live GPS position, and offline maps.

## Files

| File | What it is |
|---|---|
| `index.html` | The app (install this one on your phone) |
| `app.js` | The app's code |
| `vendor/leaflet.js` | Map library (Leaflet 1.9.4) |
| `data/crags.json` | List of crag files to load |
| `data/shaftoe.json` | Shaftoe: 6 areas, 58 boulders, 307 problems |
| `sw.js`, `manifest.webmanifest`, icons | Make it installable and work offline |
| `artifact.html` | Same app, as a preview page (no GPS or map tiles there) |

## Putting it on your iPhone

GPS, map tiles and offline maps need the app to be served from its own web address (HTTPS). The simplest free option is GitHub Pages: put this folder in a GitHub repository, turn on Pages for it, open the address in Safari, then Share → Add to Home Screen.

## Adding a crag

1. Copy `data/shaftoe.json` to `data/<crag>.json` and edit it.
2. Add the file name to `data/crags.json`, e.g. `{"crags": ["shaftoe.json", "bowden-doors.json"]}`.

Each crag has `sectors` (areas), each sector has `boulders`, each boulder has `problems`:

```json
{
  "id": "neb-boulder", "name": "Neb Boulder",
  "lat": 55.135342, "lon": -1.923146, "positionEstimated": true,
  "size": [14, 7], "rotation": 0,
  "description": "The smaller neb, 8m south of Turtle Rock.",
  "problems": [
    { "number": "55", "name": "The Neb Roof", "grade": "6c", "sitStart": true,
      "description": "Straight out across the roof.", "photo": null }
  ]
}
```

- `grade` uses Font grades (`4+`, `6a`, `7b+`). Use `"?"` if unknown.
- Optional problem flags: `sitStart`, `traverse`, `highball`, `jumpStart`, `popular`.
- `check` holds a note when something needs confirming; it shows on the card.
- `photo` is a path to a topo image, e.g. `"photos/shaftoe/neb-55.jpg"`. Leave it `null` until you have one.
- `size` is the boulder footprint in metres `[width, depth]`; `rotation` is in degrees.

## Fixing positions

Shaftoe's boulder positions are estimated. `tools/fit.py` lines the guidebook sketch maps up with the rocks on satellite imagery and the rock outlines mapped in OpenStreetMap (`tools/osm_rocks.json`, © OpenStreetMap contributors, ODbL), then puts each boulder on the nearest mapped rock. At the crag, open a problem, tap **Fix position**, then drag the boulder or use your GPS. The Discover tab lists your fixes so they can be copied back into the data file.
