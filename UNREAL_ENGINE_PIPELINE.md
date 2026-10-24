# Unreal Engine direction — War in the World

## Decision
New game-development work targets **Unreal Engine 5**. The existing HTML/Three.js build on GitHub Pages is the current web version; it is not an Unreal build and cannot load Unreal `.uasset` files.

## Important project boundary
Unreal Engine projects require the Unreal Editor/Engine toolchain to author, import, package, and test native assets. The current remote GitHub automation only had Blender installed, so it must not be described as an Unreal asset generator. No Unreal models or packaged game are considered complete until an Unreal-compatible build environment has generated and verified them.

## Target
- Genre: third-person military action/shooter.
- Target device: Android, including entry-level devices such as Samsung Galaxy A06.
- Visual direction: realistic military materials and proportions, readable silhouettes, restrained post-processing, believable terrain and lighting.
- Performance target: mobile-first; use LODs, instancing, collision proxies, texture streaming, baked/static lighting where appropriate, and scalable effects.
- Asset families: infantry/equipment, weapons, tactical vehicles, military structures, checkpoints, terrain, vegetation, debris, props, VFX and audio.

## Production order
1. Establish a valid Unreal Engine 5 project and Android target settings.
2. Build one small vertical slice: one test terrain, one player soldier, one weapon, one enemy, one cover prop and one objective.
3. Validate controls, collision, weapon handling, enemy response, Android packaging and frame rate.
4. Only after the slice works, expand the asset library in measured batches.
5. Keep the old HTML build separate until the Unreal build is packaged and tested. GitHub Pages alone does not host a native Unreal Android game.

## Asset acceptance checklist
Every model batch must have: source/project provenance, correct scale and pivot, usable materials, collision strategy, LOD plan, naming convention, and a successful import/test in Unreal. A script or plan is not proof that the model has been generated.
