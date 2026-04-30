# Darkly - Writeup : Mail Recover

## Analyse

Sur la page de récupération de mot de passe, il y a un bouton permettant d’envoyer une demande, mais aucun champ ne permet de renseigner une adresse email.

Nous avons donc copié la requête envoyée par ce bouton, puis modifié les données afin d’y insérer une adresse email différente.

Dans la réponse à cette requête modifiée, le flag est présent.

## Bonnes pratiques

Il ne faut pas définir d’adresse email par défaut pour la réception des demandes de réinitialisation de mot de passe.
Il est également important de valider côté serveur les données envoyées par l’utilisateur, notamment l’adresse email utilisée.

Cette vulnérabilité semble principalement due à une mauvaise implémentation du mécanisme de récupération de mot de passe.