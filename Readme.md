# Estimation de l'âge osseux par Deep Learning

Projet académique de Deep Learning basé sur le défi RSNA Bone Age. L'objectif est d'estimer l'âge osseux, exprimé en mois, à partir de radiographies de la main gauche d'enfants.

Le projet couvre le pipeline complet : exploration des données, prétraitement, augmentation, entraînement de modèles CNN, transfer learning, gestion du surapprentissage et interprétation des prédictions.

## Objectifs

- Construire une baseline CNN simple.
- Améliorer les performances avec Batch Normalization, Dropout, Early Stopping et régularisation L2.
- Comparer une approche from scratch avec du transfer learning sur un modèle pré-entraîné.
- Visualiser les résultats avec des courbes d'apprentissage, des scatter plots et Grad-CAM.
- Préparer une démo Streamlit et une présentation orale claire.

## Structure du dépôt

```text
data/                  Données à télécharger plus tard, dossier laissé vide pour le moment
drafts/                Notebooks de brouillon et expérimentations
  01_eda_preprocessing.ipynb
  02_baseline_cnn.ipynb
  03_regularization_tuning.ipynb
  04_transfer_learning.ipynb
notebooks/             Notebook final propre et commenté
  final_pipeline_bone_age.ipynb
streamlit_app/         Application Streamlit bonus
  app.py
  requirements.txt
presentation/          Support de soutenance
  soutenance_dl.pptx
README.md               Ce fichier
```

## Rôle des notebooks

### 01_eda_preprocessing.ipynb

Notebook d'exploration des données et de prétraitement. Il sert à comprendre la distribution des âges, vérifier le format des images, tester le redimensionnement, la normalisation et les augmentations de base.

### 02_baseline_cnn.ipynb

Première expérience d'apprentissage profond avec un CNN simple entraîné from scratch. Ce notebook sert de baseline pour mesurer les performances brutes du modèle sans régularisation avancée.

### 03_regularization_tuning.ipynb

Version améliorée du CNN baseline avec Batch Normalization, Dropout, Early Stopping et régularisation L2. L'objectif est d'étudier l'impact de ces techniques sur le surapprentissage et la stabilité de l'entraînement.

### 04_transfer_learning.ipynb

Notebook consacré au transfer learning avec un modèle pré-entraîné comme ResNet50 ou EfficientNet. Il permet de comparer une approche basée sur des poids pré-entraînés avec le CNN construit from scratch.

## Démarche recommandée

### 1. Préparation et prétraitement

Le dataset étant volumineux, il faut travailler avec des générateurs ou des pipelines de type tf.data.Dataset ou DataLoader afin d'éviter de tout charger en mémoire.

- Télécharger le dataset RSNA Bone Age depuis Kaggle.
- Vérifier la distribution des âges et du genre.
- Redimensionner les images, par exemple en 256x256 ou 512x512 selon les ressources disponibles.
- Normaliser les pixels avec un rescaling adapté au modèle utilisé.
- Choisir un batch_size compatible avec la RAM et la VRAM.
- Appliquer une augmentation légère : rotation, zoom, translation.
- Ne pas utiliser de retournement horizontal, car la main gauche deviendrait une main droite.

### 2. Expérimentations

#### Baseline CNN

Construire un CNN simple avec plusieurs blocs convolutionnels suivis de couches denses.

Objectif : établir une référence de performance et observer le surapprentissage.

#### Régularisation

Reprendre la baseline et ajouter :

- Batch Normalization après les convolutions.
- Dropout avant les couches denses.
- Early Stopping sur val_loss.
- Régularisation L2 sur les couches denses.

Objectif : montrer l'effet de la régularisation sur les courbes d'entraînement et de validation.

#### Transfer learning

Utiliser un modèle pré-entraîné sur ImageNet, comme ResNet50 ou EfficientNet.

- Geler le base model au début.
- Entraîner uniquement la tête de régression.
- Puis faire un fine-tuning léger sur les dernières couches avec un learning rate faible.

## Notebook final

Le notebook final dans notebooks/final_pipeline_bone_age.ipynb doit être propre, lisible et centré sur la démonstration du pipeline final.

- Introduction et problématique.
- Chargement des données, prétraitement et augmentation.
- Définition des modèles.
- Entraînement, validation et callbacks.
- Comparaison des architectures.
- Interprétation des résultats.

### Métriques et visualisations

- MAE : erreur moyenne absolue en mois.
- MSE : erreur quadratique moyenne.
- Courbes de loss train / validation.
- Scatter plot âge réel vs âge prédit.
- Grad-CAM pour visualiser les zones d'attention.

Si une matrice de confusion ou une courbe ROC est demandée, il est possible de discrétiser l'âge en classes, par exemple :

- Enfant jeune : moins de 5 ans.
- Enfant moyen : de 5 à 12 ans.
- Adolescent : plus de 12 ans.

## Application Streamlit

Le dossier streamlit_app/ peut servir de bonus de présentation.

- Sauvegarder le meilleur modèle au format final .keras si le projet reste sur TensorFlow/Keras. Si une version PyTorch est utilisée, exporter en .pt.
- Créer une interface d'upload d'image.
- Prétraiter l'image avant prédiction.
- Afficher l'âge estimé en mois.
- Prévoir un fichier requirements.txt avec les dépendances nécessaires.
- Déployer sur Streamlit Community Cloud ou Hugging Face Spaces.

## Plan de soutenance

### Proposition de slides

1. Titre, contexte et problématique.
2. Dataset, distribution et prétraitement.
3. Architecture CNN régularisée.
4. Architecture transfer learning.
5. Résultats et comparaison.
6. Interprétation avec Grad-CAM.
7. Démonstration de l'application Streamlit.
8. Conclusion, limites et pistes d'amélioration.

### Questions fréquentes

- MLP vs CNN vs RNN : un CNN est adapté aux images grâce aux filtres convolutifs et au partage de poids.
- Vanishing / exploding gradients : problèmes classiques des réseaux profonds, atténués par ReLU, BatchNorm et les connexions résiduelles.
- BatchNorm, Dropout et Early Stopping : techniques complémentaires pour stabiliser et régulariser l'entraînement.
- Fonction de perte et optimiseur : MAE ou MSE pour la régression, Adam comme choix robuste et standard.

## Points de vigilance

- L'âge osseux est une tâche de régression continue, pas une classification.
- Les résultats doivent être interprétés avec prudence dans un contexte médical.
- Le dataset peut contenir des biais liés à l'âge, au genre ou à la qualité des images.
- Les expériences doivent être reproductibles et bien documentées dans le notebook final.