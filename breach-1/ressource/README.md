# Darkly - Writeup : exposition du flag

## Analyse

Dans les cookies se trouve en clair un flag.

## Récupération du flag

Inspection des requêtes via les outils développeur du navigateur.

Le flag est présent dans les cookies de la requête.

## Vulnérabilités

* Stockage de données sensibles côté client (cookies)

## Bonnes pratiques

* Ne jamais stocker d’informations sensibles dans les cookies

## Conclusion

Des données sensibles sont exposées côté client, permettant une récupération triviale du flag.
