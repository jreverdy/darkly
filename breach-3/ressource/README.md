# Darkly - Writeup : Accès à une page via paramètre hashé

## Analyse

Sur la page d’accueil, un lien "copyright" est présent :

```
?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f
```

Ce lien utilise le paramètre `page` avec une valeur hashée au lieu d’un nom de fichier classique.

## Exploitation

En cliquant sur ce lien, on accède à une page spécifique correspondant au copyright.

Le paramètre hashé agit comme un identifiant de page.

## Résultat

La page contient directement le flag.

## Conclusion

L’application utilise des identifiants hashés pour référencer certaines pages. Bien que cela donne une impression d’obfuscation, ces liens restent accessibles et visibles côté client, ce qui permet d’accéder directement à des ressources sensibles.
