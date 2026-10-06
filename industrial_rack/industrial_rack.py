from pxr import Usd, UsdGeom, Gf, Sdf

# Create a new USD stage
stage = Usd.Stage.CreateNew("industrial_rack.usda")

# Z is the vertical/up axis
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)

# -------------------------
# World
# -------------------------
world = UsdGeom.Xform.Define(
    stage,
    "/World"
)

# -------------------------
# Factory
# -------------------------
factory = UsdGeom.Xform.Define(
    stage,
    "/World/Factory"
)

# -------------------------
# Rack01
# -------------------------
rack = UsdGeom.Xform.Define(
    stage,
    "/World/Factory/Rack01"
)

# -------------------------
# Structure
# -------------------------
structure = UsdGeom.Xform.Define(
    stage,
    "/World/Factory/Rack01/Structure"
)

# -------------------------
# Vertical posts
# -------------------------

post_positions = [
    (-2.5, -0.8, 2.0),  # Post1
    (-2.5,  0.8, 2.0),  # Post2
    ( 2.5, -0.8, 2.0),  # Post3
    ( 2.5,  0.8, 2.0),  # Post4
]

for i, position in enumerate(post_positions, start=1):

    post = UsdGeom.Cube.Define(
        stage,
        f"/World/Factory/Rack01/Structure/Post{i}"
    )

    post.GetDisplayColorAttr().Set([
    Gf.Vec3f(0.20, 0.25, 0.35)   # dark steel blue/gray
    ])

    post_xform = UsdGeom.Xformable(post)

    # Position first
    post_xform.AddTranslateOp().Set(
        Gf.Vec3d(*position)
    )

    # Make it tall and thin
    post_xform.AddScaleOp().Set(
        Gf.Vec3f(0.15, 0.15, 2.0)
    )

# -------------------------
# Shelves
# -------------------------
shelves = UsdGeom.Xform.Define(
    stage,
    "/World/Factory/Rack01/Shelves"
)

# -------------------------
# Shelves
# -------------------------

shelf_heights = [
    0.5,   # Bottom shelf
    2.0,   # Middle shelf
    3.5,   # Top shelf
]

for i, z in enumerate(shelf_heights, start=1):

    shelf = UsdGeom.Cube.Define(
        stage,
        f"/World/Factory/Rack01/Shelves/Shelf{i}"
    )

    shelf.GetDisplayColorAttr().Set([
    Gf.Vec3f(0.95, 0.45, 0.10)   # orange
    ])

    shelf_xform = UsdGeom.Xformable(shelf)

    # Position shelf
    shelf_xform.AddTranslateOp().Set(
        Gf.Vec3d(0, 0, z)
    )

    # Make it long, wide, and thin
    shelf_xform.AddScaleOp().Set(
        Gf.Vec3f(2.4, 0.75, 0.1)
    )

# -------------------------
# Beams
# -------------------------
beams = UsdGeom.Xform.Define(
    stage,
    "/World/Factory/Rack01/Beams"
)

# -------------------------
# Horizontal beams
# -------------------------

beam_heights = [
    0.5,
    2.0,
    3.5,
]

beam_depth_positions = [
    -0.8,   # Front
     0.8,   # Back
]

beam_number = 1

for z in beam_heights:

    for y in beam_depth_positions:

        beam = UsdGeom.Cube.Define(
            stage,
            f"/World/Factory/Rack01/Beams/Beam{beam_number}"
        )

        beam.GetDisplayColorAttr().Set([
        Gf.Vec3f(0.95, 0.45, 0.10)   # orange
        ])

        beam_xform = UsdGeom.Xformable(beam)

        beam_xform.AddTranslateOp().Set(
            Gf.Vec3d(0, y, z)
        )

        beam_xform.AddScaleOp().Set(
            Gf.Vec3f(2.4, 0.08, 0.15)
        )

        beam_number += 1

# -------------------------
# Pallets
# -------------------------
pallets = UsdGeom.Xform.Define(
    stage,
    "/World/Factory/Rack01/Pallets"
)

# -------------------------
# Pallet01
# -------------------------
pallet = UsdGeom.Xform.Define(
    stage,
    "/World/Factory/Rack01/Pallets/Pallet01"
)

# Pallet deck
deck = UsdGeom.Cube.Define(
    stage,
    "/World/Factory/Rack01/Pallets/Pallet01/Deck"
)

deck.GetDisplayColorAttr().Set([
    Gf.Vec3f(0.76, 0.62, 0.40)   # wood color
])

deck_xform = UsdGeom.Xformable(deck)

deck_xform.AddTranslateOp().Set(
    Gf.Vec3d(-1.1, 0, 0.75)
)

deck_xform.AddScaleOp().Set(
    Gf.Vec3f(0.8, 0.6, 0.08)
)

# Support blocks under pallet
block_positions = [
    (-1.7, 0, 0.55),
    (-1.1, 0, 0.55),
    (-0.5, 0, 0.55),
]

for i, position in enumerate(block_positions, start=1):

    block = UsdGeom.Cube.Define(
        stage,
        f"/World/Factory/Rack01/Pallets/Pallet01/Block{i}"
    )

    block.GetDisplayColorAttr().Set([
    Gf.Vec3f(0.76, 0.62, 0.40)   # wood color
    ])

    block_xform = UsdGeom.Xformable(block)

    block_xform.AddTranslateOp().Set(
        Gf.Vec3d(*position)
    )

    block_xform.AddScaleOp().Set(
        Gf.Vec3f(0.18, 0.5, 0.12)
    )

# -------------------------
# Box01 on top of Pallet01
# -------------------------

box = UsdGeom.Cube.Define(
    stage,
    "/World/Factory/Rack01/Pallets/Pallet01/Box01"
)

box.GetDisplayColorAttr().Set([
    Gf.Vec3f(0.72, 0.52, 0.30)   # cardboard brown
])

box_xform = UsdGeom.Xformable(box)

box_xform.AddTranslateOp().Set(
    Gf.Vec3d(-1.1, 0, 1.0)
)

box_xform.AddScaleOp().Set(
    Gf.Vec3f(0.45, 0.45, 0.25)
)

# -------------------------
# Save
# -------------------------
stage.GetRootLayer().Save()