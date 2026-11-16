# Problems listed on Rockfax Digital's public Shaftoe page (names, grades and area only) that are not in the
# printed guidebook pages used for this app. Each is placed on the app boulder that best fits its Rockfax area;
# exactly where on the boulder is unknown. Numbered R1, R2... per boulder.
NOTE = "From Rockfax's public list: name, grade and area only. Where it goes on the boulder is a guess."

# New small boulders between The Grindstone and Jubilee Boulder (Rockfax lists them in that order).
BOULDERS = [
    ("north", "napoleon", "Napoleon", -262, 378, 6, 4, 10, "Small boulder between The Grindstone and Jubilee Boulder. Position estimated."),
    ("north", "snowball", "Snowball", -265, 362, 5, 4, 10, "Small boulder between The Grindstone and Jubilee Boulder. Position estimated."),
    ("north", "squealer", "Squealer", -264, 346, 5, 4, 10, "Small boulder between The Grindstone and Jubilee Boulder. Position estimated."),
]

EXTRA = [
    ("cave-buttress", "Surface to Air Missile", "7a"),
    ("dishpan-alley", "Crimps", "6a"), ("dishpan-alley", "Troy's Eliminate", "6b"), ("dishpan-alley", "There and Back", "6c"),
    ("pudding-stone", "Pudding Filler", "4"), ("north-buttress", "Small Wall", "4"),
    ("font-boulder", "Strenuous Solution", "7a"), ("font-boulder", "Incipient Crack Sit", "6b+"), ("font-boulder", "Font Boulder 5 Sit", "6b"),
    ("wickerman", "Wicker Arete", "6c"), ("wickerman", "Wickerman Warm-up", "4"),
    ("long-wall", "Long Wall Lip Traverse", "7a"), ("long-wall", "Flesh to Nothing", "6c"), ("long-wall", "Desperate Times", "6c+"),
    ("long-wall", "3 Fingers, 1 Pebble", "6c"), ("long-wall", "The Brothers Grimm", "6a"), ("long-wall", "Filthy Gem", "7a"),
    ("long-wall", "Hidden Gem", "6b+"), ("long-wall", "Green Wall Sit", "6b+"),
    ("lost-arrowhead-cave", "Broken Arrowhead", "7a+"), ("lost-arrowhead-cave", "California Man", "7c"),
    ("lost-arrowhead-cave", "Stoned & Lost Man", "6c+"), ("lost-arrowhead-cave", "Paralytic Man", "6b+"),
    ("main-buttress", "Viagra Plus Sit", "7a+"), ("main-buttress", "Sloppy Ploppin Sit", "7c+"), ("main-buttress", "Slug Life", "8a+"),
    ("main-buttress", "Main Wall Sit", "7b+"),
    ("fluted-wall", "Left Rib", "4"), ("fluted-wall", "Right Rib", "4"), ("fluted-wall", "Buzzing Sit", "7a"),
    ("the-cob", "The Cob Right Start", "5"),
    ("galley-wall", "Green Slider", "3"), ("galley-wall", "Lip Traverse", "4"),
    ("neb-boulder", "Power Arete", "7b"), ("neb-boulder", "All Powered Out!", "7c+"), ("neb-boulder", "Honorary Gardom's", "7b"),
    ("arete-land", "Oh Grow Up", "7a+"), ("arete-land", "The Long Reach SDS", "7a"), ("arete-land", "Arete Land Traverse", "6a+"),
    ("arete-land", "Throw the Dice", "7a"), ("arete-land", "Shaftoe Bloc", "7a"), ("arete-land", "Twenty One Again", "5+"),
    ("punishment-block", "Do You Have Nothing Better To Do?", "7b+"), ("punishment-block", "The Punisher", "8a+"),
    ("punishment-block", "Punishment Mantel", "6c"),
    ("napoleon", "Napoleon 1", "4+"), ("napoleon", "Napoleon 2", "4+"), ("napoleon", "Napoleon 3", "3"),
    ("snowball", "Snowball 1", "4+"), ("snowball", "Snowball 2", "5"),
    ("squealer", "Squealer 1", "3"), ("squealer", "Squealer 2", "3+"),
    ("punch-bowl", "The Real Duvel 8.5% Extension", "6c+"), ("punch-bowl", "Mantel Pudding", "7a+"),
    ("punch-bowl", "Mantel Pudding Alternative", "7a"), ("punch-bowl", "Duvel 6.66%", "7a"), ("punch-bowl", "Belgian Blond", "7a"),
    ("punch-bowl", "0% Alcohol", "7a"),
    ("roadside", "The Lip Sit", "7a+"), ("roadside", "Spinal Tap", "7c"), ("roadside", "Capability Brawn", "8b"),
    ("roadside", "Real Slim Shady Left-hand", "7b"), ("roadside", "Slim Shady Sit", "7a"), ("roadside", "Real Slim Shady", "7a+"),
    ("roadside", "King Prawn", "6a"),
    ("salters-nick", "Salt n Pepper Right", "6a+"), ("salters-nick-boulder", "Big Ear", "5+"), ("small-boulder", "Small Fry", "4+"),
    ("dead-pine", "Clueless Caiman Hunters", "6a+"),
    ("big-birch-east", "The Super Mantel", "7b"),
    ("ravine-wall", "Smoothest Wall", "6b"),
    ("ravine-slab", "No Pocket Wall", "4"), ("ravine-slab", "Crimp Wall", "4"), ("ravine-slab", "Teeter", "4+"),
    ("ravine-slab", "Pebble Dash Left", "4+"), ("ravine-slab", "Pebble Dash", "4+"), ("ravine-slab", "Thumbs", "4+"),
    ("ravine-slab", "Slab 1", "3"), ("ravine-slab", "Slab 2", "3"),
    ("rift-north", "Guns Don't Kill People", "7a+"), ("rift-north", "Rappers Do", "6c+"),
    ("turtle-rock", "Blood Sport Left-hand", "8b+"),
    ("central-alcove", "Wall Right", "6a"), ("two-tier", "Velcroman", "6c+"),
]

def flags(name):
    n = name.lower()
    return ("s" if (" sit" in n or "sds" in n) else "") + ("t" if "traverse" in n else "")

def add_to(S, B):
    for b in BOULDERS:
        B(*b, [])
    byid = {b["id"]: b for b in S}
    count = {}
    for bid, name, grade in EXTRA:
        count[bid] = count.get(bid, 0) + 1
        byid[bid]["problems"].append((f"R{count[bid]}", name, grade, flags(name), NOTE, ""))
    return len(EXTRA)
