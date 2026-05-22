# Estimation de l'âge osseux par Deep Learning

Projet académique de Deep Learning basé sur le défi RSNA Bone Age. Le but est d'estimer l'âge osseux, exprimé en mois, à partir de radiographies de la main gauche d'enfants. Le projet couvre tout le pipeline, depuis l'exploration des données jusqu'à l'interprétation des prédictions et la préparation d'une démo de présentation.

## Vue d'ensemble

Le travail compare plusieurs approches de régression d'images médicales :

- une baseline CNN construite from scratch ;
- une version régularisée avec Batch Normalization, Dropout, Early Stopping et L2 ;
- une approche en transfer learning avec un backbone EfficientNetB0 ;
- un notebook final de synthèse qui centralise le meilleur pipeline.

L'objectif n'est pas de faire de la classification, mais bien de prédire une valeur continue en mois.

## Résultats principaux

Les sorties exécutées dans les notebooks montrent une progression nette entre la baseline et le transfer learning.

### Données traitées

- Images détectées lors de l'exploration initiale : 12 811.
- Répartition utilisée dans le pipeline final : 10 088 images d'entraînement et 2 523 images de validation.
- Taille du batch testée dans les notebooks Kaggle : 16.

### Comparaison des modèles

| Modèle | MAE validation | MSE validation | R² validation | Statut |
| --- | ---: | ---: | ---: | --- |
| CNN baseline | 33.95 mois | 1 781.33 | non mesuré explicitement | Référence initiale |
| CNN régularisé | 33.39 mois | 1 742.77 | 0.0161 | Amélioration limitée |
| Transfer learning EfficientNetB0 | 14.37 mois | 333.74 | 0.8116 | Meilleur modèle |

Le meilleur modèle du projet est donc le pipeline de transfer learning, très supérieur aux modèles entraînés from scratch.

### Export final

- Modèle sauvegardé : models/bone_age_model.keras
- Backbone utilisé : EfficientNetB0
- Statut d'export : succès

## Organisation du dépôt

```text
drafts/                Notebooks de travail et expérimentations
  01_eda_preprocessing.ipynb
  02_baseline_cnn.ipynb
  03_regularization_tuning.ipynb
  04_transfer_learning.ipynb
  kaggle_trial_1.ipynb
  kaggle_trial_2.ipynb
notebooks/             Notebook final de synthèse
  final_pipeline_bone_age.ipynb
streamlit_app/         Prototype d'application de démonstration
  app.py
  requirements.txt
presentation/          Support de soutenance
  README.md
Readme.md              Vue globale du projet
notebook_outputs.md    Résumé des sorties extraites des notebooks
```

## Données et prétraitement

Le dataset RSNA Bone Age est volumineux, donc le projet s'appuie sur des générateurs ou des pipelines de type `tf.data` pour éviter de tout charger en mémoire.

Les étapes de préparation retenues sont les suivantes :

- téléchargement du dataset depuis Kaggle ;
- contrôle de la distribution des âges et du genre ;
- redimensionnement des radiographies à une taille compatible avec la mémoire disponible ;
- normalisation des pixels via rescaling ;
- augmentation légère avec rotation, zoom et translation ;
- exclusion du retournement horizontal, car il inverserait la latéralité de la main.

Le notebook d'exploration a aussi servi à vérifier visuellement les radiographies et à valider le format des données avant l'entraînement.

## Notebooks du projet

### [01_eda_preprocessing.ipynb](drafts/01_eda_preprocessing.ipynb)

Notebook d'exploration initiale et de prétraitement. Il sert à comprendre la structure du dataset, observer la distribution cible, afficher des exemples d'images et tester les opérations de nettoyage et de normalisation.

### [02_baseline_cnn.ipynb](drafts/02_baseline_cnn.ipynb)

Première baseline CNN entraînée from scratch. Cette version permet de mesurer le comportement brut du modèle sans régularisation avancée.

Résultat observé : validation MAE autour de 33.95 mois.

### [03_regularization_tuning.ipynb](drafts/03_regularization_tuning.ipynb)

Version améliorée de la baseline avec Batch Normalization, Dropout, Early Stopping et régularisation L2. Ce notebook sert à étudier l'effet de la régularisation sur l'overfitting et la stabilité de l'entraînement.

Résultat observé : validation MAE autour de 33.39 mois, avec une amélioration faible mais réelle par rapport à la baseline.

### [04_transfer_learning.ipynb](drafts/04_transfer_learning.ipynb)

Notebook consacré au transfer learning avec un backbone pré-entraîné, puis une phase de fine-tuning légère. C'est l'approche qui s'est révélée la plus efficace sur ce projet.

Résultat observé : validation MAE autour de 14.37 mois et R² de 0.8116.

### [final_pipeline_bone_age.ipynb](notebooks/final_pipeline_bone_age.ipynb)

Notebook final propre et commenté. Il rassemble le pipeline retenu, les courbes d'apprentissage, les comparaisons de modèles, les prédictions et les visualisations Grad-CAM.

## Démarche expérimentale

### 1. Baseline CNN

Une architecture convolutionnelle simple a été utilisée comme point de départ. L'objectif était d'obtenir une référence de performance et d'observer la capacité du réseau à apprendre sans stratégie de régularisation complexe.

### 2. Régularisation

La baseline a ensuite été enrichie avec :

- Batch Normalization après les blocs convolutionnels ;
- Dropout avant les couches denses ;
- Early Stopping sur `val_loss` ;
- régularisation L2.

Cette étape a réduit le surapprentissage, mais les performances sont restées proches de la baseline.

### 3. Transfer learning

Un modèle pré-entraîné sur ImageNet a ensuite été utilisé, avec une stratégie en deux temps :

- gel du backbone au début pour entraîner uniquement la tête de régression ;
- fine-tuning léger des dernières couches avec un faible learning rate.

Cette stratégie a apporté le gain le plus important, ce qui confirme que les représentations pré-apprises sont très utiles pour ce type de tâche.

## Métriques et visualisations

Les notebooks produisent plusieurs artefacts de suivi et d'interprétation :

- MAE pour mesurer l'erreur moyenne en mois ;
- MSE pour pénaliser les erreurs plus grandes ;
- courbes de loss train / validation ;
- scatter plot âge réel vs âge prédit ;
- Grad-CAM pour localiser les zones de l'image utilisées par le modèle.

Le pipeline final contient également un suivi du learning rate pendant l'entraînement.

## Application Streamlit

Le dossier [streamlit_app/](streamlit_app/) contient une base pour présenter le modèle sous forme d'application interactive.

Fonctionnalités prévues :

- upload d'une radiographie ;
- prétraitement automatique avant inférence ;
- affichage de l'âge osseux estimé en mois ;
- chargement du modèle exporté au format `.keras` ;
- déploiement possible sur Streamlit Community Cloud ou Hugging Face Spaces.

Le fichier [streamlit_app/requirements.txt](streamlit_app/requirements.txt) regroupe les dépendances nécessaires à cette interface.

## Support de soutenance

Le dossier [presentation/](presentation/) contient le support de présentation du projet. Une soutenance claire peut suivre cette trame :

1. contexte, problématique et objectif médical ;
2. description du dataset et du prétraitement ;
3. baseline CNN ;
4. version régularisée ;
5. transfer learning ;
6. comparaison des résultats ;
7. interprétation avec Grad-CAM ;
8. démo Streamlit ;
9. conclusion, limites et pistes d'amélioration.

## Limites et points de vigilance

- L'âge osseux est une régression continue, pas une classification.
- Les résultats doivent être interprétés avec prudence dans un contexte médical.
- Le dataset peut contenir des biais liés à l'âge, au genre ou à la qualité d'acquisition.
- Les expériences doivent être reproductibles et bien documentées.

## Interprétation des résultats

Le meilleur modèle sélectionné dans le notebook final est le transfer learning basé sur EfficientNetB0. Le gain de performance par rapport à la baseline montre qu'un backbone pré-entraîné est particulièrement adapté à cette tâche, alors qu'un CNN entraîné from scratch a plus de mal à généraliser sur un dataset médical de cette taille.

En pratique, cela signifie que le projet démontre trois idées importantes :

- les radiographies peuvent être exploitées efficacement avec des CNN ;
- la régularisation seule ne suffit pas toujours à combler l'écart de performance ;
- le transfer learning apporte ici le meilleur compromis entre simplicité et précision.

## Pour aller plus loin

1. Tester d'autres backbones pré-entraînés pour comparer leur efficacité.
2. Raffiner la stratégie d'augmentation et de fine-tuning.
3. Compléter la démo Streamlit avec une page d'explication des prédictions.
4. Ajouter un suivi d'expériences plus formel pour faciliter la reproductibilité.
