# Darkly - Exploitation téléchargement script changement type image

## Analyse

Sur la page `http://10.12.200.60/?page=upload#`, on peut télécharger une image.  
On remarque que l'on peut téléverser tout type de fichier.  
On décide alors d'essayer de téléverser un script PHP en changeant son type en image lors de la requête POST.

## Exploitation

Écriture d'un script PHP quelconque. On téléverse ce script en changeant le `Content-Type` en `image/jpeg`.  
Le flag s'affiche dans la réponse.

## Bonnes pratiques

- Valider le type MIME côté serveur (ne pas se fier uniquement au `Content-Type` envoyé par le client).
- Vérifier l'extension et le contenu réel du fichier (analyse des signatures/binaires).
- Restreindre strictement les types de fichiers autorisés (liste blanche).
- Renommer les fichiers uploadés et éviter l'exécution dans le répertoire de stockage.
- Mettre en place des contrôles de taille et de contenu.
