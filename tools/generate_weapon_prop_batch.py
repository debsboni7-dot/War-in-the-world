import bpy, math, os
OUT = os.path.abspath("public/assets/models/weapons")
os.makedirs(OUT, exist_ok=True)

def mat(name, color, metallic=0.0, rough=0.75):
    m=bpy.data.materials.new(name); m.diffuse_color=(*color,1); m.use_nodes=True
    p=m.node_tree.nodes.get("Principled BSDF")
    p.inputs["Base Color"].default_value=(*color,1); p.inputs["Metallic"].default_value=metallic; p.inputs["Roughness"].default_value=rough
    return m
STEEL=mat("Dark blued steel",(0.075,0.085,0.08),0.55,0.42)
POLY=mat("Black polymer",(0.025,0.03,0.028),0.0,0.68)
WOOD=mat("Dark composite",(0.16,0.13,0.09),0.0,0.8)
OLIVE=mat("Olive drab",(0.19,0.22,0.14),0.0,0.85)
SAND=mat("Dusty tan",(0.47,0.39,0.26),0.0,0.9)
def cube(n,loc,dim,ma, bevel=0.015):
    bpy.ops.mesh.primitive_cube_add(size=1,location=loc); o=bpy.context.object; o.name=n; o.dimensions=dim
    bpy.ops.object.transform_apply(location=False,rotation=False,scale=True); o.data.materials.append(ma)
    if bevel:
        b=o.modifiers.new("Small edge bevel","BEVEL"); b.width=bevel; b.segments=1
        o.modifiers.new("Weighted normals","WEIGHTED_NORMAL")
    return o
def cyl(n,loc,r,depth,ma,verts=12,rot=None):
    bpy.ops.mesh.primitive_cylinder_add(vertices=verts,radius=r,depth=depth,location=loc)
    o=bpy.context.object; o.name=n; o.data.materials.append(ma)
    if rot: o.rotation_euler=rot
    return o
def export(name):
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.export_scene.gltf(filepath=os.path.join(OUT,name+".glb"),export_format="GLB",use_selection=False,export_apply=True,export_yup=True)
def reset():
    bpy.ops.object.select_all(action="SELECT"); bpy.ops.object.delete(use_global=False)
def rifle(i):
    reset()
    stock=WOOD if i%3==0 else POLY
    cube("Stock",(-0.28,0,0),(0.42,0.10,0.12),stock)
    cube("Receiver",(0.02,0,0.01),(0.34,0.12,0.14),STEEL)
    cube("Handguard",(0.27,0,0.015),(0.34,0.09,0.095),POLY)
    cube("Barrel",(0.53,0,0.02),(0.30,0.035,0.035),STEEL,0.005)
    cube("Muzzle",(0.69,0,0.02),(0.05,0.05,0.05),STEEL,0.005)
    cube("Magazine",(0.02,-0.025,-0.13),(0.10,0.06,0.20),STEEL,0.008)
    cube("Grip",(0.00,0,-0.105),(0.07,0.08,0.13),POLY,0.008)
    cube("Sight",(0.03,0,0.105),(0.08,0.045,0.035),STEEL,0.005)
    export("rifle_variant_%02d"%(i+1))
def crate(i):
    reset(); ma=[OLIVE,SAND,WOOD][i%3]
    cube("Military supply crate",(0,0,0),(0.65,0.42,0.42),ma,0.025)
    for z in (-0.12,0.12): cube("Reinforcement strip",(0,-0.216,z),(0.60,0.025,0.035),STEEL,0.004)
    for x in (-0.22,0.22): cube("Side latch",(x,-0.225,0),(0.055,0.025,0.08),STEEL,0.004)
    export("supply_crate_%02d"%(i+1))
def barricade(i):
    reset(); ma=OLIVE if i%2==0 else SAND
    cube("Barricade beam",(0,0,0.30),(1.25,0.18,0.30),ma,0.025)
    for x in (-0.43,0.43):
        cube("Support leg",(x,0,0.06),(0.12,0.14,0.48),WOOD,0.015)
    for x in (-0.22,0.22): cube("Metal plate",(x,-0.10,0.30),(0.08,0.025,0.20),STEEL,0.006)
    export("road_barricade_%02d"%(i+1))
def sandbag(i):
    reset(); ma=SAND if i%2==0 else OLIVE
    for row in range(3):
        count=4-row
        for j in range(count):
            x=(j-(count-1)/2)*0.24 + (0.12 if row%2 else 0)
            bpy.ops.mesh.primitive_uv_sphere_add(segments=10, ring_count=6, radius=1, location=(x,0.0,0.12+row*0.13))
            o=bpy.context.object; o.name="Sandbag"; o.scale=(0.15,0.10,0.09); bpy.ops.object.transform_apply(location=False,rotation=False,scale=True); o.data.materials.append(ma)
    export("sandbag_wall_%02d"%(i+1))
for i in range(10): rifle(i)
for i in range(5): crate(i)
for i in range(5): barricade(i)
for i in range(5): sandbag(i)
print("Generated 25 weapon and combat-prop GLB prototypes.")
