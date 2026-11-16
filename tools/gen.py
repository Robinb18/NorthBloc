import json, math, sys
sys.path.insert(0,'.')
from spec import S
from fit import fit
fit(S)
LAT0, LON0 = 55.13638, -1.91605   # NZ054824 (centre of the 100m square)
def ll(x,y): return round(LAT0 + y/111320,6), round(LON0 + x/(111320*math.cos(math.radians(LAT0))),6)
SECT = [
 ("rift","The Rift","Also called Long Byres. A dry valley on the east side, closest to the eastern parking. Several roofed traverses stay dry in rain."),
 ("north","Shaftoe North","Quiet west-facing problems near Middleton Bank Top Farm. Arête Land is the busiest spot; the Pudding Stone and North Buttress are further north."),
 ("central","Central Area","Interesting, slightly esoteric boulders around Salter's Nick. Many face south and are best in winter."),
 ("western","Western Edges","Near Shaftoe Grange Farm, home to many of the most popular boulders: Font, Smith's Rocks, Turtle Rock and the Neb."),
 ("summit","Shaftoe Summit","Rocks around the 213m trig point, overlooking Shaftoe Grange Farm to the west and the Central Area to the north."),
 ("south","Shaftoe South","Boulders in the wooded escarpment above Ferney Chesters and the A696, and on the plateau above. Generally more sheltered."),
]
def flags(f):
  d={}
  if 's' in f: d['sitStart']=True
  if 't' in f: d['traverse']=True
  if 'h' in f: d['highball']=True
  if 'j' in f: d['jumpStart']=True
  return d
POP={("rift-north","4"),("arete-land","20"),("arete-land","11"),("jubilee-boulder","42"),("lost-arrowhead-cave","28"),("lost-arrowhead-cave","25"),("syco-sheep","12"),("salters-nick-boulder","6"),("font-boulder","11"),("font-boulder","4"),("smiths-rocks","27"),("smiths-rocks","30"),("turtle-rock","46"),("turtle-rock","47"),("neb-boulder","55"),("neb-boulder","53"),("neb-boulder","60"),("neb-boulder","51"),("main-buttress","38a"),("main-buttress","40"),("the-cob","49"),("the-cob","50"),("dishpan-alley","26"),("cave-buttress","14"),("little-dal","25"),("long-wall","27a"),("central-alcove","37"),("two-tier","40")}
sectors=[]
for sid,name,desc in SECT:
  bl=[]
  for b in [b for b in S if b['sector']==sid]:
    lat,lon=ll(b['x'],b['y'])
    probs=[]
    for n,pn,g,f,d,chk in b['problems']:
      p={"number":n,"name":pn,"grade":g,**flags(f),"description":d,"photo":None}
      if (b["id"],n) in POP: p["popular"]=True
      if chk: p["check"]=chk
      if g=='?': p.setdefault("check","Grade not legible")
      probs.append(p)
    bl.append({"id":b['id'],"name":b['name'],"lat":lat,"lon":lon,"positionEstimated":True,
               "size":[b['w'],b['h']],"rotation":b['rot'],"description":b['desc'],"problems":probs})
  sectors.append({"id":sid,"name":name,"description":desc,"boulders":bl})
_xs=[b['x'] for b in S]; _ys=[b['y'] for b in S]
CLAT,CLON=ll((min(_xs)+max(_xs))/2,(min(_ys)+max(_ys))/2)
crag={
 "id":"shaftoe","name":"Shaftoe","region":"Northumberland",
 "gridRef":"NZ054824","lat":CLAT,"lon":CLON,"altitude":"212m","aspect":"Mostly west facing","approach":"5 to 10 minutes",
 "access":"Open access land (CRoW).",
 "parking":[
   {"name":"Bolam West Houses track (limited)","lat":55.1365,"lon":-1.9092,"positionEstimated":True,
    "note":"From Belsay take the road past Bolam Lake, turn left down the track at Bolam West Houses (5 mph please). Park just after the cattle grid, or by the small lake without blocking the track. About 10 minutes to the rocks."},
   {"name":"A696 lay-by (Ferney Chesters)","lat":55.1224,"lon":-1.9176,"positionEstimated":True,
    "note":"From Belsay follow the A696 towards Jedburgh and park in the lay-by on the right. Walk back to the track signed Ferney Chesters and Shaftoe Grange, about 5 minutes to the crag."}],
 "notes":"Over 300 problems on 50+ boulders across Shaftoe Moor. The ground gets wet and boggy in winter and after long rain. Rock quality varies, and it can be soft and friable at the base of some boulders.",
 "positionsNote":"Boulder positions are estimated. The guidebook's sketch maps were lined up with the rocks visible on satellite imagery and mapped in OpenStreetMap, then each boulder was placed on the nearest mapped rock. Some may still be tens of metres out, so correct them on site with the Fix position tool.",
 "source":"Problem names, numbers and grades from the Northumberland guidebook (Shaftoe pages 332-383). Descriptions written fresh for this app.",
 "sectors":sectors}
json.dump(crag,open('shaftoe.json','w'),indent=1,ensure_ascii=False)
np=sum(len(b['problems']) for s in sectors for b in s['boulders']); nb=sum(len(s['boulders']) for s in sectors)
nc=sum(1 for s in sectors for b in s['boulders'] for p in b['problems'] if 'check' in p)
print(nb,'boulders',np,'problems',nc,'to check')
