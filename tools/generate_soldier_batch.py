import bpy, math, os
from mathutils import Vector

# War in the World — Batch 01: 10 low-poly infantry prototypes.
# Run with: blender -b --python tools/generate_soldier_batch.py
OUT = os.path.abspath("public/assets/models/soldiers")
os.makedirs(OUT, exist_ok=True)

def mat(name, color, roughness=0.82, metallic=0.0):
    m = bpy.data.materials.new(name)
    m.diffuse_color = (*color, 1)
    m.use_nodes = True
    bsdf = m.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = (*color, 1)
    bsdf.inputs["Roughness"].default_value = roughness
    bsdf.inputs["Metallic"].default_value = metallic
    return m

def uv(name, loc, scale, material, segments=12, rings=8):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segments, ring_count=rings, location=loc)
    o = bpy.context.object
    o.name = name
    o.scale = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    o.data.materials.append(material)
    return o

def box(name, loc, scale, material, bevel=0.04):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    o = bpy.context.object
    o.name = name
    o.dimensions = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    o.data.materials.append(material)
    if bevel:
        mod = o.modifiers.new("Soft equipment edges", "BEVEL")
        mod.width = bevel
        mod.segments = 1
        o.modifiers.new("Weighted normals", "WEIGHTED_NORMAL")
    return o

def cylinder(name, loc, radius, depth, material, vertices=10):
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=depth, location=loc)
    o = bpy.context.object
    o.name = name
    o.data.materials.append(material)
    return o

def build_soldier(idx):
    bpy.ops.object.select_all(action="SELECT"); bpy.ops.object.delete(use_global=False)
    palette = [
      ((0.18,0.22,0.13),(0.30,0.34,0.21)), ((0.24,0.27,0.20),(0.37,0.39,0.29)),
      ((0.12,0.17,0.14),(0.22,0.27,0.21)), ((0.31,0.28,0.20),(0.43,0.38,0.27)),
      ((0.17,0.20,0.24),(0.28,0.31,0.34))
    ]
    uniform_col, gear_col = palette[idx % len(palette)]
    uniform=mat("Uniform fabric",uniform_col); gear=mat("Tactical webbing",gear_col)
    boots=mat("Boot rubber",(0.055,0.052,0.043)); skin=mat("Skin",(0.48,0.32,0.22))
    helmet=mat("Helmet shell",(0.12,0.16,0.12),0.6); metal=mat("Weapon metal",(0.07,0.08,0.075),0.4,0.35)
    # Feet, legs, torso, arms, head and helmet; approximate height 1.8 m.
    for x in (-0.13,0.13):
        box("Boot",(x,0.04,0.10),(0.19,0.34,0.17),boots)
        box("Lower leg",(x,0.02,0.38),(0.17,0.19,0.45),uniform)
        box("Knee pad",(x,-0.09,0.52),(0.18,0.07,0.13),gear)
        box("Thigh",(x,0.015,0.72),(0.23,0.22,0.38),uniform)
    box("Torso",(0,0,1.15),(0.53,0.28,0.56),uniform,0.07)
    box("Plate carrier",(0,-0.16,1.19),(0.43,0.10,0.40),gear,0.025)
    for x in (-0.13,0,0.13):
        box("Magazine pouch",(x,-0.225,1.10),(0.085,0.055,0.13),helmet,0.01)
    box("Backpack",(0,0.19,1.25),(0.32,0.20,0.36),gear,0.035)
    for side in (-1,1):
        x=side*0.36
        uv("Shoulder pad",(x,0,1.36),(0.14,0.16,0.15),gear)
        box("Upper arm",(side*0.37,0,1.19),(0.17,0.19,0.31),uniform)
        box("Forearm",(side*0.39,-0.01,0.96),(0.14,0.16,0.24),uniform)
        uv("Glove",(side*0.39,-0.025,0.82),(0.075,0.07,0.09),boots)
    cylinder("Neck",(0,0,1.48),0.085,0.12,skin)
    uv("Head",(0,-0.005,1.60),(0.13,0.12,0.17),skin)
    uv("Helmet",(0,0,1.72),(0.15,0.14,0.105),helmet)
    box("Helmet brim",(0,-0.07,1.69),(0.27,0.17,0.035),helmet,0.01)
    # A compact slung-rifle silhouette, kept separate for later replacement.
    box("Rifle stock",(0.31,-0.12,0.91),(0.10,0.08,0.20),boots,0.01)
    box("Rifle body",(0.31,-0.17,1.02),(0.09,0.08,0.30),metal,0.01)
    box("Rifle barrel",(0.31,-0.19,1.22),(0.045,0.045,0.24),metal,0.005)
    box("Rifle magazine",(0.31,-0.22,0.97),(0.055,0.055,0.14),metal,0.005)
    # Join by material is intentionally avoided: separate parts remain easy to edit.
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.export_scene.gltf(filepath=os.path.join(OUT,f"infantry_{idx+1:02d}.glb"),
                              export_format="GLB", use_selection=False,
                              export_apply=True, export_yup=True)

for i in range(10):
    build_soldier(i)
print("Exported 10 infantry prototype GLBs to", OUT)
