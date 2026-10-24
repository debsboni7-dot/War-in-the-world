import bpy, math, os, random
OUT=os.path.abspath("public/assets/models/environment")
os.makedirs(OUT,exist_ok=True)
random.seed(24)
def mat(n,c,metal=0,rough=.85):
 m=bpy.data.materials.new(n); m.diffuse_color=(*c,1); m.use_nodes=True
 p=m.node_tree.nodes.get("Principled BSDF"); p.inputs["Base Color"].default_value=(*c,1); p.inputs["Metallic"].default_value=metal; p.inputs["Roughness"].default_value=rough
 return m
CONC=mat("Weathered concrete",(0.28,.29,.27)); RUST=mat("Oxidized steel",(.16,.12,.08),.5); WOOD=mat("Rough timber",(.20,.14,.08)); SAND=mat("Dry soil",(.39,.31,.20)); LEAF=mat("Dusty olive foliage",(.15,.22,.10)); ROCK=mat("Stone",(.25,.25,.22))
def cube(n,loc,dim,ma,bev=.02):
 bpy.ops.mesh.primitive_cube_add(size=1,location=loc); o=bpy.context.object; o.name=n; o.dimensions=dim
 bpy.ops.object.transform_apply(location=False,rotation=False,scale=True); o.data.materials.append(ma)
 if bev:
  b=o.modifiers.new("Chipped edges","BEVEL"); b.width=bev; b.segments=1
  o.modifiers.new("Weighted normals","WEIGHTED_NORMAL")
 return o
def cyl(n,loc,r,depth,ma,verts=10,rot=None):
 bpy.ops.mesh.primitive_cylinder_add(vertices=verts,radius=r,depth=depth,location=loc,rotation=rot or (0,0,0))
 o=bpy.context.object; o.name=n; o.data.materials.append(ma); return o
def reset(): bpy.ops.object.select_all(action="SELECT"); bpy.ops.object.delete(use_global=False)
def export(n):
 bpy.ops.object.select_all(action="SELECT"); bpy.ops.export_scene.gltf(filepath=os.path.join(OUT,n+".glb"),export_format="GLB",use_selection=False,export_apply=True,export_yup=True)
def barrier(i):
 reset(); ma=CONC if i%2==0 else RUST
 cube("Concrete road barrier",(0,0,.35),(1.65,.48,.7),ma,.045)
 cube("Reflective panel",(0,-.246,.45),(.42,.025,.20),SAND,.005)
 export("road_barrier_%02d"%(i+1))
def drum(i):
 reset(); ma=RUST if i%2==0 else CONC
 cyl("Industrial drum",(0,0,.35),.25,.70,ma,16)
 for z in (.15,.35,.55): cyl("Raised drum rib",(0,0,z),.258,.035,STEEL if 'STEEL' in globals() else RUST,16)
 export("industrial_drum_%02d"%(i+1))
def tree(i):
 reset(); trunk=mat("Tree bark",(.19,.13,.07))
 cyl("Trunk",(0,0,.75),.14,1.5,trunk,8)
 for j in range(3):
  bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1,radius=1,location=(random.uniform(-.18,.18),random.uniform(-.12,.12),1.45+j*.32))
  o=bpy.context.object; o.name="Low poly canopy"; o.scale=(.55-j*.05,.50-j*.04,.55); bpy.ops.object.transform_apply(location=False,rotation=False,scale=True); o.data.materials.append(LEAF)
 export("dryland_tree_%02d"%(i+1))
def rock(i):
 reset()
 bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1,radius=1,location=(0,0,.25))
 o=bpy.context.object; o.name="Rock"; o.scale=(random.uniform(.3,.65),random.uniform(.25,.5),random.uniform(.18,.38)); bpy.ops.object.transform_apply(location=False,rotation=False,scale=True); o.data.materials.append(ROCK)
 export("rock_cluster_%02d"%(i+1))
def post(i):
 reset(); cyl("Steel post",(0,0,.6),.055,1.2,RUST,8)
 cube("Warning sign",(0,-.015,1.05),(.45,.06,.28),CONC,.01)
 export("warning_post_%02d"%(i+1))
for i in range(5): barrier(i)
for i in range(3): drum(i)
for i in range(5): tree(i)
for i in range(5): rock(i)
for i in range(2): post(i)
print("Generated 20 environment prototype GLBs.")
