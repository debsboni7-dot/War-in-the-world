import bpy, math, os
OUT=os.path.abspath("public/assets/models/vehicles")
os.makedirs(OUT,exist_ok=True)

def mat(n,c,metal=0.0,rough=0.8):
 m=bpy.data.materials.new(n); m.diffuse_color=(*c,1); m.use_nodes=True
 p=m.node_tree.nodes.get("Principled BSDF"); p.inputs["Base Color"].default_value=(*c,1); p.inputs["Metallic"].default_value=metal; p.inputs["Roughness"].default_value=rough
 return m
OLIVE=mat("Olive military paint",(0.18,0.22,0.14),0.18,0.78)
DARK=mat("Rubber",(0.025,0.028,0.026),0,0.92)
STEEL=mat("Dark metal",(0.07,0.08,0.075),0.6,0.45)
GLASS=mat("Smoky armored glass",(0.045,0.09,0.095),0.25,0.3)
SAND=mat("Desert paint",(0.43,0.36,0.23),0.12,0.8)
def cube(n,loc,dim,ma,bev=0.035):
 bpy.ops.mesh.primitive_cube_add(size=1,location=loc); o=bpy.context.object; o.name=n; o.dimensions=dim
 bpy.ops.object.transform_apply(location=False,rotation=False,scale=True); o.data.materials.append(ma)
 if bev:
  b=o.modifiers.new("Beveled edges","BEVEL"); b.width=bev; b.segments=1
  o.modifiers.new("Weighted normals","WEIGHTED_NORMAL")
 return o
def cyl(n,loc,r,depth,ma,vertices=12,rot=(math.pi/2,0,0)):
 bpy.ops.mesh.primitive_cylinder_add(vertices=vertices,radius=r,depth=depth,location=loc,rotation=rot)
 o=bpy.context.object; o.name=n; o.data.materials.append(ma); return o
def reset():
 bpy.ops.object.select_all(action="SELECT"); bpy.ops.object.delete(use_global=False)
def wheels(length,width,count,rad=0.28):
 for side in (-1,1):
  for j in range(count):
   x=-length/2+0.35+j*(length-0.7)/max(1,count-1)
   cyl("All terrain tire",(x,side*(width/2+0.02),rad),rad,0.16,DARK,12)
   cyl("Wheel hub",(x,side*(width/2+0.11),rad),rad*0.48,0.025,STEEL,10)
def export(name):
 bpy.ops.object.select_all(action="SELECT")
 bpy.ops.export_scene.gltf(filepath=os.path.join(OUT,name+".glb"),export_format="GLB",use_selection=False,export_apply=True,export_yup=True)
def light_vehicle(i):
 reset(); paint=SAND if i%3==0 else OLIVE
 # 4x4 field vehicle
 cube("Chassis",(0,0,0.55),(2.7,1.25,0.28),STEEL)
 cube("Armored body",(0,0,0.92),(2.55,1.38,0.72),paint,0.07)
 cube("Engine hood",(-0.72,0,1.28),(0.88,1.28,0.28),paint,0.04)
 cube("Cabin",(0.42,0,1.42),(1.15,1.24,0.64),paint,0.05)
 for x in (0.12,0.68):
  for side in (-1,1):
   cube("Armored window",(x,side*0.631,1.52),(0.42,0.025,0.28),GLASS,0.008)
 cube("Front windshield",(-0.12,0,1.52),(0.025,1.02,0.28),GLASS,0.008)
 for side in (-1,1):
  cube("Headlight",(-1.21,side*0.46,1.18),(0.07,0.16,0.12),GLASS,0.01)
 wheels(2.45,1.38,4,0.29)
 if i%2==0:
  cube("Roof rack",(0.35,0,1.82),(0.72,0.72,0.06),STEEL)
 else:
  cyl("Roof mount",(0.3,0,1.82),0.20,0.10,STEEL,12,(0,0,0))
 export("field_vehicle_%02d"%(i+1))
def apc(i):
 reset(); paint=SAND if i%2 else OLIVE
 cube("Tracked hull",(0,0,0.75),(3.8,1.65,0.95),paint,0.08)
 cube("Upper sloped armor",(0.05,0,1.32),(3.25,1.52,0.55),paint,0.06)
 cube("Front glacis",(-1.68,0,1.22),(0.32,1.48,0.55),paint,0.035)
 # track runs and simplified road wheels
 for side in (-1,1):
  cube("Track belt",(0,side*0.88,0.43),(3.6,0.20,0.58),DARK,0.08)
  for x in (-1.3,-0.65,0,0.65,1.3):
   cyl("Road wheel",(x,side*1.0,0.43),0.22,0.06,STEEL,12)
  for x in (-0.8,0.2,0.95):
   cube("Side armor panel",(x,side*0.84,1.0),(0.52,0.08,0.28),STEEL,0.015)
 for x in (-0.8,-0.15,0.5):
  cube("Periscope",(x,-0.22,1.63),(0.12,0.09,0.10),STEEL,0.01)
 cyl("Low profile turret",(0.35,0,1.72),0.42,0.24,paint,12,(0,0,0))
 cube("Turret barrel",(0.77,0,1.77),(0.75,0.10,0.10),STEEL,0.01)
 export("armored_carrier_%02d"%(i+1))
def cargo_truck(i):
 reset(); paint=SAND if i%2 else OLIVE
 cube("Truck chassis",(0,0,0.52),(3.7,1.1,0.22),STEEL)
 cube("Cab",(1.25,0,1.05),(0.95,1.18,0.95),paint,0.06)
 cube("Windshield",(1.25,-0.01,1.30),(0.025,0.93,0.32),GLASS,0.01)
 for side in (-1,1): cube("Side window",(1.50,side*0.60,1.30),(0.34,0.025,0.28),GLASS,0.01)
 cube("Cargo bed",(-0.65,0,0.95),(2.2,1.18,0.16),STEEL)
 for side in (-1,1): cube("Cargo side rail",(-0.65,side*0.58,1.22),(2.2,0.08,0.48),paint,0.015)
 for x in (-1.55,0.1,1.35):
  for side in (-1,1):
   cyl("Truck tire",(x,side*0.63,0.34),0.27,0.15,DARK,12)
   cyl("Hub",(x,side*0.72,0.34),0.12,0.025,STEEL,10)
 export("cargo_truck_%02d"%(i+1))
for i in range(4): light_vehicle(i)
for i in range(3): apc(i)
for i in range(3): cargo_truck(i)
print("Generated 10 vehicle prototype GLBs.")
