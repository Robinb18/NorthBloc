# Compact spec for Shaftoe. Positions are local metres (x east, y north) from NZ054824 — ESTIMATED from the
# guidebook's not-to-scale sketch maps. Problem tuple: (number, name, grade, flags, description, check_note)
# flags: s = sit start, t = traverse, h = highball, j = jump start, l = link/eliminate
S = []
def B(sector, bid, name, x, y, w, h, rot, desc, probs):
    S.append(dict(sector=sector, id=bid, name=name, x=x, y=y, w=w, h=h, rot=rot, desc=desc, problems=probs))

# ---------------- THE RIFT ----------------
B("rift","rift-north","The Rift, North Side",265,262,62,9,-8,
 "Long roofed wall on the north side of a usually dry valley running east to west. The roofed traverses stay dry in light rain.",[
 ("1","First Problem","6a+","","Mantel onto the ledge just right of where Perpetual Motion starts.",""),
 ("2","","7a+","t","Traverse the lip from the pillar at the right end of the roof, leftwards to the corner past the first boulder.",""),
 ("3","","7a","t","Carry on traversing left from the first corner to the second.",""),
 ("4","Perpetual Motion","7c","t","Problems 2 and 3 in one go, with no rest in the corner. A pumpy classic.",""),
 ("5","","5","t","Follow the break at the back of the roof, starting 5m left of the pillar, finishing at the corner past the first boulder.",""),
 ("6","","6a+","s","From a sitting start 2m right of the pothole, reach the lip and shuffle left to the pothole to pull over.",""),
 ("7","","5+","t","Left-to-right along the break then the lip, ending stood up above the cave.",""),
])
B("rift","rift-west","The Rift, West Block",205,268,14,6,-8,"Short wall about 50m left (west) of the main north side roof.",[
 ("8","","6a","t","From above the block at the left end, follow the lip right, drop to the break, come back left via two big pockets and finish along the lip.",""),
])
B("rift","rift-south","The Rift, South Side",255,238,48,8,-6,"The opposite (south) wall of the valley.",[
 ("9","","6b","t","Starts on a layaway at the left end and traverses to the dirty corner.",""),
 ("10","","6c","t","From the dirty corner, traverse right along the roof until you can land on the block.",""),
 ("11","","7a","t","Problems 9 and 10 combined, a good stamina workout.",""),
])
B("rift","rift-schism","Schism Wall",200,236,30,7,-5,"Western end of the south side.",[
 ("12","Schism","7a","t","From the dirty corner left of the nose, move left along the break with harder and harder moves until you can step onto the slab.",""),
 ("13","The First Nose","6b","","From the shelf under the nose, gain the lip by either line of holds and mantel.",""),
 ("14","The Second Nose","6b","","Small crimps right of a leaning boulder lead to a long reach and an awkward mantel.",""),
 ("15","The Lip","6a","t","Traverse a waist-high lip left to right, finishing with a mantel. About 25m right of the noses.",""),
 ("16","Broken Lip","6a","t","A shorter lip 12m right of The Lip, from the left end of the roof rightwards to a mantel.",""),
])

# ---------------- SHAFTOE NORTH ----------------
B("north","pudding-stone","The Pudding Stone",-100,780,9,6,20,"Second-to-last boulder in a group at the far north end of the escarpment, with a crack on its left side.",[
 ("1","","5","","Right-hand line up the crack.",""),
 ("2","","5","","Left-hand line up the crack.",""),
 ("3","","6c","s","Sit start at the far right end, then climb diagonally leftwards.",""),
])
B("north","north-buttress","North Buttress",-108,752,16,7,20,"Small crag at the north end of the escarpment, 25m south of the Pudding Stone.",[
 ("4","Short Wall","4","","The short wall.",""),
 ("5","Merry Dancers","6a","","Wall and left arête.",""),
 ("6","Undercut Arête","6b","","The undercut arête.",""),
 ("7","Mini Power","6c","","Small crimps on the wall left of the big leaning boulder.",""),
 ("8","Aurora Borealis","4","","The arête, without bridging.",""),
 ("9","Northern Frights","5+","","The wall, getting harder as you go.",""),
])
B("north","arete-land","Arête Land (Hallions Rocks)",-237,550,22,10,15,"Small outcrop with an off-width crack in the middle and an overhanging arête at the right end. Marked as Hallions Rocks on OS maps. The most popular spot in Shaftoe North.",[
 ("10","","5+","s","Sit start on the left arête, mantel to finish.",""),
 ("11","Piano","7b+","s","Sit start at the left arête, follow the overlap rightwards on undercuts to the right arête, then up to the break.",""),
 ("12","Fingers","7a","t","Low traverse beneath Piano, from the left arête.",""),
 ("13","The Long Reach","6c","","From the middle of the wall, use the undercling to reach the top. Sit start is 7b.",""),
 ("14","Slapper","6c","s","Left side of the arête from a sit start, right hand on the arête.",""),
 ("15","Clamper","7a+","s","The arête with both hands on it; feet anywhere except the right wall.",""),
 ("16","Corner Crack","4+","","Layback or jam the crack and carry on up the arête.",""),
 ("17","","6a+","t","From the crack, go right under the bulge and round the right arête, finishing up 24.",""),
 ("18","","5","","Middle of the wall, finishing by the left arête or direct.",""),
 ("19","","6a","","Slopers left of the arête to an undercut, then straight up.",""),
 ("20","Classic Arête","6a+","s","The arête from a sit start.",""),
 ("21","","5+","s","Sit start right of the arête, reach a pocket at 2m and top out via the rounded break.",""),
 ("22","","5+","","As for 21 but use the smaller pocket to the right and top out a bit further right.",""),
 ("23","","6a+","","From mid-wall, use a layaway to reach the top.",""),
 ("24","","6a","","Start as 23, then up and right to a pocket and a crimp in the break.",""),
])
B("north","six-pack","Six Pack",-241,512,9,5,15,"Heavily undercut shelf with a short crack just to its right.",[
 ("25","Six Pack Circuit","6b","t","From the left end traverse right to the right arête, gain the lip and follow it back left.",""),
 ("26","Lip Trip","6a+","t","Traverse the lip from either end to a mantel at its widest point.",""),
 ("27","Alexis","6b+","s","Sit start under the shelf near its left end, crimp up, then a long move right to a sloping crimp and mantel.",""),
])
B("north","punishment-block","Punishment Block",-246,474,12,7,10,"Whale-shaped boulder with a big fallen block under its roof. The slab on the north side has the first three problems.",[
 ("28","Green Line","4+","","The obvious groove on the left. The boulder behind is off limits.",""),
 ("29","","4","","Straight up past pockets on the left.",""),
 ("30","","4","","Right-hand pockets, then move right to finish.",""),
 ("31","","7b","t","Traverse left to right to the middle, mantel at the holes.",""),
 ("32","","5+","t","Follow pockets along the back wall with feet on the back wall.",""),
 ("33","","7a","t","Right to left to the middle, then mantel.",""),
 ("34","","6c","","Mantel over the lip.",""),
])
B("north","dolphin","Dolphin",-249,440,10,5,10,"Boulder just south of the Punishment Block.",[
 ("35","","6c","t","From the left end, traverse and mantel.",""),
 ("36","","6c","","Starts from the right-hand hole.",""),
 ("37","","7b","t","From the gully on the right, traverse left to the nose and finish as for 35.",""),
])
B("north","inclined-slab","The Inclined Slab",-236,418,5,8,-20,"A tilted slab resting on two other boulders.",[
 ("38","","3+","","Left side of the slab.",""),
])
B("north","grindstone","The Grindstone",-255,398,9,8,0,"Dome-topped boulder with a 2m roof and two smaller boulders under it. Two easy warm-ups go either side of the arête to its right.",[
 ("39","From the Left","7a","t","From the left, traverse to the nose and mantel.","Name from Rockfax, matched by its place in the list and its grade"),
 ("40","From the Right","6c","t","From the right, traverse to the nose and mantel.","Name from Rockfax, matched by its place in the list and its grade"),
 ("41","Total Traverse","7a","t","Girdle the whole boulder in either direction.","Name from Rockfax, matched by its place in the list and its grade"),
])
B("north","jubilee-boulder","Jubilee Boulder",-262,322,12,6,10,"75m further south, just north-west of the Jubilee Stone on top of the escarpment. Grassy on top at the left end, with a nose over a 2m roof on the right.",[
 ("42","Jubilee Traverse","6c+","st","Sit start on good holds at the left end, gain the lip and heel-hook along it, round the nose to a jug and mantel.",""),
])

# ---------------- CENTRAL AREA ----------------
B("central","salters-nick","Salter's Nick",-132,108,24,10,30,"The big rock outcrop at the west end of the escarpment. The first problem is on the right of the wide track in the small gorge, where the rock turns undercut.",[
 ("1","In the Nick","6c","t","From the far left of the ledge, hand traverse right round the arête and up to the break.",""),
 ("2","Sharp Arête","5","","Left side of the sharp arête, beside a small alcove.",""),
 ("3","Crack and Roof","5","","Crack through the roof to a tricky mantel. Poor landing.",""),
 ("4","Salt n Pepper","6a","","Undercut blunt arête, climbable either side. The right side is harder, 6a.",""),
 ("5","'S' Crack","4","","S-shaped crack to a juggy top.",""),
])
B("central","snail-boulder","Snail Boulder",-150,82,3,3,0,"Tiny boulder below Salter's Nick.",[
 ("5a","Snail Boulder","5","s","Sit start bottom right, climb to top left staying under the lip until the end.",""),
])
B("central","salters-nick-boulder","Salter's Nick Boulder",-122,70,16,7,10,"Long boulder south of Salter's Nick.",[
 ("6","Central Traverse","6c","t","Feet on the boulder at the left end, traverse right to big holds.",""),
 ("7","Right-hand Traverse","5+","t","Lip of the right-hand block, left to right.",""),
 ("8","Combined Traverse","7a","t","6 and 7 linked. Can also start at the far left end.",""),
 ("9","","6c+","s","Sit start, use the hold at the top of the faint flake to reach the lip, mantel using quartz holds or slopers.",""),
 ("10","","5+","s","Sit start on a tiny undercut and a nodule, slap for the big hole and mantel.",""),
])
B("central","small-boulder","Small Boulder",-102,78,4,3,0,"Small boulder east of Salter's Nick Boulder.",[
 ("11","Small Boulder","5","s","Sit start, bottom right to top left.",""),
])
B("central","syco-sheep","Syco Sheep Wall",-92,92,6,4,0,"Wall with a bottomless arête.",[
 ("12","Syco Sheep","6b+","h","Below the bottomless arête, up under the roof, out left to a sloper and up the arête and fluting. Highball, a spotter is essential.",""),
 ("13","Full Nettle Jacket","5+","","Right side of the arête. 4+ if you use the small ledge with the sapling.",""),
])
B("central","finger-bowl","Finger Bowl Boulders",-74,86,8,4,0,"A few metres right of Syco Sheep Wall.",[
 ("14","Finger Bowl","4","","Blunt left arête.",""),
 ("15","Chicken Ed","4+","","Front face left of the deep crack, using the crack and the chicken-head hold.",""),
 ("16","The Crucifier","5+","","From under the arête on its right side, use the pothole and arête.",""),
])
B("central","lost-arrowhead-lower","Lost Arrowhead Lower Boulder",-40,98,10,5,5,"The lower of two popular caves just along the escarpment from Salter's Nick.",[
 ("17","","4+","s","Sit start at the flake on the left, gain the lip, mantel and finish up the slab.",""),
 ("18","","5+","s","Sit start in the middle of the cave, go up and right to the lip and the easy slab.",""),
 ("19","","5+","s","Sit start at the right end, good hold then up and left to a flat hold.",""),
 ("20","The Temporary Neb","5+","st","Lip traverse from a sit start left of 17, ending with a frantic mantel right of 18.",""),
 ("20a","","6a+","t","Low traverse left to right.",""),
])
B("central","lost-arrowhead-cave","Lost Arrowhead Cave",-18,116,12,6,5,"The upper cave.",[
 ("21","Lost Slab","4","","Short slab left of the groove.",""),
 ("22","Lost Groove","4","","Groove at the left end.",""),
 ("23","Axe Head","6a","s","Sit start under the undercut nose, up to the break and the slab above.",""),
 ("24","Stone Age Man","7b","","From the back of the cave on a flatty and a layaway, cross the roof to potholes by the lip and wrestle onto the slab.",""),
 ("25","Lost Arrowhead","6c","","From the back of the cave as for 24, up and right to the niche and the hanging arête.",""),
 ("26","Broken Arrow","7c","st","Sit start under 23, low traverse right to the start of 24. Linked into Stone Age Man it is 7c+.",""),
 ("27","Neolithic Man","6b","t","From the right side of the cave under the heather, traverse the back to the break on the left, round the nose and up the slab as 22.",""),
 ("28","Cave Dweller","7a+","t","Classic left-to-right lip traverse: up Axe Head to the break, along the lip, finish up Lost Arrowhead.",""),
])
B("central","crucifix","Crucifix Boulder",42,112,12,5,0,"On the edge of the northern escarpment behind a big oak tree.",[
 ("29","Christmas Time","4","","Left of the main boulder: faint arête past two breaks to a good hold and an awkward mantel.",""),
 ("30","","6a","","Arête at the left end of the boulder.","Name hidden and grade only partly visible (looks like 6a)"),
 ("31","","6a+","","Middle of the wall, avoiding the crack.","Name hidden and grade only partly visible (looks like 6a)"),
 ("32","Crucifix Crack","5","","The crack.",""),
 ("33","","5","","Two-finger pocket then up right of Crucifix Crack.",""),
 ("34","","6c","t","From the left arête, traverse right to the crack and the break.",""),
])
B("central","oyster-rock","Oyster Rock (Wall Boulder)",110,98,8,5,0,"Boulder cut through by the wall, halfway up the north side of the valley, across the track from Crucifix Boulder.",[
 ("35","Oyster Traverse","6a","t","Lip traverse from the right, finishing on the wall.",""),
])
B("central","boulder-in-the-woods","Boulder in the Woods",190,52,6,4,0,"Well hidden in the woods and often damp, but a good problem.",[
 ("36","","7a","t","Right of a short chimney, low left-to-right traverse across the central groove (the crux), round the arête past the tree.",""),
])

B("central","gate-boulder","Boulder by the Gate",58,-28,8,5,0,"The undercut boulder down on the right as you come through the gate from the Bolam side. Also called the First Boulder.",[
 ("37","Gateway Roof","7a","t","Traverse the lip. Getting across the stain in the middle is the hard part.","Name from Rockfax, matched by its place in the list and its grade"),
])
B("central","undercut-walls","Undercut Walls",-16,-28,22,6,0,"Undercut walls about 100m up the valley from the Boulder by the Gate.",[
 ("38","","6a","t","Traverse the two right-hand boulders from left to right. The step across from one to the other is the crux.",""),
 ("39","","6a","t","From the crack at the left end, traverse right and finish at the grassy break.",""),
])
B("central","mrs-mops","Mrs Mops",27,22,10,5,0,"A neglected wall with some easier climbs.",[
 ("40","","3+","","Easy line up the pockets.",""),
 ("41","","4","","Just right of 40: the wall left of the obvious crack, using crimps only.",""),
 ("42","","3+","","The crack.",""),
 ("43","","4+","","Start just left of the right end of the buttress with hands in the bottom break, trend left and finish up the wall right of the crack.",""),
])
B("central","ravine-slab","The Ravine, Low Slab",-17,80,14,6,0,"Low slab and boulder at the right (east) end of The Ravine, just down from Lost Arrowhead.",[
 ("44","Shallow Groove","4","","The shallow groove.","Number hidden by the page fold, taken from the order on the page"),
 ("45","Pocket Wall","4","","The wall by way of the big pocket.","Number and start of name hidden by the page fold"),
 ("46","Side Wall","3+","","Follow the line of good crimps.","Number and start of name hidden by the page fold"),
 ("47","Hidden Crack","5","","The crack behind the boulder.","Number and start of name hidden by the page fold"),
 ("48","Young's Arête","6b","","The short arête next to the boulder.","Number and start of name hidden by the page fold"),
])
B("central","ravine-wall","The Ravine, Main Wall",-52,82,34,7,0,"South-facing wall below Lost Arrowhead, with more eliminates squeezed between the listed lines. The slab right of Shallow Groove has many lines, easier the further right you go.",[
 ("49","Easy Wall","4","","The wall just left of the corner crack.",""),
 ("50","Crack One","5","s","Sit start, then up the crack without using the big block.",""),
 ("50a","No Need for Speed","7a","s","Link: start just left of 50 and finish up 51. Recommended.",""),
 ("51","Smooth Wall","7a","","The wall on poor sloping holds.",""),
 ("52","Crack Two","4","","The left-hand crack.",""),
 ("52a","Buford T Justice","6b+","","The smooth wall just left of the crack, hard on the grip.",""),
 ("53","Pocket Wall","5+","","The wall past a good pocket.",""),
 ("54","","5+","","Wall right of the hueco, trending right to the top.",""),
 ("55","Way Cool","5","","The wall using the big hueco.",""),
 ("56","","5+","","Next wall left, with a nasty top-out.",""),
 ("57","","5","","The wall further left again.",""),
 ("LT","Low Level Traverse","4+","t","Traverse along the wall at low level.",""),
 ("MT","Mid Level Traverse","4+","t","Traverse along the wall at the height of the hole.",""),
])
B("central","big-birch-edge","The Big Birch, Escarpment",-112,40,30,6,0,"Overgrown but worth a look, below a birch on top of the escarpment. Look for the two large birch trees.",[
 ("58","","6a","s","Sit start to the left arête.",""),
 ("59","","6a","s","Sit start with the left hand on a pinch on the arête and the right on a sloper, reach a two-finger pocket, then another pocket on the lip and mantel.",""),
 ("60","","6b","s","Sit start, the right arête. A low traverse from left to right finishing up this arête is 6c.",""),
 ("61","","4+","s","About 10m right. Sit start on the block in the cave facing the left wall, move left out of the cave, then back right to top out over the lip.",""),
 ("62","","5","s","Sit start, the wall left of the fluting.",""),
 ("63","","4","","The four clear flutings, keeping off the ledge on the left. 5 from a sit start.",""),
])
B("central","big-birch","The Big Birch Boulder",-94,34,10,6,0,"The boulder next to the big birch tree.",[
 ("64","","5","t","Low-level traverse from left to right.",""),
 ("65","","6a","s","Sit start to the break, then up for a sloper and mantel. Easier if you use the left arête.",""),
 ("66","Branch Left","6a","","Start just left of the branch and go straight up.",""),
 ("67","Branch Right","6b","","From the undercuts just right of the branch, slap for a sloper, then expect an awkward landing on the slab or the ground.",""),
 ("68","","5+","s","Sit start under the nose at the right end and mantel to finish.",""),
 ("69","Last of the Summer Wine","7a","t","From the flat hold right of the right arête, move down and round the nose, traverse left with hands on top past the tree without touching it, and on to the left arête to finish as for 65.","Number partly hidden by glare"),
])
B("central","big-birch-east","The Big Birch, East Boulders",-80,38,10,6,0,"Boulders just east of the Big Birch boulder.",[
 ("70","The Weasel","5+","s","Sit start from the layaway 2m left of the arête, move right round the nose with hands below the top, and finish at the top end of the boulder.","Number and grade partly hidden by glare; name from Rockfax"),
 ("71","The Shelf","5","s","Under the roof to the right: sit start just right of the block on the ground, up and left to stand on the jutting shelf.",""),
 ("72","The Mantel","7a+","s","Sit start to the lip. With luck you finish on top rather than on the ground.",""),
])

# ---------------- WESTERN EDGES ----------------
B("western","font-boulder","Font Boulder",-430,22,14,8,10,"Always clean and well chalked. The shelf is out of bounds for every traverse.",[
 ("1","Bleaustard","6a","","Up to the crack, then finger locks and jams.",""),
 ("2","Purely Belter","7b","","Hard bulge right of the crack. If it feels easy you are too far right.",""),
 ("3","Surprising Solution","7a","","Easier bulge 2m right of the crack.","Start of name cut off by the page fold"),
 ("4","Incipient Crack","6a+","","Hanging crack from standing. Sit start from the pedestal left of the lower hairline crack is 7a.",""),
 ("5","","6a","","Wall right of Incipient Crack from standing. Sit start at the knee-height pocket, up and left to the break, is 6b.",""),
 ("6","Short Crack","5","","The crack using hands only.","Start of name cut off by the page fold"),
 ("7","Little Prow","6a","s","The prow from a sit start.",""),
 ("8","Cuvier","6a+","","From the break under the roof at the right end, gain holds above the lip and mantel. No bridging.","Start of name cut off by the page fold"),
 ("9","Final Prow","4+","","Arête just right of the crack.",""),
 ("10","Gnarly Start","7a","t","Rarely repeated traverse from the far left, hands under the top, to the crack, then as 11 and reverse 12.",""),
 ("11","Font Traverse","6c","t","Start as 1, traverse to finish up Incipient Crack. A Shaftoe classic. Keeping hands below the break is 7a+.",""),
 ("12","Reverse Traverse","6b","t","From just left of Cuvier traverse left to finish up Incipient Crack. 11 then 12 reversed is the Classic Link, 6c+.",""),
 ("13","Top Traverse","6a","t","Hand traverse the top past the crack to the heather ledge.",""),
])
B("western","the-business","The Business",-385,8,9,5,0,"Barrel-shaped flat-topped boulder about 50m up the valley from Font Boulder.",[
 ("14","","7a","st","Sit start left, traverse low and right to a big pocket, gain the lip and go right to a mantel.",""),
 ("15","","7a","t","From a round layaway at the right end, feet on the boulder, traverse left to the pocket and mantel over the nose.",""),
])
B("western","mini-obelisk","Mini Obelisk",-372,-14,4,4,45,"Pyramid-shaped boulder opposite The Business.",[
 ("23","Cliff's Slab","4","","Middle of the slab.",""),
])
B("western","astro","Astro",-395,-16,6,4,0,"First boulder on the right side of the valley up from Font, topped with turf.",[
 ("24","Astro Traverse","7a","t","Lip traverse left to right with feet on the back.",""),
])
B("western","stolen-from-ivor","Stolen from Ivor",-330,-8,10,6,0,"Flat-topped boulder with a notch in the middle, about 100m from Font.",[
 ("16","Groove One","5+","s","Sit start under the roof, reach crimps and top out.",""),
 ("17","Groove Two","5+","","Hanging start on the lower holds, then to the top.",""),
 ("18","Groove Three","5+","","Hanging start, then to the top.",""),
 ("19","Top Traverse","6c","t","From the left corner, traverse right along the lip.",""),
 ("20","Starting Something","6c","t","From the left corner, traverse right under the lip and finish up 16.",""),
 ("21","Stolen from Ivor","6c","t","From the hanging groove (16), crimp right under the lip to the end.",""),
 ("22","Stealing it Back","7a+","t","Problem 20 into problem 21 to the end.",""),
])
B("western","hair-lip","Hair Lip",-352,-52,8,4,0,"Flat-topped boulder set into the hillside 100m east of Smith's Rocks, with a crack near the middle.",[
 ("25","Hair Lip Traverse","6a","t","Lip leftwards to the crack, rest, then across the wall. Feet above the lip.",""),
 ("26","","5+","t","Same traverse with feet on the back wall.",""),
])
B("western","smiths-rocks","Smith's Rocks",-452,-55,24,7,-5,"A ridge of boulders running west to east, 20m north of Turtle Rock.",[
 ("27","Smith's Rocks Traverse","7a","t","Excellent. From the right end, go left under the lip to the arch, across the scooped wall low, then over a big gap to the last boulder.",""),
 ("28","The Lip","7a","t","From the hand jam, traverse the lip above the scooped wall.",""),
 ("29","The Scoop","6b","s","The scooped wall from a sit start.",""),
 ("30","The Mask","6c+","s","Pinch up the arête from a sit start.",""),
 ("31","The Crack","4","","The easy crack.",""),
 ("31a","Milk and Cookies","6a+","s","The slab from a sit start.",""),
 ("31b","Knee Cracker","6a+","","The small block, from the pocket on the left.",""),
 ("32","The Bunker","6b","s","In the gully behind the arête: undercut to a pocket at 3m and top out.",""),
 ("33","The Edge","6a","","Left arête of The Bunker.",""),
 ("34","Weasels Ripped my Flesh","6c","","Good hold, long move left to the lip and a small pocket, round the overhang onto the face.","First letter of name cut off"),
 ("35","Classic Arête","4","","Well-shaped arête. Sit start is 6b with an awkward pull round.","Start of name cut off"),
 ("36","Clamp","5+","","Left pinnacle from a crouch.",""),
 ("37","City of Sand","6b","","Right pinnacle, carefully.","Start of name cut off"),
 ("38","","6c","t","Left side of the undercut slab and crack, along slopers to finish up the arête.",""),
 ("39","Pebble Slab","6c","","Straight up the middle of the slab.","Start of name cut off"),
 ("40","Proposal","6c","","Lie-down start under the prow, feet on the thin plate, pinch out. Using the good edges low down is a desperate 7c.","Start of name cut off"),
])
B("western","turtle-rock","Turtle Rock",-458,-84,14,8,0,"The huge neb on the western edge of Shaftoe. The SW face also has a route, Galapagos Turtle (E5).",[
 ("41","Turtle's Flipper Left-Hand","5","s","Sit start up to the horizontal break, then up and left to good holds.",""),
 ("42","Turtle's Flipper Right-Hand","5","","As 41, then out right from the break to an awkward top out.",""),
 ("43","","6a","s","Sit start under the roof, up and left under it to good holds, hard mantel onto the ledge and slab.",""),
 ("44","Underbelly","4+","t","Follow the horizontal break under the turtle left to right and back.",""),
 ("45","Boody Gold","6c","j","Jump for two lip holds, move left to the boss and rock over back right.",""),
 ("46","Blood Sport","8a+","","From the back wall, power across the roof to the hole at the lip, then the break, then the lip. The most sought-after line here.",""),
 ("47","Soft Centre","6a","","Reach the break, gain the lip, go right to a boss and mantel.",""),
 ("48","The Boss","7b","j","Jump to slots 0.5m right of Soft Centre, high foot, small edge, slap for the top.",""),
 ("49","Hard Shell","6c+","","Overhanging wall bridging across the groove, no hands on the right wall.",""),
 ("50","Darkness Beckons","6a+","","Wall just right of the overhanging groove.",""),
])
B("western","neb-boulder","Neb Boulder",-452,-112,14,7,0,"The smaller neb, 8m south of Turtle Rock. Probably the most climbed boulder at Shaftoe.",[
 ("51","Power is Nothing without Control","7c","t","From the big hold on the left, traverse the lip of the roof round the nose to a pocket and mantel as 54.",""),
 ("52","","7b","s","Sit start on a small ledge at 0.5m, rock over to a small hold and the top.",""),
 ("53","Crease Classic","6c","s","Sit start under the roof, pull out and follow the crease up the middle of the wall.",""),
 ("54","Broken Hearts are for Assholes","7a+","s","Sit start, cross the roof left of The Neb Roof.",""),
 ("55","The Neb Roof","6c+","s","Sit start at the pedestal at the back, straight out across the roof.",""),
 ("56","The Original","6a+","s","Sit start under the roof, out to the lip and a flat hold, follow it left to the big pocket and mantel.",""),
 ("57","Perverse Classic","6c","","Start as 56, up to the rounded break, left along it to a hand jam and up.",""),
 ("58","","6a","","Start as 56, straight up past the flat hold and slopers.",""),
 ("59","","5+","","Start as 56, along the break to the next hold then up and left.",""),
 ("60","Sloper Masterclass","6a+","","Start as 56, then right along the rounded breaks to the top. Lots of variations, all slopers.",""),
 ("61","","6b","","Start as 56, right along a series of rounded breaks to stand in a big pocket and top out.",""),
 ("62","","6b","s","Sit start at the right end of the roof on the flat hold, straight up.","Grade partly hidden by glare (looks like 6b)"),
 ("63","Aside","6b","s","Sit start in the big pocket, straight up to a mantel.",""),
 ("64","Pure Endurance","7a","st","From the far right in the big pocket, traverse left along the rounded break past the jam and pocket, mantel on the short west face.",""),
 ("65","Flat Out","7a","s","Sit start as Aside, up to the crease and slopers left to the left arête, hands above the break.",""),
])

# ---------------- SHAFTOE SUMMIT ----------------
B("summit","dead-pine","Dead Pine Buttress",-239,-178,18,6,-10,"Flat-topped buttress with a full-length roof, split by a chimney, with a dead pine at its right end. The first two problems are on the neb just left of it.",[
 ("1","The Alligator","5+","s","Sit start at the back of the roof on the left, climb out and over the nose.",""),
 ("2","The Alligator Right-Hand","6b","","Hands and feet on the right side only.",""),
 ("3","Lightning Never Strikes Twice","5","s","Sit start on surprisingly good holds.",""),
 ("4","","6b","","Hanging start, feet on the back wall, from the large flake.",""),
 ("5","","6b","","Hanging start from the spike.",""),
 ("6","","6b","","Hanging start, up the middle of the buttress.",""),
 ("7","","6b","","Hanging start from the ledge.",""),
 ("8","","6b","","Hanging start from the block.",""),
 ("9","","6b","t","From the chimney, traverse the lip right and finish up 8.",""),
 ("10","","5+","t","Left to right under the lip. Stays dry in the rain.",""),
])
B("summit","pygmy-rocks","Pygmy Rocks",-305,-160,7,5,0,"Jumble of boulders 20m before Dishpan Alley.",[
 ("11","Pygmy Traverse","6a","st","Sit start on the left, traverse the lip right round the arête as far as you can, then mantel.",""),
 ("12","","6a","st","Sit start under the left arête, traverse right to the crack.",""),
 ("13","The Cow","6a","t","Right to left along the slot under the top, finishing on the slab via a pocket.",""),
])
B("summit","the-prow-summit","The Prow",-345,-172,4,4,0,"Small, very undercut boulder just left of Dishpan Alley.",[
 ("14","","7a","t","Hard traverse of the boulder, left to right.",""),
 ("15","","7a","t","Harder traverse, right to left.",""),
])
B("summit","dishpan-alley","Dishpan Alley",-326,-178,26,6,-5,"Small escarpment on the south rim of the main valley, with a crack right of centre and an overhanging nose at the right end. A popular warm-up spot.",[
 ("16","East Wall","5+","s","Sit start on good holds at the left end of the lip, big lock and mantel.",""),
 ("17","Arête","6a","s","Sit start left of the arête, awkward move up and right.",""),
 ("18","","5","s","Crouching start 2m right of the arête on a lip crimp, up and left.",""),
 ("19","","5","s","Crouching start under the roof 3m right of the arête, to a pocket or dish, then up.",""),
 ("20","","5+","","Wall just left of the crack, avoiding it.",""),
 ("21","","5+","","From the undercling under the roof, right side of the crack using the big pocket.",""),
 ("22","","6a","","0.5m right of the crack using the pocket.",""),
 ("23","Rising Cramp","7a","t","From the crack, right to the hole, wedge into the scoop, then crimp across to the arête.","Start of name cut off"),
 ("24","Rising Damp","6b","","Under the roof, slopers right of the corner and the edge of the ramp, mantel up and right.","Start of name cut off"),
 ("25","Corner","4+","","The corner.","Start of name cut off"),
 ("26","Mantel Madness","6c+","","Left of the right arête, good holds over the roof to a sloping ledge and a hard mantel.",""),
 ("27","","?","","The undercut right arête.","Name and grade hidden in the shadow"),
 ("28","Dishpan Alley Traverse","6a","t","From round the corner left of 16, hand traverse past a finger-lock and layback to the right arête.",""),
])
B("summit","west-wall","West Wall",-300,-190,8,5,0,"Short wall at the right end of Dishpan Alley.",[
 ("29","","6a","s","Sit start 1m left of the Blunt Nose, up to the break and crimps to good holds.",""),
 ("30","Blunt Nose","6a+","s","Sit start to the break, then just right of the arête to slopers.",""),
 ("31","","5+","s","Sit start 1m right on the break, to a second break and the top. Long arms help.",""),
 ("32","","4+","","From the far right end of the ledge, straight up on good holds.",""),
 ("33","","6c","t","From the ledge left of 29, along the half-height break, then back left above the ledge to finish up 29.",""),
])
B("summit","main-buttress","Main Buttress",-401,-190,18,7,0,"Prominent buttress with a 3m roof about 1m off the ground. Lots of good problems, mostly on slopers.",[
 ("34","","5+","","Left arête. Sit start is 6a.",""),
 ("35","Viagra","6c","","Shallow groove, then left to a good hold on the arête. Sit start is 7b.",""),
 ("36","Viagra Plus","6c","","Rib right of the arête to a good hold. Sit start is 7b.",""),
 ("37","Sloppy Ploppin","6c","","Hanging start on slopers right of 36, over the bulge. Sloppy Ploppin SS, from the lip of Vorsprung durch Technik, is 7c+.",""),
 ("38","Central Wall","7b+","","Middle of the wall. Starting holds are about 2.4m up, so height helps.",""),
 ("38a","Vorsprung Durch Technik","8a","s","Sit start deep in the cave, use the flake to cross the roof and turn the lip on small holds. A Shaftoe classic.","Listed in the book without its own number"),
 ("39","Main Wall","6c+","","Scoop right of centre, moving right at the top. Main Wall SS, from the back of the cave across the roof with a one-finger pocket, is 7b+.",""),
 ("40","Timmy Tip Toes","7b","","Right arête, mostly on its right side, from a good flake under the roof.",""),
 ("41","","7a+","","Faint rib left of the scoop.",""),
 ("42","Magic Fluting","5","","Big fluting to a positive hold, saving the hardest move for last.",""),
 ("43","","5+","","Wall 1m right of the fluting on small holds.",""),
 ("44","Main Buttress Traverse","6c","t","From the big flutings on the right, traverse left with feet above the lip, finish up 36.","Name from Rockfax, matched by its place in the list and its grade"),
])
B("summit","fluted-wall","Fluted Wall",-385,-200,8,4,0,"Back wall between Main Buttress and The Cob.",[
 ("45","The Wasp","6b+","","Wall trending right at the top. Tricky; the finish is not as well protected as it looks, take care.","Start of name cut off"),
 ("46","The Sting","6a+","","Up the flutings with a tricky move to a good hold.","Start of name cut off"),
 ("47","Buzzing","6c","","Scoop left of the arête. Sit start with a pinch on the arête is 7a.","Start of name cut off"),
 ("FW","Fluted Wall Traverse","6b+","t","Traverse leftwards from 49 past the flutings to 43.","Number hidden in the shadow"),
])
B("summit","the-cob","The Cob",-372,-208,12,8,0,"Leaf-shaped buttress right of the Fluted Wall. Its back forms one side of Ship's Bait Cabin.",[
 ("48","","5+","","Right wall of the gully just left of the arête.",""),
 ("49","Cob Arête","5+","","The photogenic arête.",""),
 ("50","","6a","","Good pockets right of the arête to a hold up and right. Popular.",""),
 ("51","Hound Dog","7a+","","Two-finger pocket at 3m, reached via an undercut. Often tried, rarely topped.",""),
 ("52","Killer Queen","6c","","Undercut flake left of a mono to a poor hold, then a positive one to mantel.",""),
 ("53","Hip Hop","6b","","From the right end, use an undercut to reach an obvious pocket at 3m and top out.",""),
 ("54","Korn on the Cob","6b","s","Sit start 1m right of 53 on a side-pull, long reach to a flat hold, right to an edge, onto the slab.",""),
 ("55","Honeycomb Wall Traverse","6c","t","Front face of The Cob from the left arête (49) to beyond 54.",""),
 ("56","The Link","6c","t","Traverse the west face of The Cob.",""),
 ("57","Bait Boxed","7a","t","Full girdle of The Cob, taking in 55, 56 and 61.",""),
 ("58","","4","s","Back of The Cob: sit start to the arête at the left end.",""),
 ("59","","4","s","Sit start under the hanging corner in the middle of the slab.",""),
 ("60","","5","","Hanging start to the undercut arête, awkward mantel over the nose.",""),
 ("61","The Thug","5+","t","Lip of the roof from 58 to 60.",""),
])
B("summit","galley-wall","Galley Wall (Ship's Bait Cabin)",-368,-222,14,4,0,"Wall facing the back of The Cob, in the small boxed canyon called Ship's Bait Cabin. Many eliminates have been climbed here.",[
 ("62","The Technician","5+","t","From left of the corner, traverse the right wall left to right with hands under the top.",""),
 ("63","Port","5+","s","Sit start right of the crack, up to a small flake and the top. Avoiding the back wall is the crux.",""),
 ("64","Galley Wall","4+","","Middle of the wall to an undercut flake. Sit start with a side-pull and tiny pinch is 6a.",""),
 ("64a","Wolf","6b+","s","Sit start, undercut up to two small bumps, then the top.",""),
 ("65","Starboard","5","s","Sit start in the good break on the right of the wall, past two pockets.",""),
 ("66","Bow Wave","6a","","Short prow in the corner.",""),
 ("67","Lost Crack","4+","","Rough crack. Sit start is 5+.",""),
])
B("summit","cow-pat","Cow Pat Buttress",-476,-205,8,4,0,"10m west of and just below The Cob, with a break under the lip. One of three small buttresses above Shaftoe Grange Farm.",[
 ("68","Cow Pat","5+","t","From the big ledge on the right, follow the break left, then the lip back right.",""),
])
B("summit","grange-farm","Grange Farm Buttress",-509,-274,7,4,0,"Neglected boulder 20m right of Cow Pat, set into the hillside on the escarpment north-east of Shaftoe Grange Farm.",[
 ("69","","4+","t","Lip traverse left to right.",""),
 ("70","","5","s","Sit start, cross the roof at its widest to a mantel.",""),
 ("71","","5+","s","Sit start, cross the roof at its narrowest to a mantel.",""),
 ("72","","6c","t","Right to left, anything below the lip and above the ledge.",""),
])
B("summit","provence","Provence Buttress",-545,-316,8,4,0,"90m right of Grange Farm Buttress, directly above Shaftoe Grange Farm.",[
 ("73","A Week in Provence","7b+","t","From the layaway left of the nose, traverse right below the lip to a mantel.",""),
 ("74","Provence Traverse","5+","t","Traverse the lip.",""),
 ("75","Weakling in Provence","6a","s","Sit start at the back of the roof, undercling out to a good hold and mantel.",""),
])

# ---------------- SHAFTOE SOUTH ----------------
B("south","rudders","Rudder's Boulders",-180,-548,14,5,0,"Undercut pancake boulders on the plateau, with two more undercut boulders lower down the slope.",[
 ("1","Rudyard","5+","t","From the left end of the undercut pancake, follow the lip, exit the groove awkwardly and keep going right to a mantel.",""),
 ("2","","5+","t","Lower right-hand boulder: from the gap between the boulders, traverse the lip to the left end.",""),
 ("3","","5+","t","Lower left-hand boulder: one foot in the right-hand crack, traverse the lip to the top.",""),
 ("4","","6a","s","Sit start, a hand in either crack, reach the lip and mantel. Stay between the cracks.",""),
])
B("south","seadog","The Seadog Boulder",-238,-622,6,4,0,"About 100m from the Punch Bowl, on the other side of the track from Rudder's Boulders.",[
 ("5","Seadog Traverse","6b","t","Both hands on the flat hold at the left end, traverse right and mantel.",""),
])
B("south","punch-bowl","Punch Bowl",-380,-620,12,7,0,"On the plateau directly above Cave Buttress, with a water-worn channel.",[
 ("6","Black Pudding","7a","t","From the left side between the detached boulder and the main boulder, traverse right below the lip to the big hold by the detached boulder on the right.","Start of name cut off"),
 ("7","","6c","t","Start as Black Pudding, traverse round avoiding the detached boulder, finish right of the arête.",""),
 ("8","The Real Duvel 8.5%","6c","","Halfway between the left boulder and the channel, power over the bulge.",""),
 ("9","","5+","t","From the water-worn channel, traverse right on the lip top to the right arête.",""),
 ("10","","5+","s","Sit start under the water channel.",""),
 ("11","Canine","6a","s","Sit start right of the water channel using the 'K' and '9' holds to the top.",""),
 ("12","","6c","s","Sit start with both hands on the flake under the roof, powerful moves up and over.",""),
])
B("south","cave-buttress","Cave Buttress",-364,-650,16,7,0,"The big cave under the Punch Bowl, reached most easily by old steps to the east.",[
 ("13","Flake Crack","5","","Awkward layback flake 5m left of the cave mouth.",""),
 ("14","Pocket Rocket","7a","","Wall right of Flake Crack on a good pocket and a small crimpy layaway.",""),
 ("15","Orangutan","6c","","Left of the corner with a pocket each hand, left round the roof. Watch the landing.",""),
 ("16","Feeding the Baboons","7a","","From the left corner 2m into the cave, underclings with feet on the wall across the roof to the right-hand crack.",""),
 ("17","The Eyes","6c","","From the hand jam left of the eyes at the back, along the left crack then swing into the right crack. Starting up The Eyes and finishing up Orangutan is 7b.",""),
 ("18","Right-hand Crack","7a+","","From the back of the cave out to the lip and round it, finishing as 19.",""),
 ("19","The Wall","4+","","Wall right of the cave.","Name partly hidden by glare"),
])
B("south","little-dal","Little Dal Buttresses",-283,-636,14,6,0,"Two buttresses with a big tree at their right end.",[
 ("20","The Scoop","4","","Arête and scoop.",""),
 ("21","The Wall","6b","","Wall left of the crack: mantel from the head-height hold to the fluting. Reach helps.",""),
 ("22","Little Crack","4","","From a short corner, up the crack.",""),
 ("23","Little John","5","","From the shelf up the scoop.",""),
 ("24","Slab Arête","4","","Short slab and arête.",""),
 ("25","Little and Often","6b+","s","Sit start, crozzly holds to the break, long reach to the crack, awkward finish.",""),
 ("26","","4+","t","Right to left across the scoop.",""),
])
B("south","long-wall","Long Wall",-225,-638,14,4,0,"Long traversing wall 30m right of Little Dal.",[
 ("27","Long Wall Traverse","5+","t","Low traverse of the break. Along the lip of the roof is 7a.",""),
 ("27a","Long Wall Mantel","7a","","Pull over the block to an awkward mantel.",""),
])
B("south","wickerman","Wickerman Boulder",-241,-650,4,3,0,"Boulder below the Long Wall.",[
 ("27b","Wickerman","6b","","Mantel onto the boulder.",""),
])
B("south","minuscule-matterhorn","Minuscule Matterhorn",-198,-678,4,4,45,"Small pointed boulder at about the same height as Café Noir.",[
 ("28","","4","","The arête and crack.",""),
 ("29","","4","","Wall right of the crack.",""),
])
B("south","central-alcove","Central Alcove",-122,-656,14,6,0,"Alcove set a few metres up the hillside between Café Noir and Two Tier Boulder, with a crack and big chockstone in the middle.",[
 ("30","Short Left Wall","4","","Short left wall of the alcove.","Name from Rockfax, matched by its place in the list and its grade"),
 ("31","Jam Crack","4","","Short crack.",""),
 ("32","Pegasus","4+","","Wall right of the crack past the old peg.",""),
 ("33","Behind the Tree","5+","","Wall right behind the tree.","Name from Rockfax, matched by its place in the list and its grade"),
 ("34","Left of Chimney","4","","Left wall of the chockstone chimney by the arête. No bridging.","Name from Rockfax, matched by its place in the list and its grade"),
 ("35","Right of Chimney","5+","","Right wall of the chimney. No bridging.","Name from Rockfax, matched by its place in the list and its grade"),
 ("36","Antler and Deck","7a","","Arête to the right, steep moves to the antler-shaped feature, then jugs and flutes.",""),
 ("37","Butch Catch-Me and the Campus Board Kid","7a","s","Sit start, crimps from a good lip hold up and right to slap for a jug set back from the edge.",""),
])
B("south","two-tier","Two Tier Boulder",-77,-658,14,8,0,"Deserves more traffic, and very sheltered from cold northerlies in winter.",[
 ("38","A Tale of Two Cities","6a","t","Upper tier: from the block behind the lower tier, hands in the crack, finish on the right-hand block.","Start of name cut off"),
 ("38x","","?","","Left side of the lower wall.","Number, name and grade hidden in the shadow"),
 ("39","Tears in Heaven","5+","","Left end of the boulder; hard pull off the ground to good holds.","Number hidden, assumed 39"),
 ("40","River of Tears","7b+","","Under the arête with right hand on a layaway, pull on and follow undercuts to finish up the flake.",""),
 ("41","Tears on the Dance Floor","6b+","","Rounded arête left of the groove.","Number hidden, assumed 41"),
 ("42","Tuppence Ha'penny","4+","","Corner groove up and round the tree.","Number hidden, assumed 42"),
 ("43","Edge of Sanity","5+","s","Sit start to the left arête of the slanting crack.",""),
 ("44","Two Tier Crack","4+","s","Sit start up the crack to the ledge, escape left.",""),
 ("45","Tears for Fears","5","s","Sit start to the right arête of the crack.",""),
 ("46","Two Tears","7b","s","Sit start under the bulge, up the left crease, hard finish.",""),
 ("47","Two a Penny","5+","s","Sit start at the right end just right of the bulge, right crease to the top.",""),
])
B("south","cyclops","Cyclops Buttress",-27,-643,8,6,0,"80m right of Two Tier Boulder.",[
 ("48","Green Wall","4","","Left side of the buttress.",""),
 ("49","Left Arête","4+","","The left arête.",""),
 ("50","Cyclops Wall","5","","Straight up to the eye.",""),
 ("51","Right Arête","5","","Right arête. A bit crumbly, take care.",""),
 ("52","The Scoop","4+","","Scoop just right of Right Arête. The better problem.",""),
 ("53","Side Wall","5","","Short wall to a tricky mantel.",""),
])
B("south","halfway-house","Halfway House",-337,-703,5,4,0,"Halfway down the hillside between the arête right of Cave Buttress and the roadside boulders.",[
 ("54","","5","s","Sit start at the top right corner on two slopers, up and right.",""),
 ("55","","5","s","Sit start under the undercut arête and follow it.",""),
])
B("south","roadside","Roadside Boulder",-344,-752,10,7,0,"Big boulder at the bottom near the track. Roadside Face problems go left to right; three more are on the Hillside Face behind.",[
 ("56","Slim Shady","6a","","Arête left of the big crack. Sit start is 7a.","Start of name cut off"),
 ("57","Intermittent Crack","6a","","Broken crack splitting the left edge of the boulder.","Start of name cut off"),
 ("58","Not to be Taken Away","5+","","Flake on the left of the front wall to the second break, long reach to finish.","Start of name cut off"),
 ("59","Roadside Wall","7c+","","Middle of the Roadside Face.","Start of name cut off"),
 ("60","Roadside Arête","5","","Just left of the right arête to good holds and jugs.","Start of name cut off"),
 ("61","","4","","Hillside Face: left arête.",""),
 ("62","","5","","Hillside Face: up to the fluting on small crimps.",""),
 ("63","","4","","Hillside Face: the easy slab on the right.",""),
])
