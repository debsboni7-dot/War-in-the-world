# WAR IN THE WORLD

Prototype 3D de battle royale / guerre, pensé pour Android et navigateur desktop.

## Jouer

Le jeu démarre dans `index.html`. Pour publier : **Settings → Pages → Deploy from a branch → `main` → `/(root)` → Save**. Attendre la publication, puis ouvrir l'URL GitHub Pages du dépôt.

## Fonctionnalités du prototype

- Insertion aérienne, descente/parachute et atterrissage.
- Terrain de bataille procédural, routes, cratères, bâtiments, arbres, fumée et brouillard sombre.
- 50 armes originales dans le catalogue, butin au sol, munitions, rechargement, visée et changement d'arme.
- 11 bots, santé, éliminations, mini-carte et zone de survie rétrécissante.
- Commandes tactiles, clavier/souris et réglages graphiques.
- Textures de terrain générées localement par Canvas pour éviter de télécharger de grandes images.

## Modèles 3D externes

- Soldat animé : modèle d'exemple Three.js `Soldier.glb` (`https://threejs.org/examples/models/gltf/Soldier.glb`).
- Hélicoptère : modèle GLB Light Helicopter d'Innerscene, dédié CC0 (`https://www.innerscene.com/tools/library/3d-parts/light-helicopter-eab26245`).
- Si un modèle distant ne charge pas, le prototype utilise un modèle de secours construit dans le code.

Ces modèles sont chargés depuis Internet au lancement : une connexion est nécessaire. Ce dépôt ne contient pas encore les fichiers binaires GLB en local.

## Limites connues

Ceci est une première version jouable, pas un jeu AAA : les 50 armes ont des statistiques et des noms distincts, mais leurs modèles visuels ne sont pas encore 50 modèles d'armes uniques. Les bots, tirs, impacts et animations sont des systèmes de prototype. Le jeu ne possède pas encore de multijoueur en ligne, de parachute animé détaillé, ni de système de progression persistant.
