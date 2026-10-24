# Unreal Engine 5 — Vertical Slice de War in the World

## Objectif
Construire d'abord une petite mission militaire jouable et mesurable sur Android, avant d'étendre la carte. Ce document décrit la première tranche de jeu à réaliser dans Unreal Engine 5 ; ce n'est pas une déclaration qu'un projet compilé existe déjà.

## Plateforme et cible
- Moteur : Unreal Engine 5, projet natif distinct de la version HTML/Three.js.
- Cible principale : Android, y compris Samsung Galaxy A06 (appareil d'entrée de gamme).
- Contrôle : joystick tactile gauche pour le déplacement, zone tactile droite pour regarder, boutons contextuels Tirer / Recharger / Viser / Sauter / Interagir.
- Objectif performance initial : viser 30 FPS stables avec réglages mobiles bas ; mesurer sur appareil réel avant d'augmenter la qualité.
- Mémoire et chargement : niveaux compacts, textures avec mipmaps, LOD, collision simplifiée et chargement progressif si la taille du monde le nécessite.

## Première mission : « Point de contrôle »
### Boucle jouable
1. Le joueur apparaît derrière une couverture sûre.
2. Un objectif HUD indique d'atteindre le poste de contrôle.
3. Le joueur se déplace, regarde autour de lui et peut sprinter.
4. Un ennemi repérable patrouille dans une zone courte ; il détecte le joueur selon la distance et la ligne de vue.
5. Le joueur peut viser, tirer, recharger et se mettre à couvert.
6. L'ennemi réagit aux impacts et peut être neutralisé.
7. Le joueur active un point d'objectif et reçoit une confirmation de mission terminée.
8. Un bouton permet de recommencer la mission.

### Contenu minimal de la scène
- Terrain militaire compact avec relief léger et sol PBR.
- Un personnage joueur équipé d'un fusil.
- Un ennemi avec comportement simple : patrouille, détection, poursuite, attaque, retour à la patrouille.
- Trois couvertures : sacs de sable, barrière béton, caisse militaire.
- Un poste de contrôle avec barrière, grillage et éclairage.
- Deux éléments de décor éloignés pour donner de la profondeur, sans densité excessive.
- HUD mobile lisible et pause avec commandes, sensibilité et qualité graphique.

## Architecture UE5 proposée
- `BP_PlayerCharacter` ou classe C++ équivalente : déplacement, caméra, santé, équipement et interaction.
- `BP_WeaponBase` : données de l'arme, cadence, chargeur, munitions, rechargement et dégâts.
- `BP_EnemySoldier` : santé et réactions aux dégâts.
- `BP_EnemyAIController` + Behavior Tree simple : patrouille et combat.
- `BP_MissionObjective` : déclencheur de fin de mission.
- `WBP_MobileHUD` : commandes tactiles et objectifs.
- `WBP_PauseMenu` : reprise, sensibilité, audio et qualité.
- Data Assets / Data Tables pour les statistiques des armes et les réglages, plutôt que des valeurs copiées dans plusieurs Blueprints.

## Ordre d'implémentation
1. Créer le projet UE5 avec le modèle Third Person et activer la cible Android.
2. Configurer le package Android et vérifier qu'une scène vide peut être compilée et installée.
3. Faire marcher le joueur et la caméra tactile sans arme.
4. Ajouter collisions et couvertures, puis vérifier qu'on ne traverse aucun obstacle.
5. Ajouter une seule arme avec tir, rechargement, recul léger, son et impact.
6. Ajouter un ennemi avec santé et IA basique.
7. Ajouter objectif, HUD, pause et recommencement.
8. Compiler, installer et mesurer sur l'appareil cible.
9. Seulement après validation, remplacer les placeholders par les modèles et matériaux finaux.

## Critères d'acceptation avant d'agrandir le jeu
- Aucun crash lors du lancement, de la pause, de la reprise ou du recommencement.
- Les commandes tactiles ne bloquent pas la caméra et ne tirent pas involontairement.
- Le joueur et les ennemis ne traversent pas le sol ni les couvertures.
- Tir, dégâts, munitions et rechargement restent synchronisés.
- L'objectif ne se termine qu'une fois les conditions remplies.
- La lisibilité reste bonne sur petit écran.
- Mesure FPS et mémoire consignée sur le Samsung Galaxy A06 ; ne pas annoncer 30 FPS sans mesure réelle.
- Aucun asset manquant, matériau rose/noir, texture cassée ou référence d'objet invalide.

## Profil graphique mobile initial
- Commencer sans Nanite ni Lumen sur la scène de test ; n'activer une fonction que si la version du moteur et le matériel ciblé la supportent avec de bonnes performances.
- Éclairage statique/baké autant que possible pour les environnements fixes.
- Limiter les lumières dynamiques et les ombres en temps réel.
- Utiliser LODs, instancing pour végétation et accessoires répétés, et collisions simplifiées.
- Textures PBR : tailles adaptées à la distance et à l'importance visuelle ; éviter le 4K systématique sur mobile.
- Effets de tir courts et peu coûteux ; limiter transparences, particules et post-traitement.
- Proposer les niveaux Bas / Moyen, avec Bas sélectionné par défaut sur appareil d'entrée de gamme.

## Limites actuelles
Le dépôt contient une version Web Three.js. Les fichiers Unreal `.uasset` et `.umap` ne sont pas utilisables directement par GitHub Pages. Il faut Unreal Engine installé pour créer/importer les ressources natives, ouvrir la scène, compiler et empaqueter l'APK. Aucun test Unreal ou Android n'est déclaré effectué par ce document.
