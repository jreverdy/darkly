# Darkly - Writeup : Accès à une page via paramètre hashé

## Analyse

Face à cette page de connexion, nous avons d’abord tenté une attaque par brute force en développant un script Python capable de rejouer la requête avec chaque mot de passe issu d’une liste de mots de passe courants.

Cependant, cette approche s’est révélée rapidement inefficace. Le temps de réponse du serveur, combiné à la taille du dictionnaire (plusieurs dizaines de milliers d’entrées), rendait l’attaque beaucoup trop lente.

Nous nous sommes donc tournés vers un outil spécialisé, plus adapté à ce type d’attaque : Hydra. Cet outil permet de paralléliser les requêtes et d’accélérer considérablement le processus.

Commande utilisée :

```
docker run -v /home/jereverd/Downloads:/data --rm vanhauser/hydra -l admin -P /data/rockyou.txt 10.14.200.154 http-get-form "/index.php:page=signin&username=admin&password=^PASS^&Login=Login:F=images/WrongAnswer.gif" -o /data/results.log -F
```


Cette commande indique à Hydra :
- d’utiliser le login `admin`
- de tester les mots de passe du fichier `rockyou.txt`
- d’envoyer des requêtes HTTP GET avec les paramètres du formulaire
- de détecter un échec via la présence de `images/WrongAnswer.gif`
- de s’arrêter dès qu’un mot de passe valide est trouvé (`-F`)

Le mot de passe trouvé est : `shadow`

## Bonnes pratiques

Pour se protéger contre ce type d’attaque, plusieurs mesures doivent être mises en place :

- Limiter le nombre de requêtes par IP (rate limiting) afin d’empêcher les attaques automatisées
- Introduire un délai entre les tentatives échouées pour ralentir les attaques par brute force
- Imposer des mots de passe forts (longs, complexes et uniques)
- Mettre en place un mécanisme de blocage temporaire après plusieurs tentatives échouées
- Utiliser une méthode POST plutôt que GET pour éviter l’exposition des identifiants dans l’URL
- Stocker les mots de passe de manière sécurisée (hash + salt)