# Darkly - Exploitation robots.txt - /whatever

## Analyse

Dans le fichier robots.txt situé à l'URL `http://x.x.x.x/robots.txt`, on trouve des instructions destinées aux outils de scraping.
On y remarque une ligne `Disallow: /whatever`.
À cette URL, on trouve un fichier `htpasswd`.
Ce fichier contient une seule ligne : `root:437394baff5aa33daa618be47b75cb49`.

## Exploitation

On peut déduire que cette ligne correspond à un nom d'utilisateur (`root`) et un mot de passe hashé (`437394baff5aa33daa618be47b75cb49`).
On tente de déchiffrer le hash en supposant qu'il repose sur l'algorithme MD5. On obtient : `qwerty123@`.
En saisissant ces identifiants sur la page `http://x.x.x.x/admin`, on obtient le flag.

## Bonnes pratiques

- **Ne jamais exposer un fichier `.htpasswd` publiquement** : ce fichier contient des identifiants et doit être stocké en dehors de la racine web ou protégé par une règle serveur explicite (ex. `Deny from all` sur Apache).
- **Utiliser un algorithme de hachage robuste** : MD5 est obsolète et non adapté au stockage de mots de passe. Il est extrêmement rapide à bruteforcer et des bases de hash précalculés (rainbow tables) permettent de le casser en quelques secondes. Lui préférer **bcrypt**, **argon2** ou **scrypt**, qui sont intentionnellement lents et résistants aux attaques par force brute.
- **Choisir des mots de passe solides** : `qwerty123@` est un mot de passe prévisible figurant dans tous les dictionnaires d'attaque courants. Un mot de passe robuste doit être long (16 caractères minimum), aléatoire et unique pour chaque service. L'usage d'un gestionnaire de mots de passe est fortement recommandé.
- **Ne jamais lister de ressources sensibles dans `robots.txt`** : comme pour `/.hidden`, indiquer `/whatever` dans ce fichier revient à signaler publiquement son existence à tout acteur malveillant.
