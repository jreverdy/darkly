#!/bin/bash

for i in $(seq 1 14)
do
    dir="breach-$i"
    
    mkdir -p "$dir/ressource"
    
    touch "$dir/flag"
    
    echo "Dossier $dir créé avec succès."
done

echo "Terminé ! 14 structures ont été générées."