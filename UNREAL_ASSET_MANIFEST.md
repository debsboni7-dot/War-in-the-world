# War in the World — ordre de production des assets Unreal

Priorité des 25 premiers assets de la tranche verticale. Ce manifeste est un plan de production : il ne signifie pas que ces fichiers sont déjà créés.

## Priorité P0 — nécessaires à la mission test
1. Soldier_Player — soldat jouable, silhouette militaire crédible, équipement modulaire, proportions humaines réalistes.
2. Soldier_Enemy — soldat ennemi distinct visuellement, même squelette compatible si possible.
3. Rifle_Assault — fusil d'assaut avec crosse, canon, chargeur, viseur et poignée clairement définis.
4. Terrain_Test — terrain de test avec pente légère, chemins et sol militaire.
5. Sandbag_Barricade — barricade de sacs de sable empilés, collision simple.
6. Concrete_Barrier — barrière béton avec bords usés et marques discrètes.
7. Military_Crate — caisse de ravitaillement avec matériaux PBR.
8. Checkpoint_Gate — barrière de contrôle et supports.
9. Fence_Modular — segment de grillage modulaire avec poteaux.
10. Objective_Marker — marqueur de mission lisible, non intrusif.
11. Muzzle_Flash — effet de bouche bref et léger.
12. Bullet_Impact_Dirt — impact de balle dans le sol, effet bref.
13. Bullet_Impact_Concrete — impact poussière/éclat sur béton.
14. Rifle_Shot_SFX — son de tir adapté au mix mobile.
15. Reload_SFX — son de rechargement.

## Priorité P1 — amélioration de la scène
16. Military_Backpack — sac à dos avec sangles et poches, mesh optimisé.
17. Helmet_Modular — casque militaire, variantes de couleur.
18. Tactical_Vest — gilet porte-équipement, poches lisibles sans microgéométrie excessive.
19. Ammo_Box — caisse de munitions.
20. Portable_Lamp — lampe de poste de contrôle.
21. Sandbag_Single — sac individuel réutilisable en instancing.
22. Metal_Barrel — baril métallique usé.
23. Road_Block — obstacle routier modulaire.
24. Dry_Grass_Cluster — touffe d'herbe adaptée au LOD/instancing.
25. Small_Rock_Cluster — groupe de pierres pour casser la répétition du terrain.

## Exigences communes
- Échelle physique cohérente en centimètres Unreal.
- Pivot placé pour faciliter le placement et l'animation.
- Matériaux PBR propres ; pas de texture blanche/grise de secours dans la livraison finale.
- Nommage stable, par exemple `SM_Checkpoint_Gate`, `SK_Soldier_Player`, `M_Rifle_Body`, `T_Sandbag_BaseColor`.
- LODs pour meshes visibles à distance ; collision simplifiée et adaptée au gameplay.
- Pour les personnages : rig compatible, poids de skinning propres et animations testées dans Unreal.
- Pour les armes : point d'attache de main, point de sortie du canon et chargeur correctement positionnés.
- Garder les versions source et les textures sous contrôle de taille ; ne pas imposer 4K à chaque texture sur Android.
- Vérifier chaque asset dans une scène Unreal de test avant de le déclarer validé.

## Critères de qualité
Un asset n'est « validé » qu'après import dans Unreal, vérification d'échelle, matériau, collision, LOD et comportement en jeu. Une image de référence, un prompt ou un script ne compte pas comme asset livré.
