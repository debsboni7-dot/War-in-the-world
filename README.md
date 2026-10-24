# WAR IN THE WORLD

Prototype 3D de battle royale / guerre, pensé pour Android et navigateur desktop.

## Jouer

Le jeu démarre dans `index.html`. Pour publier : **Settings → Pages → Deploy from a branch → `main` → `/(root)` → Save**. Attendre la publication, puis ouvrir l'URL GitHub Pages du dépôt.

## Fonctionnalités du prototype

- Insertion aérienne, descente/parachute et atterrissage.
- Terrain de guerre ravagé : boue, gravier, pierres cassées, cratères, murs détruits, gravats externes CC0, fumée et brouillard; aucune texture d'herbe ni végétation n'est utilisée dans le décor.
- 50 armes originales dans le catalogue, butin au sol, munitions, rechargement, visée et changement d'arme.
- 11 bots, santé, éliminations, mini-carte et zone de survie rétrécissante.
- Commandes tactiles, clavier/souris et réglages graphiques.
- Textures procédurales locales pour la boue, le gravier, le béton, le métal et les roches; les modèles de gravats externes se chargent séparément.

## Modèles 3D externes

- Armes 3D externes : packs de fusils, pistolets, SMG, fusil à pompe et sniper du dépôt [petroulacl/fps-asset-kit](https://github.com/petroulacl/fps-asset-kit), annoncé CC0/public domain. Le jeu garde ses modèles procéduraux en secours si le téléchargement échoue.
- Décors de guerre : modèles `SM_Rubble_Pile.glb`, `SM_Debris_Scatter.glb` et `SM_Wall_Damaged_4m.glb` du dépôt [JaronKBragg7337/asset-pack-ue-threejs-blender-unity](https://github.com/JaronKBragg7337/asset-pack-ue-threejs-blender-unity), annoncés CC0. Des morceaux de murs, des pierres et des poutres sont aussi générés directement par le jeu.
- Soldats ennemis faits à la main dans Three.js : dix variantes géométriques distinctes avec différences de casque, silhouette, sac, plaques, masque, antenne, pochettes et équipement. Elles sont générées directement dans le code, sans télécharger de personnage lourd. Le soldat externe animé reste réservé au joueur. Ce ne sont pas dix fichiers GLB exportés depuis Blender, mais dix modèles procéduraux construits dans le jeu.
- Soldat animé de secours : modèle d'exemple Three.js `Soldier.glb` (`https://threejs.org/examples/models/gltf/Soldier.glb`).
- Hélicoptère : modèle GLB Light Helicopter d'Innerscene, dédié CC0 (`https://www.innerscene.com/tools/library/3d-parts/light-helicopter-eab26245`).
- Si un modèle distant ne charge pas, le prototype conserve un modèle de secours construit dans le code.

Ces modèles sont chargés depuis Internet au lancement : une connexion est nécessaire. Ce dépôt ne contient pas encore les fichiers binaires GLB en local.

## Limites connues

Ceci est une première version jouable, pas un jeu AAA : les 50 armes ont des statistiques et des noms distincts, mais leurs modèles visuels ne sont pas encore 50 modèles d'armes uniques. Les bots, tirs, impacts et animations sont des systèmes de prototype. Le jeu ne possède pas encore de multijoueur en ligne, de parachute animé détaillé, ni de système de progression persistant.

## Boutique officielle (prototype)

- Page catalogue : `market.html` — publiée sur GitHub Pages à l'adresse `/market.html`.
- Le menu **Paramètres** du jeu contient un lien vers la boutique.
- Catégories prévues : armes, soldats, vêtements, équipements, shaders officiels, animations, sons, véhicules et propositions de créateurs.
- Les fiches de démonstration affichent une image conceptuelle, une description, un prix indicatif en FCFA, une taille de fichier indicative, un format prévu, la compatibilité, l'effet envisagé en jeu et la licence prévue.
- La recherche, les filtres de catégories, le tri, les fiches détaillées et les paramètres sont interactifs.

### Limites de sécurité et de paiement

**La boutique est une maquette, pas encore une boutique transactionnelle.** Les prix et tailles affichés sont des exemples; aucun paquet réel n'est proposé au téléchargement. Les boutons d'achat et de téléchargement restent désactivés. Aucun paiement n'est encaissé.

Avant une mise en production, il faut un backend et une base de données, une authentification, un prestataire compatible Mobile Money et cartes en Côte d'Ivoire, des webhooks de paiement vérifiés côté serveur, un processus de remboursement et de support, un système de signatures cryptographiques et des liens de téléchargement temporaires à usage unique. Les secrets ne doivent jamais être intégrés au JavaScript public.

Une vérification de signature uniquement dans le navigateur peut être contournée. Les shaders doivent être des packs officiels validés ou des préréglages contrôlés; ne jamais exécuter du code de shader arbitraire envoyé par un joueur. Les fichiers doivent être analysés, limités en taille et en formats, et les contenus de créateurs doivent être examinés avant publication.

La licence « un téléchargement » est stricte : elle peut bloquer l'accès si le téléchargement échoue ou si le joueur change d'appareil. Il faut prévoir un avertissement avant confirmation et une procédure de récupération manuelle après vérification, sans prétendre empêcher à 100 % la copie des fichiers.


## Crédits des ressources 3D externes

- Soldat riggé chargé depuis le dépôt public [cktang88/3d-fps](https://github.com/cktang88/3d-fps), modèle source « FREE [Military Soldier] RIGGED » par BAMEN, licence CC BY 4.0. Source du modèle : https://sketchfab.com/3d-models/free-military-soldier-rigged-e9c56308a67d4a3db62e914fafa4d198. Les conditions de la licence demandent de conserver l’attribution.
- Animations de référence indiquées par le projet source : Quaternius Universal Animation Library, CC0.

Les armes et les décors externes sont chargés à distance depuis GitHub. Les fichiers binaires ne sont pas tous stockés dans ce dépôt; une connexion Internet est nécessaire pour les charger. Si une source devient indisponible, les armes procédurales et les ruines générées localement restent disponibles.
