// WITW Arsenal — Frontline Contrast
// GLSL ES 3.00 fragment shader. Use with a fullscreen pass in a WebGL2 renderer.
#version 300 es
precision highp float;
uniform sampler2D tDiffuse;
uniform float uContrast; // recommended 1.12
uniform float uSaturation; // recommended 0.92
uniform float uExposure; // recommended 1.0
in vec2 vUv;
out vec4 outColor;
void main() {
  vec4 src = texture(tDiffuse, vUv);
  vec3 c = max(src.rgb * uExposure, vec3(0.0));
  c = (c - 0.5) * uContrast + 0.5;
  float l = dot(c, vec3(0.2126, 0.7152, 0.0722));
  c = mix(vec3(l), c, uSaturation);
  c = clamp(c, 0.0, 1.0);
  outColor = vec4(c, src.a);
}
