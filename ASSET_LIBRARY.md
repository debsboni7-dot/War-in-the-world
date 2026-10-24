# War in the World — 3D asset batches

## Batch 01: infantry prototypes
`tools/generate_soldier_batch.py` creates 10 editable low-poly soldier prototypes and exports them as GLB to `public/assets/models/soldiers/`.

### Important
- These are **blockout/prototype assets**, not photorealistic final models.
- They use primitive geometry and simple materials so the first batch can be generated reliably.
- The models are not rigged or animated yet. Before using them as playable characters, add a humanoid armature, UV unwrap, PBR textures, and performance checks.
- Intended height is approximately 1.8 m. Rifle is a separate visual silhouette but currently exported in the same GLB.
- Blender is required to execute the generator: `blender -b --python tools/generate_soldier_batch.py`.

## Planned library of 1,000 assets
1. 100 infantry and equipment variants
2. 100 weapons and accessories
3. 100 vehicles
4. 200 combat environment props
5. 200 terrain and vegetation assets
6. 150 bases and resource props
7. 150 secondary props

The count is a target for staged batches, not a claim that 1,000 finished models already exist.
