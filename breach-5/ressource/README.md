# Darkly - Writeup : Accès à une page via paramètre hashé

## Analyse

À un moment, on tombe sur une page contenant un formulaire. En rejouant la requête avec `curl` et en envoyant une valeur d’input plus grande que celle prévue, on parvient à obtenir le flag.

Cela montre que la validation côté client est contournable et qu’aucune vérification stricte n’est effectuée côté serveur.

## Bonnes pratiques

Il est important de valider les entrées utilisateur, aussi bien côté front pour l’expérience utilisateur que côté back pour la sécurité.  

Dans ce cas précis, le serveur aurait dû restreindre les valeurs acceptées (par exemple de 1 à 10, comme indiqué dans le formulaire) et vérifier systématiquement les données reçues.