// WITW Arsenal — Smoke & Atmosphere
// GLSL ES 3.00 fragment shader for a procedural fullscreen haze layer.
#version 300 es
precision highp float;
uniform sampler2D tDiffuse;
uniform float uTime;
uniform float uDensity; // recommended 0.18
uniform vec3 uFogColor; // recommended vec3(0.40, 0.43, 0.40)
in vec2 vUv;
out vec4 outColor;
float hash(vec2 p) { return fract(sin(dot(p, vec2(127.1, 311.7))) * 43758.5453); }
float noise(vec2 p) {
  vec2 i=floor(p), f=fract(p);
  f=f*f*(3.0-2.0*f);
  return mix(mix(hash(i),hash(i+vec2(1,0)),f.x),
             mix(hash(i+vec2(0,1)),hash(i+vec2(1,1)),f.x),f.y);
}
void main() {
  vec4 src=texture(tDiffuse,vUv);
  float n=noise(vUv*vec2(7.0,3.0)+vec2(uTime*0.025,uTime*0.008));
  float band=smoothstep(0.18,0.92,n)*uDensity;
  float horizon=1.0-smoothstep(0.15,0.9,abs(vUv.y-0.48));
  float a=clamp(band*horizon,0.0,0.42);
  outColor=vec4(mix(src.rgb,uFogColor,a),src.a);
}
