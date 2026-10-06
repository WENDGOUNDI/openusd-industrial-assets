from pxr import Usd, UsdGeom, Gf, Sdf

# Create a new USD stage
stage = Usd.Stage.CreateNew("conveyor.usda")

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
# Conveyor container
# -------------------------
conveyor = UsdGeom.Xform.Define(
    stage,
    "/World/Factory/Conveyor01"
)

# -------------------------
# Conveyor frame
# -------------------------
frame = UsdGeom.Cube.Define(
    stage,
    "/World/Factory/Conveyor01/Frame"
)

frame_xform = UsdGeom.Xformable(frame)

frame_xform.AddTranslateOp().Set(
    Gf.Vec3d(0, 0, 0.5)
)

frame_xform.AddScaleOp().Set(
    Gf.Vec3f(3.0, 0.8, 0.3)
)

# -------------------------
# Conveyor belt
# -------------------------
belt = UsdGeom.Cube.Define(
    stage,
    "/World/Factory/Conveyor01/Belt"
)

belt_xform = UsdGeom.Xformable(belt)

belt_xform.AddTranslateOp().Set(
    Gf.Vec3d(0, 0, 0.75)
)

belt_xform.AddScaleOp().Set(
    Gf.Vec3f(2.8, 0.7, 0.1)
)

# -------------------------
# Conveyor legs
# -------------------------
leg_positions = [
    (-2.5, -0.6, -0.1),
    (-2.5,  0.6, -0.1),
    ( 2.5, -0.6, -0.1),
    ( 2.5,  0.6, -0.1),
]

for i, position in enumerate(leg_positions, start=1):

    leg = UsdGeom.Cube.Define(
        stage,
        f"/World/Factory/Conveyor01/Leg{i}"
    )

    leg_xform = UsdGeom.Xformable(leg)

    leg_xform.AddTranslateOp().Set(
        Gf.Vec3d(*position)
    )

    leg_xform.AddScaleOp().Set(
        Gf.Vec3f(0.15, 0.15, 0.6)
    )

# -------------------------
# Conveyor rollers
# -------------------------
roller_positions = [-2.4, -1.2, 0.0, 1.2, 2.4]

for i, x in enumerate(roller_positions, start=1):

    roller = UsdGeom.Cylinder.Define(
        stage,
        f"/World/Factory/Conveyor01/Roller{i}"
    )

    roller.GetRadiusAttr().Set(0.18)
    roller.GetHeightAttr().Set(1.2)

    roller_xform = UsdGeom.Xformable(roller)

    roller_xform.AddTranslateOp().Set(
        Gf.Vec3d(x, 0, 1.0)
    )

    roller_xform.AddRotateXOp().Set(90)

# -------------------------
# Digital twin attributes
# -------------------------

conveyor_prim = conveyor.GetPrim()

status_attr = conveyor_prim.CreateAttribute(
    "conveyor:status",
    Sdf.ValueTypeNames.String
)
status_attr.Set("Running")

speed_attr = conveyor_prim.CreateAttribute(
    "conveyor:speed",
    Sdf.ValueTypeNames.Float
)
speed_attr.Set(1.2)

temperature_attr = conveyor_prim.CreateAttribute(
    "conveyor:motor_temperature",
    Sdf.ValueTypeNames.Float
)
temperature_attr.Set(45.0)

id_attr = conveyor_prim.CreateAttribute(
    "conveyor:id",
    Sdf.ValueTypeNames.String
)
id_attr.Set("CV-001")


# -------------------------
# Status indicator
# -------------------------

status_indicator = UsdGeom.Cube.Define(
    stage,
    "/World/Factory/Conveyor01/StatusIndicator"
)

status_xform = UsdGeom.Xformable(status_indicator)

status_xform.AddTranslateOp().Set(
    Gf.Vec3d(0, -1.1, 1.2)
)

status_xform.AddScaleOp().Set(
    Gf.Vec3f(0.2, 0.2, 0.2)
)

# Read current digital twin values
current_status = status_attr.Get()
current_temperature = temperature_attr.Get()

# Temperature has highest priority
if current_temperature >= 60.0:
    color = Gf.Vec3f(1.0, 0.0, 0.0)   # Red = Overheat

elif current_status == "Running":
    color = Gf.Vec3f(0.0, 1.0, 0.0)   # Green

elif current_status == "Stopped":
    color = Gf.Vec3f(1.0, 0.0, 0.0)   # Red

elif current_status == "Warning":
    color = Gf.Vec3f(1.0, 1.0, 0.0)   # Yellow

else:
    color = Gf.Vec3f(0.5, 0.5, 0.5)   # Gray

status_indicator.GetDisplayColorAttr().Set([color])

# -------------------------
# Moving product
# -------------------------

product = UsdGeom.Cube.Define(
    stage,
    "/World/Factory/Conveyor01/Product01"
)

product.GetDisplayColorAttr().Set([
    Gf.Vec3f(0.1, 0.3, 1.0)
])

product_xform = UsdGeom.Xformable(product)

translate_op = product_xform.AddTranslateOp()

product_xform.AddScaleOp().Set(
    Gf.Vec3f(0.25, 0.25, 0.25)
)

translate_op.Set(
    Gf.Vec3d(-2.5, 0, 1.45),
    time=0
)

translate_op.Set(
    Gf.Vec3d(0, 0, 1.45),
    time=90
)

translate_op.Set(
    Gf.Vec3d(2.5, 0, 1.45),
    time=180
)

stage.SetStartTimeCode(0)
stage.SetEndTimeCode(180)
stage.SetTimeCodesPerSecond(30)

# -------------------------
# Save
# -------------------------
stage.GetRootLayer().Save()