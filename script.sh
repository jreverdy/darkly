#!/bin/bash

# Boucle de 1 à 14
for i in $(seq 1 14)
# Utilisation de {1..14} pour générer la séquence
do
    # Nom du dossier principal
    dir="breach-$i"
    
    # Création du dossier breach-x et du sous-dossier ressource simultanément
    mkdir -p "$dir/ressource"
    
    # Création du fichier flag à l'intérieur du dossier breach-x
    touch "$dir/flag"
    
    echo "Dossier $dir créé avec succès."
done

echo "Terminé ! 14 structures ont été générées."