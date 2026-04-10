# Darkly - Writeup : exposition de donnée importante via cookie

## Analyse

En inspectant les cookies de la page, on remarque qu’une valeur est stockée en clair : ```68934a3e9455fa72420237eb05902327```.

## Exploitation

Cette valeur ressemble à un hash de type MD5. On le décryptant on se rend compte que le hash vaut `False`. Il suffit donc de modifier la valeur du cookie par `True` en MD5.

## Vulnérabilités

* Stockage de données sensibles côté client (cookies)  
* Confiance excessive du serveur aux données fournies par le client

## Conclusion

Cette faille illustre clairement pourquoi il ne faut jamais stocker d’informations critiques dans les cookies ou exposer des données sensibles côté client. La vulnérabilité permet la récupération directe du flag de façon triviale.