# Darkly - Writeup : Accès à une page via paramètre hashé

## Analyse

Sur la page d’accueil, un lien "copyright" est présent :

```
?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f
```

Ce lien utilise le paramètre `page` avec une valeur hashée au lieu d’un nom de fichier classique.

En cliquant sur ce lien, on accède à une page spécifique correspondant au copyright.

Le paramètre hashé agit comme un identifiant de page.

## Bonnes pratiques

Ne pas laisser d'informations privées ou confidentielles dans les parametres d'URL.